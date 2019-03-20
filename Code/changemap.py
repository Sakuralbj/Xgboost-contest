#Use this to change the log.txt to map.txt
#-*-coding:utf-8-*-
file = open("../Data/feature_label.log")
fo = open( '../Data/feature_map.txt', 'w' )
m=1
flag=True
a=0
for line in file.readlines():
    line=line.strip('\n')
    if ":"  in line:

        str1=line.split(':')
        flag = False
        if m > 1:
            fo.write("\n")
        fo.write(" ")
        fo.write(str(m))
        m=m+1

        fo.write(".")
        fo.write(" ")
        fo.write(str1[0])
        fo.write(":")
        fo.write(" ")

    else:
        if flag:
            fo.write(",")
        str2=line.strip(" ")
        str2=str2.strip("\n")
        str3=str2.split(" ")
        flag=True

        fo.write(str(a))
        a=a+1
        fo.write("=")
        fo.write(str3[0])



