import random

worldlist = ["driver","gardner","mother","school","college","computer","tubelight","spectacles","tortoise","museum","festival","vegetable","medicine","electricity","switch","umbrella","keyboard"]

word = random.choice(worldlist)
n = len(word)
play = True
g = 5
gword = ""
gchar = []
m = random.randint(0,len(word)-1)
cm = word[m]
gchar.append(cm)
for ch in word:
    if ch==cm:
        gword+=cm+" "
    else:
        gword+="_ "


print("hi, i have guesed the following word")
print(gword)
while play:
    if g == 0:
        print("Your chances are over. the corect word is ->",word)
        break
    c = input("Enter your guesed character-> ")
    if c in gchar:
        g-=1
        print("you already guesed this. Remaining wrong chance is",g)
    elif c in word:
        tword=""
        gchar.append(c)
        for i in range(len(word)):
            ch=word[i]
            if ch==c:
                tword+=c+" "
            elif gword[i*2] != "_":
                tword+=gword[i*2]+" "
            else:
                tword+="_ "  
        gword=tword      
        print(gword)
        tword=""
        for i in range(len(gword)):
            if gword[i]=="_" or gword[i]==" ":
                continue
            tword += gword[i]
        if tword == word:
            print("you won! congrats...")
            break
    else:
        g-=1
        print("Sorry, wrong guess. Reamaining wrong chances is",g)
        print(gword)