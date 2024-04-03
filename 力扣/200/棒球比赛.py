def calPoints(operations):
    def if_integer(string):
        try:
            int(string)
            return True
        except ValueError:
            return False
    operations_sum = 0
    list_text=[]
    for i in range(0,len(operations)):
        if if_integer(operations[i]):
            operations_sum += int(operations[i])
            list_text.append(int(operations[i]))
        elif operations[i] == 'C':
            operations_sum -= list_text[-1]
            del list_text[-1]
        elif operations[i] == 'D':
            operations_sum += 2 * list_text[-1]
            list_text.append(2 * list_text[-1])
        elif operations[i] == '+':
            operations_sum += list_text[-1] + list_text[-2]
            list_text.append(list_text[-1]+list_text[-2])
    return operations_sum

print(calPoints(["8373","C","9034","-17523","D","1492","7558","-5022","C","C","+","+","-16000","C","+","-18694","C","C","C","-19377","D","-25250","20356","C","-1769","-8303","C","-25332","29884","C","+","C","-29875","-15374","C","+","14584","13773","+","17037","-28248","+","16822","D","+","+","-19357","-26593","-8548","4776","D","-8244","378","+","-19269","-25447","18922","-16782","2886","C","-17788","D","-22256","C","308","-9185","-19074","1528","28424","D","8658","C","7221","-13704","8995","-21650","22567","-29560","D","-9807","25632","6817","28654","D","-18574","C","D","20103","7875","C","9911","23951","C","D","C","+","18219","-20922","D","-24923"]))