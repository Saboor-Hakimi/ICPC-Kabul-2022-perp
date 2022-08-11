# 
# 
# 
# 

data = [2,2,8,6,9]

final = [-999999999999]
temp = []
for i in data:
    if not i in data and i > final[::-1]:
        final.append(i)
    else:
        temp.append(i)
print(final)
print(temp)
print(final + temp)