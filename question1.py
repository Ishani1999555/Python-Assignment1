

result =[]
for i in range(1500,2701):
    if i%5==0 and i%7 ==0:
        result.append(i)

print("numbered list is: ", result)