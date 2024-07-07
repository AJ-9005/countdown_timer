import time
def countdown(t):
    while t>0:
        mins,secs=divmod(t,60)
        timer="{:02d}:{:02d}".format(mins,secs)
        print(timer, end="\r\r")
        time.sleep(1)
        t-=1
    print("Boom")
ty=int(input("Enter no of seconds:"))
countdown(ty)
