#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/fs.h>
#include <asm/uaccess.h>
#include <linux/dmaengine.h>
#include <linux/dma-mapping.h>

MODULE_AUTHOR("Guo Chaohong");
MODULE_DESCRIPTION("An example to demo DSA memory copy");
MODULE_LICENSE("GPL");



static bool is_dsa_dma(struct dma_chan *chan, void *filter_param)
{
	if (!chan) 
		printk("Got NULL channel\n");
	else if (chan->name)
		printk("Got channel: name=%s\n", chan->name);
	else 
		printk("channel has not set name\n");

	return true;
}

void cb_tx_done(void *param)
{
        struct completion *done = (struct completion *) param;
	printk("callback of tx completed is being called\n");
        complete(done);
}


void test(void)
{
	dma_cap_mask_t mask;
	u32	pp;
	struct dma_chan *ch;
	u8 *src_buf, *dst_buf;
	dma_cookie_t cookie;
        dma_addr_t src_addr, dst_addr;
	struct completion done;	
	struct dma_async_tx_descriptor *desc;
	int ret;

	
#define COPY_SIZE 4096
#define TIMEOUT_TX_DMA 1000 

	dma_cap_zero(mask);
	dma_cap_set(DMA_MEMCPY, mask);

	ch = dma_request_channel(mask,  is_dsa_dma, (void *)&pp);
	if (!ch) {
		printk("Failed to call dma_request_channel\n");
		return;
	}

	src_buf = dma_alloc_coherent(ch->device->dev, COPY_SIZE, &src_addr, GFP_KERNEL);
        dst_buf = dma_alloc_coherent(ch->device->dev, COPY_SIZE, &dst_addr, GFP_KERNEL);

	printk("src=0x%lx, dst=0x%lx\n", src_buf, dst_buf);

	memset(src_buf, 'S', COPY_SIZE);
	memset(dst_buf, 'D', COPY_SIZE);
	printk("Before DMA: src_buf[0] = %c\n", src_buf[0]);
	printk("Before DMA: dst_buf[0] = %c\n", dst_buf[0]);

	desc = dmaengine_prep_dma_memcpy(ch, dst_addr, src_addr, COPY_SIZE, DMA_PREP_INTERRUPT | DMA_MEM_TO_MEM);
//	desc = dmaengine_prep_dma_memcpy(ch, dst_addr, src_addr, COPY_SIZE, DMA_MEM_TO_MEM);
	if (!desc) {
		printk("Failed to call dmaengine_prep_dma_memcpy\n");
		goto out;
	}
	
	init_completion(&done);
	
	desc->callback = cb_tx_done;
	desc->callback_param = &done;

	cookie = dmaengine_submit(desc);
	if (dma_submit_error(cookie)) { 
		printk("Failed to call dmaengine_submit\n");
		goto out;
	}

	/* kick tx DMA  */
	dma_async_issue_pending(ch);

	if(wait_for_completion_timeout(&done, msecs_to_jiffies(TIMEOUT_TX_DMA)) <= 0) {
		printk("dma tx timeout\n");
	}

	ret = dma_async_is_tx_complete(ch, cookie, NULL, NULL);
	if (ret == DMA_COMPLETE) {
		if( memcmp(src_buf, dst_buf, COPY_SIZE) == 0)
			printk("good to memory copy\n");
	} else {
		printk("dma_async_is_tx_complete failed, retval=%d\n", ret);
	}

	dmaengine_terminate_all(ch);

out:
	printk("After DMA: src_buf[0] = %c\n", src_buf[0]);
	printk("after DMA: dst_buf[0] = %c\n", dst_buf[0]);
	dma_free_coherent(ch->device->dev, COPY_SIZE, src_buf, src_addr);
        dma_free_coherent(ch->device->dev, COPY_SIZE, dst_buf, dst_addr);

	if (ch) {
		printk("Release DMA channel\n");
		dma_release_channel(ch);
	}

}

static int __init dsa_test_init(void)
{
	printk("initalizeing dsaexample module...\n");

	test();

	return 0;
}

static void __exit dsa_test_exit(void)
{
	printk("unload dsaexample module...\n");
}

module_init(dsa_test_init);
module_exit(dsa_test_exit);


