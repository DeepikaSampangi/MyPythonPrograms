
pwd = input("Enter the Password String: ")
score = 0
spl_char = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}",":",";","<",">",",",".","?","/","~","`"]

if len(pwd) >=8:
    score+=25

for s in pwd:
    if s.isupper():
        score+=25
        break

for s in pwd:
    if s.isdigit():
        score+=25
        break

for s in pwd:
    if s in spl_char:
        score+=25
        break

print(score)