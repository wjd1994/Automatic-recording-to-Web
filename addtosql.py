import sqlite3

db = sqlite3.connect('test.db')
cur = db.cursor()

def splitall(e,l):
    a = []
    e2 = e
    for e0 in l:
        a0 = e2.split(e0)
        a.append(a0[0])
        e2 = a0[1]
    a.append(e2)
    return a
def danxuan(e):
    global cur,db
    l = ['A．','B．','C．','D．','难度：','答案：']
    a = splitall(e,l)
    
    cur.execute("insert into text(tx,tm,A,B,C,D,da,nd) \
                values('单项选择题','{}','{}','{}','{}','{}','{}',{})"\
                .format(a[0],a[1],a[2],a[3],a[4],a[6],int(a[5][0])))
    db.commit()
    
def duoxuan(e):
    global cur,db
    l = ['A．','B．','C．','D．','E．','难度：','答案：']
    a = splitall(e,l)
    
    cur.execute("insert into text(tx,tm,A,B,C,D,E,da,nd) \
                values('多项选择题','{}','{}','{}','{}','{}','{}','{}',{})"\
                .format(a[0],a[1],a[2],a[3],a[4],a[5],a[7],int(a[6][0])))
    db.commit()
    
def zhuguan(e):
    global cur,db
    tx = 'zhuguan'
    l0 = ['问答题','简答题','填空题','判断题','名词解释题']
    l = ['难度：','答案：']
    for i in l0:
        if i in e[0]:
            tx =  i
            break
            
    a = splitall(e[1],l)
    cur.execute("insert into text(tx,tm,da,nd) values('{}','{}','{}',{})".format(tx,a[0],a[2],int(a[1][0])))
    db.commit()
f = open('file1.txt')
s = f.read()
l = s.split('题型：')

l1=[]
for e in l:
    e = e.split('+++')
    if len(e) < 2:
        continue
    if '单项选择题' in e[0]:
        danxuan(e[1])
    elif '多项选择题' in e[0]:
        duoxuan(e[1])
    else:
        zhuguan(e)
print('ok')

cur.close()
db.close()
f.close()
