result = 0

for i in range(8):
    if i % 3 == 1:
        result += i
    else:
        result += 1
        
print(result)