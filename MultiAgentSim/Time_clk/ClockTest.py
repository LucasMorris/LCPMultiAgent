import time


num = 0

while num < 10:
    num = int(time.perf_counter())
    if num % 2 == 0:
        clk = 1
        print(clk)
        #t = t+1
    else:
        clk = 0
        print(clk)
        #print(clk)
        #t = t+1