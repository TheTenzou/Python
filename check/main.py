'''
f1 = open('C:\\Users\\dreve\\Music\\music\\Music.m3u', 'r')
f2 = open('C:\\Users\\dreve\\OneDrive\\Рабочий стол\\Music.m3u', 'r')
res = open('res.txt', 'w')

for f1_line in f1:
    if f1_line.split('.')[0].isdigit():
        id = f1_line.split(' ')[0]
        #print(id)

        flag = False
        f2.seek(0)
        for f2_line in f2:
            #if id in f2_line:
            #print(f2_line.find(id) > 0)
            #print(f2_line)
            if f2_line.find(id) > 0:
                #res.write(f2_line)
                flag = True
        if not flag:
            res.write(f1_line)

        #res.write('===================================================================================================\n')
res.close()
f1.close()
f2.close()
'''
f = open('C:\\Users\\dreve\\Music\\music\\Music.m3u', 'r')
contents = f.readlines()
f.close()

#for line in contents:
for i in range(len(contents)):
    if contents[i].split('.')[0].isdigit():
        #print(line)
        contents[i] = '/storage/emulated/0/Music/music/' + contents[i]
        #print(line)

res = open('resl.txt', 'w',  encoding='utf-16')
contents = ''.join(contents)
print(contents)
res.write(contents)
f.close()

