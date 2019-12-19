import os



def c(x):
    os.system(x)

c("open https://www.instagram.com")

r = Region(2,154,1241,613)

wait("1576670021610.png", FOREVER)

while True:
    if not r.exists("1576670063574.png"):
        type(Key.PAGE_DOWN)
        wait(2)
    else:
        r.click("1576670080591.png")
        wait(1)
        continue
