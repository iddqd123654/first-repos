import random  as r
def getHealth():
    health = 100
    while True:
        a = r.randint(1,20)
        #b = r.randint(1, 20)
        #if a>b:
            #health-=20
        #if health <= 0:
           # print("Ваше здоровье закончилось")
            #break
getHealth()

def getHealth1(a,b):
    if a > b:
        return True
    else:
        return False

hp = 100
while hp >0:
    a = r.randint(1, 20)
    b = r.randint(1, 20)
    if getHealth1(a ,b ):
        hp -=20
print("Ваше здоровье закончилось")