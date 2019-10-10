def task_1():
    a=''
    for i in range(0,10,1):
            a+=str(i)*i+'\n'
      
    return a
a = task_1()
print(a)
assert task_1() == '''
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''