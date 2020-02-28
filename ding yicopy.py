'''
    定义copy
    循环copy
'''
def copy(file1,file2):
    a=open(file1,"r")
    b=open(file2,"a")
    while True:
        i=a.read(2)
        if not i:
            break
        b.write(i)

copy("/home/tarena/AID1912/day04/4.txt","5.txt")


