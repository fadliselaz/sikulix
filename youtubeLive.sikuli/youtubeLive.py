import random


msg = ["semoga sehat selalu semuanya guys..",
        "selamat berhari libur guys..",
        "selamat menonton guys..",
        "selamat jalan jalan pagi guys..",
        "selamat menjalankan ibadah puasa guys..."]



r = Region(904,780,453,60)

rt = [5,10,15,20]

while True:
    rMsg = random.choice(msg)
    if exists("1558823927441.png"):
        click("1558823927441.png")
        wait(1)
        type(rMsg.upper())
        wait(3)
        click("1558824031769.png")
        wait(2)

    wait(random.choice(rt))
        