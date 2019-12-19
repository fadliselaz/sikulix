import os
import time

r = Region(10,172,851,593)
textArea = "textArea.png"


r.click(textArea)
wait(1)
r.type('selamat pagi..')
wait(2)
r.type(Key.ENTER)