import random
import stickfigure
word_string=""
word_copy2=""
Wordlist=['Circulation','Discombobulate','Hellfire','Sinners','Ocean','Megalomaniac','Obviously','Tenet','Valkyrie']
word=Wordlist[random.randint(0,5)]
word_copy=word
word_one=word.lower()
dashed_word='_'
for i in range(0,len(word_one)-1):
    dashed_word+='_'
new_list=[]
for i in range(0,len(word_one)):
    new_list.insert(i,'_')
while True:
    if word_copy==word_string:
        print(f"{stickfigure.limb_list[stickfigure.life]}")
        print(f"You have {stickfigure.life} lives left!")
        print("THAT'S A BINGOO! You won!")
        break
    elif stickfigure.lives==stickfigure.life:
        print(dashed_word)
        guessed_letter=input("Type the letter you have guessed:")
        guessed_real=guessed_letter.lower()
        word_copy2=dashed_word
        for j in range(0,len(word_one)):
            if guessed_real in word_one[j]:
                new_list.pop(j)
                if j==0:
                    new_list.insert(j,guessed_real.upper())
                else:
                    new_list.insert(j,guessed_real)
             
        word_string="".join(new_list)      
        dashed_word=word_string
                
        if word_copy2==word_string: #it checks whether there was a match with the previous word_string and the current word_string. If so it means that no change was made during the input. Hence a life is reduced.
            stickfigure.life-=1
            if stickfigure.life==0:
                print(f"You have {stickfigure.life}/6 left! Game Over!")
                print(stickfigure.limb_list[0])
                break

         
        elif word_copy2!=word_string:
            print(word_string)
            print(f"{stickfigure.limb_list[stickfigure.life]}")
            print(f"You have {stickfigure.life}/6 left!")

                
    elif stickfigure.lives!=stickfigure.life:
        stickfigure.lives-=1
        print(f"You have lost a life! {stickfigure.life}/6 lives left!")
        print(stickfigure.limb_list[stickfigure.life])
       
        