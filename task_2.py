def task_2():
    a=''
    b=''
    for i in range(1,10):
        if(i<=5):
            if(i==1):
                a=a+'*\n'
            elif(i==2):
                a+='**\n'
            elif(i==3):
                a+='***\n'
            elif(i==4):
                a+='****\n'
            elif(i==5):
                a+='*****\n'
            
        else:
            if(i==6):
                a=a+'****\n'
            elif(i==7):
                a+='***\n'
            elif(i==8):
                a+='**\n'
            elif(i==9):
                a+='*'

    #print(a)                
    return a                    
a = task_2()
print(a)
assert task_2() == '''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''