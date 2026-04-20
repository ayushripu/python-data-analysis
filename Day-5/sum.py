Student_score = [1,2,6,4,5,3]

total_Score= sum(Student_score)
print(total_Score)

sum=0
for score in Student_score:
    sum += score   
print(sum)

max = 0
for score in Student_score:
    if score > max:
        max = score
print(max)