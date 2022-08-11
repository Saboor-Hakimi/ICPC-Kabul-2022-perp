data = input()

def countChar(char, data):
    count = 0
    for i in data:
        if i=='a':
            count += 1
    return count


non_a = [i for i in data if i != 'a']
a = [i for i in data if i == 'a']
while countChar('a', data) <= len(data)/2:
    non_a = non_a[0:len(non_a)-1]
    data = a + non_a
    
    # countChar('a', data)
    # print(data)
print(len(data))
    