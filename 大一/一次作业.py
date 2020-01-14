import os,random,sys,time
object_number=random.randint(1,1000)#dong's part
for i in range(object_number):
    fp=open("elder"+str(i)+".txt",'w')
    row_number=random.randint(1,1000)
    for j in range(row_number):
        length_number=random.randint(1,20)
        str_said=""
        for k in range(length_number):
            str_said+=str(random.randint(0,9))
        fp.write(str_said+'\n')
    fp.close()
start_time=time.clock()#my part
abcd=0
g=0
list_elder=[]
while(len(open("elder%s.txt"%(str(abcd)),"r").readlines())!=0):#find how many elders
    st_number=len(open("elder%s.txt"%(str(abcd)),"r").readlines())
    test_number=int(st_number*(1e3)+(1000-abcd))
    list_elder.append(test_number)
    abcd+=1
    e=open('elder%s.txt'%(str(abcd)),'a')
    e.write('')
    if (len(open("elder%s.txt"%(str(abcd)),"r").readlines())==0):
        file_number=abcd-1
list_elder.sort()
dic_elder={}
for i in range(file_number+1):
    a=str(list_elder[-(i+1)])
    b=int(str(a)[-3:])
    c=1000-b
    dic_elder[i+1]="elder%s.txt"%(str(c))
print(dic_elder)#the answer
end_time=time.clock()
print(end_time-start_time)#use time
