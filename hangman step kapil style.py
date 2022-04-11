import random
from logo import logo,stages
from words import words

print(logo)
chosen=random.choice(words)
c1=len(chosen)
c=range(c1)
end=False
s=len(stages)
lives =s-1
d=[]
for blanks in c:
    d+="_"

while not end:
   guess=input("whats your choice of letter\n").lower()
    
   if guess in d:
       print(f"You've already guessed {guess}")
      
    
   for p in c:
         l=chosen[p]
         if l==guess:
             d[p]=l

    
   if guess not in chosen:
       print(f"{guess} thats not in word for every wrong guess you lose a life")
       lives-=1
       if lives==0:
            end=True
            print("you lose")
   
   if "_" not in d:
     end=True
     print("you win")
   print(f"{' '.join(d)}")  
   print(stages[lives])
print(f"the chosen word was {chosen}")
         

