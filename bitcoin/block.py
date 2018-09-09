
from datetime import datetime
from utils import *

import pdb

# block header is 80 bytes
class BlockHeader:
    def __init__(self, f):
        self.version = uint32(f)
        self.prevHash = sha256(f)
        self.merkleRoot = sha256(f)
        self.time = uint32(f)
        self.nBits = uint32(f)
        self.nonce = uint32(f)

# magic(4) + size(4) + header + txcount + tx
class Block:
    def __init__(self, f):
        self.magic = uint32(f)
        self.blocksize = uint32(f)
        self.getBlockHeader(f)
        self.txArray = []
        self.txCount = varInt(f)
        self.getTxArray(f, self.txCount)

    def getBlockHeader(self, f):
        self.blockHeader = BlockHeader(f)

    def utcToStr(self, time):
        utc = datetime.utcfromtimestamp(time)
        return utc.strftime("%Y-%m-%d %H:%M:%S.%f+00:00 (UTC)")

    def getTxArray(self, f, count):
        '''
        if (self.blockHeader.version > 1):
            tx = Tx(f, 1)
            self.txArray.append(tx)
            s = 1
        else:
            s = 0
'''
        s = 0
        for i in range(s, count):
            tx = Tx(f, 0)
            self.txArray.append(tx)

    def blockFileSize(self):
        return self.blocksize + 8

    def __str__(self):
        return """
 {
    Magic: 0x%x 
    BlockSize: %d
    
    BlockHeader 
    {
        version: %d
        prevHash: %s
        merkleRoot: %s
        time: %s
        nBits: 0x%x
        nonce: 0x%x
    }

    txCount: %d
    Tx_begin { %s
    } # Tx_end

 }\n""" \
          %(self.magic,
            self.blocksize,
            self.blockHeader.version,
            toHexString(self.blockHeader.prevHash),
            toHexString(self.blockHeader.merkleRoot),
            self.utcToStr(self.blockHeader.time),
            self.blockHeader.nBits,
            self.blockHeader.nonce,
            self.txCount,
             "\n".join("%s" %tx for tx in self.txArray)
            )

class Tx:
    def __init__(self, f, coinbase):
        self.version = uint32(f)
        self.inputs = []
        self.inCount = varInt(f)
#        pdb.set_trace()
        self.getInputs(f, self.inCount, coinbase)
        self.outputs = []
        self.outCount = varInt(f)
        self.getOutputs(f, self.outCount)
        self.lockTime = uint32(f)

    def __str__(self):
        return """ 
        version: 0x%x
        inCount: %d
        input_begin { %s
        } # input_end
            
        outCount: %d
        output_begin { %s
        } # output_end

        lockTime: %s
        """  %(self.version, 
               self.inCount,
               "\n".join("%s" %txIn for txIn in self.inputs),
               self.outCount,
               "\n".join("%s" %txOut for txOut in self.outputs),
               self.lockTime)


    def getInputs(self, f, count, coinbase):
        for i in range(0, count):
            txIn = TxInput(f, coinbase)
            self.inputs.append(txIn)

    def getOutputs(self, f, count):
        for i in range(0, count):
            txOut = TxOutput(f)
            self.outputs.append(txOut)


class TxInput:
    def __init__(self, f, coinbase):
        self.txID = sha256(f)
        self.vOut = uint32(f)
        self.scriptSigSize = varInt(f)

        if coinbase > 0:
            n = uint8(f)
            self.height = f.read(n)

        self.scriptSig = f.read(self.scriptSigSize)
        self.sequence = uint32(f)

    def __str__(self):
        return """
            txID: %s
            vOut: %d
            sigSize: %d
            sig: %s
            sig: %s
            sequence: %x""" \
                %(toHexString(self.txID), self.vOut, self.scriptSigSize,
                  toHexString(self.scriptSig), self.scriptSig, self.sequence)


class TxOutput:
    def __init__(self, f):
        self.value = uint64(f)
        self.scriptKeySize = varInt(f)
        self.scriptPubkey = f.read(self.scriptKeySize)

    def __str__(self):
        return """
            value: %d;
            keySize: %d;
            pubKey: %s """ \
        %(self.value,
          self.scriptKeySize,
          toHexString(self.scriptPubkey))
