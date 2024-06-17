'''f=open("n1.txt","x")
print("file created")
print(f.mode)
print(f.closed)
f.close()
print(f.closed)'''
'''f=open("n2.txt","x")
print("file created")
print(f.mode)
print(f.closed)
f.close()
print(f.closed)'''
''''f=open("n1.txt","a")
f.write("....................this is sanchita page thank u .............")
data=('my name is sanchita\n',"i am from bhopal\n","thank u\n")
f.writelines(data)
print(f.writable())'''
'''f=open('n1.txt',"r")
f=open("n1.txt")
print(f.mode)
data=f.read()
print (data)'''
#f.close
'''f.read(50)
f.readline()
f.readlines()
f.readable()'''
#f=open('n1.txt',"a")
'''print(f.mode)
data=f.read(10)
print(data)
data=f.readline()
print(data)
data=f.readlines()
print(data)
print(f.readable())'''
'''f.close
data=f.write('hiiii')
print(data)
f.close'''
# f=open('n1.txt','w')
# f.write("my name is ")
# f=open("n1.txt",'a')
# f.write("iamsan")
#f.close()
f=open("n1.txt",'rb')
'''print(f.tell())
print(f.read(3))
print(f.tell())
print(f.read(7))
print(f.tell())
#print(f.readline())
print(f.tell())
print(f.read(5))'''
'''print(f.tell())
print(f.read(3))
f.seek(0)
print(f.tell())
print(f.read(10))
print(f.tell())
f.seek(15)
print(f.tell())'''
'''print(f.tell())
f.seek(10,0)
print(f.tell())
#f.read(10)
print(f.read(10))'''
#with open("n1.txt","r") as f:
'''with open("n1.txt","rb") as f:
    print(f.read(10))
    print(f.tell())
    #f.seek(10)
    f.seek(10,1)
    print(f.tell())
    print(f.closed)
print(f.closed)'''
