
import time
import pyopencl as cl
import numpy as np
N_LIMIT = pow(2,16)


class PP:
    def __init__(self, path):
        self.memfag = cl.mem_flags
        self.context = cl.create_some_context(interactive=True)
        self.queue = cl.CommandQueue(self.context)
        self.code = "".join(open(path, 'r').readlines())
        self.program = cl.Program(self.context, self.code).build()

    def getQueue(self):
        return self.queue

    def getProgram(self):
        return self.program

    def getFlags(self):
        return self.memfag

    def getContext(self):
        return self.context


if __name__ == '__main__':
    start = time.time()
    p = PP("./prime.cl")
    n, G, L = np.int32(N_LIMIT), pow(2,16), pow(2,8)

    primes=np.zeros(shape=n, dtype=(np.int32))
    dest_buff=cl.Buffer(p.getContext(),p.getFlags().READ_WRITE,primes.nbytes)

    p.getProgram().prime(p.getQueue(),(G,),(L,), dest_buff, n).wait()
    cl._enqueue_read_buffer(p.getQueue(), dest_buff, primes)
    print(time.time() - start)
    c=0

    for i in range(0,len(primes)):
        if primes[i]==1:
            c=c+1
    print(c)

    # create the program


