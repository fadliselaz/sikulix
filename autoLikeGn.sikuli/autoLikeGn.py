wait(2)

a = Region(882,67,482,709)
click("1566050475344.png")
#click("1558821765373.png")
while True:
    

    if not a.exists("1566050726505.png") or a.exists("1558860859987.png"):
        type(Key.DOWN *3)


    
    
    elif a.exists("1558820256262.png"):
        wait(1)
        a.click("1558820256262.png")
        wait(1)

    else:
        type(Key.DOWN *3)