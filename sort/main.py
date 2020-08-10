def mykey(s):
    id = s.split(' ')[0]
    id = id.split('/')[-1]
    numbers = id.split('.')
    numbers = numbers[:len(numbers) - 1]
    sum = 0.0
    mult = 1.0
    for number in numbers:
        sum += int(number) * mult
        mult /= 1000
    return sum


file = open('playlist.txt', 'r', encoding='utf-8')
contents = file.readlines()
file.close()
print(contents)

contents.sort(key=mykey, reverse=True)

res = open('Music.m3u', 'w',  encoding='utf-8')
contents = ''.join(contents)
print(contents)
res.write(contents)
