th_txt=open(r"D:\PycharmProjects\learning\学习\1234.txt","r+",encoding='UTF-8')
th_list=[]
diameter_list=[]
thickness_list=[]
for line in th_txt:
    for k in range(0,len(line)):
        if line[k] == '*':
            diameter_list.append(line[0:k])
            thickness_list.append(line[k+1:])
diameter_set=set(diameter_list)
thickness_set=set(thickness_list)
diameter_txt=open(r"D:\PycharmProjects\learning\学习\内径.txt", "r+",encoding='UTF-8')
thickness_txt=open(r"D:\PycharmProjects\learning\学习\壁厚.txt", "r+",encoding='UTF-8')
for diameter in diameter_set:
    diameter_txt.write(diameter+'\n')
for thickness in thickness_set:
    thickness_txt.write(thickness)
th_txt.close()
diameter_txt.close()
thickness_txt.close()
