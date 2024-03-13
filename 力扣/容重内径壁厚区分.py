th_txt=open("D:\\PycharmProjects\\learning\\学习\\1234.txt","r+",encoding='UTF-8')
th_list=[]
density_list=[]
diameter_list=[]
thickness_list=[]
for line in th_txt:
    for k in range(0,len(line)):
        for j in range(k,len(line)):
            for i in range(j,len(line)):
                for z in range(i,len(line)):
                    if line[k:j].isdigit() and line[j]=='K' and line[k-1]==' ' and line[i]=='*' and line[z]=='(':
                        density_list.append(line[k:j])
                        diameter_list.append(line[j+5:i])
                        thickness_list.append(line[i+1:z])
density_set=set(density_list)
diameter_set=set(diameter_list)
thickness_set=set(thickness_list)
density_txt=open(r"D:\PycharmProjects\learning\学习\容重.txt", "r+",encoding='UTF-8')
diameter_txt=open(r"D:\PycharmProjects\learning\学习\内径.txt", "r+",encoding='UTF-8')
thickness_txt=open(r"D:\PycharmProjects\learning\学习\壁厚.txt", "r+",encoding='UTF-8')
for density in density_set:
    density_txt.write(density+'\n')
for diameter in diameter_set:
    diameter_txt.write(diameter+'\n')
for thickness in thickness_set:
    thickness_txt.write(thickness+'\n')
th_txt.close()
density_txt.close()
thickness_txt.close()
diameter_txt.close()
