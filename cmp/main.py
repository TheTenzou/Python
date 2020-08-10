f1 = open('full.m3u', 'r', encoding='utf-8')
f2 = open('notfull.m3u', 'r', encoding='utf-8')
res = open('res.txt', 'w', encoding='utf-8')

for f1_line in f1:
    f1_id = f1_line.split(' ')[0]
    f1_id = f1_id.split('/')[-1]
    f1_id += ' '

    flag = False
    f2.seek(0)
    for f2_line in f2:
        f2_id = f2_line.split(' ')[0]
        f2_id = f2_id.split('/')[-1]
        f2_id += ' '
        if f1_id == f2_id:
            flag = True

    if not flag:
        res.write(f1_line.split('/')[-1])

f1.close()
f2.close()
res.close()
