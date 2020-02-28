'''
    查找
'''

while True:
    dict = open("dict.txt", "r")
    a = input(">>")
    for line in dict:

        b=line.split(" ")
        if b[0]>a:
            print("没有找到")
            break
        elif a == b[0]:
            print(line)
            break
    else:
        print("no find")







