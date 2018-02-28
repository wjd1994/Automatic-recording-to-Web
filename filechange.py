def removeall(s,e):
    l = ''
    for i in range(len(s)):
        if s[i] == e:
          continue
        l += s[i]
    return l
f = open('file.txt','r')
f1 = open('file1.txt','w')
l = ['单项选择题','多项选择题','问答题','简答题','填空题','判断题','名词解释题']
while True:
    flag = 0
    s = f.readline()
    if not s:
        break
    s = removeall(s,' ')
    s = removeall(s,'\t')
    #s = removeall(s,'．')
    #s = removeall(s,'：')
    if s == '\n':
        continue
    if '（）' in s:
        s = s.replace('（）' , '（  ）')
    if '()' in s:
        s = s.replace('()' , '（  ）')
    for e in l:
        if e in s:
            f1.write('题型：')
            f1.write(s)
            f1.write('+++')
            flag = 1
    if flag == 0:
        f1.write(s)

f1.close()
f.close()
print('ok')
