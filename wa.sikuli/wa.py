import random

r = Region(9,113,852,604)

text = ["hello", "apa kabar", "oy..", "kemana aja lu.."]

rText = random.choice(text)
wait(1)

for i in range(10):
    wait(1)
    if r.exists("1576125828933.png"):
        wait(1)
        click("1576125828933.png")
        wait(1)
        click("1576125849859.png")
        wait(1)
        type(rText)
        wait(1)
        type(Key.ENTER)
