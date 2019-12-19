#like with class
import random
selebgram = ["princesss", "attahal", "lunamaya", "laudyacynthiabella", "agnezmo", "ruben_onsu", "sarwendah29", "viavallen"]

class ig:
    def __init__(self, follow, unfollow, execute, reg, tm):
        self.follow = follow
        self.unfollow = unfollow
        self.execute = execute
        self.reg = reg
        self.tm = tm

    def unfollowing(self):
        e = 0
        roll = 0
        while True: 
            if exists(self.unfollow):

                click(self.unfollow)
                wait(self.execute, FOREVER)
                click(self.execute)
                e += 1
                if e == self.tm:
                    popup("berhasil execute {}".format(self.tm))
                    quit()
                wait(2)

            
            else:
                for x in range(4):
                    type(Key.DOWN *10)
                roll += 1
                if roll >= 5:
                    quit()

    def following(self):
        f = 0
        roll = 0
        while True:
            if exists(self.follow):

                click(self.follow)
                
                f += 1
                #reset roll
                roll = 0
                
                if f == self.tm:
                    popup("Berhasil action {}x".format(self.tm))
                    quit()

                wait(2)

            else:
                for z in range(4):
                    
                    type(Key.DOWN)

                wait(1)
                roll += 1
                if roll >= 2:
                    popup("sudah tidak ada yang bisa di clik..!!")
                    quit()

                    

    def start(self):


        seleb = random.choice(selebgram)
        self.tm = int(input("masukan jumlah action :"))
        tanya = int(input("1. Following\n2. Unfollowing"))
        
        click("1560192418580.png" or "1560192434283.png")
        wait("1560192518344.png",FOREVER)
        click("1560192518344.png")
        wait(1)
        type(seleb)
        wait(5)
        click("1560192649156.png")
        
        wait("1560269637516.png",FOREVER)
        click(Pattern("1560269637516.png").targetOffset(28,39))
        wait("1560192712470.png",FOREVER)
        click("1560192712470.png")
        wait("1560192649156.png",FOREVER)
        
        
        
        
        if tanya == 1:
            self.following()
        elif tanya == 2:
            self.unfollowing()
        else:
            quit()

instagram = ig("1560191080510.png" ,"1560191100848.png" ,"1560191116242.png" ,Region(933,117,452,673) ,20 )

instagram.start()
