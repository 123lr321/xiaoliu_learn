def tictactoe(moves):
        a_list = []
        b_list = []
        k = 2
        for i in moves:
            if k % 2 == 0:
                a_list.append(i)
            else:
                b_list.append(i)
            k += 1
        if len(a_list)<3:
            return 'Pending'
        for i in range(0,len(a_list)):
            for j in range(0,len(a_list)):
                for k in range(0,len(a_list)):
                    if i!=j and i!=k and j!=k:
                        if a_list[i][0]-a_list[j][0]==a_list[j][0]-a_list[k][0] and a_list[i][1]-a_list[j][1]==a_list[j][1]-a_list[k][1]:
                            return 'A'
        for i in range(0,len(b_list)):
            for j in range(0,len(b_list)):
                for k in range(0,len(b_list)):
                    if i!=j and i!=k and j!=k:
                        if b_list[i][0]-b_list[j][0]==b_list[j][0]-b_list[k][0] and b_list[i][1]-b_list[j][1]==b_list[j][1]-b_list[k][1]:
                            return 'B'
        if len(moves)<=8:
            return 'Pending'
        else:
            return 'Draw'





print(tictactoe([[1,0],[2,2],[0,1],[0,2],[2,1],[1,1],[0,0],[2,0]]))
