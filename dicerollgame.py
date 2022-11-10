import random,time

firstPoints = 0;
secondPoints = 0;
fRandom = 0
sRandom = 0

for x in range(0, 20):
  fRandom = 0
  sRandom = 0
  fRandom = random.randrange(1, 7)  
  sRandom = random.randrange(1, 7)  
  if(fRandom > sRandom):
    firstPoints = firstPoints + 1
  elif(fRandom < sRandom):
    secondPoints = secondPoints + 1
  
print (firstPoints)
print (secondPoints)

if(firstPoints > secondPoints):
    print("pierwszy wygral")
elif(firstPoints < secondPoints):
    print("drugi wygral")
else:
    print("remis")
    
    