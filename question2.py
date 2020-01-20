A="I am a human being"
B="I am good"
C="Good graders study well"
D="Humans love graders"
E="Every human does not study well"
neg_E="Every human study well"#here neg_E is the negation of E
count=0
result=0
truths=[[1,1],[1,0],[0,0],[0,1]]
for value in truths:
    if value[0]==1:
        C="T"
    else: 
        C="F"
    if value[1]==1:
        E="T"
    else:
        E="F"
    if E=="T":
        neg_E="F"
    else:
        neg_E="T"

    for i in (C and E):
        if i=="T":
            count+=1
if count==len(truths):
    result="YES"
else:
    result="NO"
print("Is every human is a good grader? :   ",result)