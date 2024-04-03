def spiralOrder(matrix):
        anw_list=[]
        def spiral0rder_1(matrix,anw_list):
            for i in matrix[0]:
                anw_list.append(i)
            del matrix[0]
            for i in range(0,len(matrix)):
                anw_list.append(matrix[i][-1])
                del matrix[i][-1]
            if matrix == []:
                return anw_list
            if len(matrix) == 1:
                for i in range(len(matrix[0])-1,-1,-1):
                    anw_list.append(matrix[0][i])
                return anw_list
            for i in range(len(matrix[-1])-1,-1,-1):
                anw_list.append(matrix[-1][i])
            del matrix[-1]
            sum_test = 0
            for i in matrix:
                if i == []:
                    sum_test+=1
            if sum_test == len(matrix):
                return anw_list
            for i in range(len(matrix)-1,-1,-1):
                anw_list.append(matrix[i][0])
                del matrix[i][0]
            if matrix == []:
                return anw_list
            if len(matrix) == 1:
                for i in matrix[0]:
                    anw_list.append(i)
                return anw_list
            sum_test = 0
            for i in matrix:
                if i == []:
                    sum_test+=1
            if sum_test == len(matrix):
                return anw_list
            if len(matrix) >= 2:
                return spiral0rder_1(matrix,anw_list)
        return spiral0rder_1(matrix,[])

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

