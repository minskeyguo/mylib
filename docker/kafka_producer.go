package main

import "os"
import "log"
import "sync"
import "os/signal"

import "github.com/Shopify/sarama"

func main() {
	config := sarama.NewConfig()
	config.Consumer.Return.Errors = true

	config.Version = sarama.V0_11_0_0
	//	producer, err := sarama.NewAsyncProducer([]string{"localhost:9001", "localhost:9002", "localhost:9003"}, config)
	producer, err := sarama.NewAsyncProducer([]string{"localhost:9001"}, config)

	if err != nil {
		panic("Failed at NewAsyncProducer")
	}

	signals := make(chan os.Signal, 1)
	signal.Notify(signals, os.Interrupt)

	var (
		wg                          sync.WaitGroup
		enqueued, successes, errors int
	)

	wg.Add(1)
	go func() {
		defer wg.Done()
		for range producer.Successes() {
			successes++
		}
	}()

	wg.Add(1)
	go func() {
		defer wg.Done()
		for err := range producer.Errors() {
			log.Println(err)
			errors++
		}
	}()

ProducerLoop:
	for {
		message := &sarama.ProducerMessage{Topic: "my_topic",
			Value: sarama.StringEncoder("testing 123")}
		select {
		case producer.Input() <- message:
			enqueued++
		case <-signals:
			producer.AsyncClose()
			break ProducerLoop
		}
	}

	wg.Wait()
	log.Printf("Successfully produced: %d; errors: %d\n", successes, errors)
}
