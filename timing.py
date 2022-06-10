import time

# put this at the top, before the while loop starts
start= time.time()


# put all this code at the END
end= time.time()

if end - start > 60:
    print("too slow! you lost the game!")
    break
