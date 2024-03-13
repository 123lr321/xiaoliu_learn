#定义图书馆
Library_management=[{'book':'挪威的森林','author':'村上春树','price':35,'number':40},\
{'book':'三国','author':'罗贯中','price':45,'number':40},\
{'book':'三国','author':'刘润','price':100,'number':2}, \
{'book': 'A Dream of Red Mansions', 'author': '曹雪芹', 'price': 35, 'number': 40},\
{'book':'西游记','author':'吴承恩','price':38,'number':40}]
user={'刘润':'123456','徐越':'234567'}
def user_admin():
    a=input('zhanghao')
    b=input('mima')
    i=0
    for key in user.keys():
        if key==a and user[key]==b:
            return True
        elif key==a and user[key]!=b:
            return False

user_input1=1
while user_input1!=5:
  user_input1=int(input('请输入您所需的功能：\n1.借书\n2.查书\n3.显示所有书籍\n4.还书\n5.退出'))
  #用户想要显示所有书籍
  if user_input1==3:
  #从图书馆遍历获取全部的书籍信息
      for book_information in Library_management:
          print('书名：',book_information['book'],'作者：',\
          book_information['author'],'价格：',book_information['price'],'数量：',book_information['number'])
  #用户想要查询书籍
  elif user_input1==2:
      user_input2=input('请输入您所要查询的书名或作者：')
  #用于记录遍历次数，当遍历次数等于图书馆元素数且无查找结果时报错
      count=0
  #从图书馆中查找并打印查找结果
      for book_find in Library_management:
          if user_input2==book_find['book'] or user_input2==book_find['author']:
              print('书名：',book_find['book'],'作者：',\
              book_find['author'],'价格：',book_find['price'],'数量：',book_find['number'])
          else:
              count+=1
  #当遍历次数等于图书馆元素数且无查找结果时报错
      if count==len(Library_management):
          print('查无此书')
          #当用户想要借书时
  elif user_input1==1:
      user_input2=input('请输入您所要借阅的书名或书作者：')
  #用于收集所有查找结果
      book_find_result=[]
      i=0
  #当遍历次数等于图书馆元素数且无查找结果时报错
      count=0
  #从图书馆中遍历输入结果并记录在book_find_result
      for book_find in Library_management:
          if user_input2==book_find['book'] or user_input2==book_find['author']:
              book_find_result.append(book_find)
              print('序号：',i,'书名：',book_find['book'],'作者：',\
              book_find['author'],'价格：',book_find['price'],'数量',book_find['number'])
              i+=1
          else:
              count+=1
  #当遍历次数等于图书馆元素数且无查找结果时报错
      if count==len(Library_management):
          print('查无此书')
      elif count!=0:
  #用户筛选查找结果
          user_input3=int(input('请输入您所要借阅的书序号：'))
          i=0
          for book_find in Library_management:
              if book_find['book']==book_find_result[user_input3]['book'] and \
                 book_find['author']==book_find_result[user_input3]['author']:
                 if book_find['number']<1:
                     print('此书已无')
                     break
                 Library_management[i]['number']-=1
                 print('借阅成功')
              i+=1
#当用户想要还书时
  elif user_input1==4:
      user_input2=input('请输入您所要归还的书名或书作者：')
  #用于收集所有查找结果
      book_find_result=[]
      i=0
  #当遍历次数等于图书馆元素数且无查找结果时报错
      count=0
  #从图书馆中遍历输入结果并记录在book_find_result
      for book_find in Library_management:
          if user_input2==book_find['book'] or user_input2==book_find['author']:
              book_find_result.append(book_find)
              print('序号：',i,'书名：',book_find['book'],'作者：',\
              book_find['author'],'价格：',book_find['price'])
              i+=1
          else:
              count+=1
  #当遍历次数等于图书馆元素数且无查找结果时报错
      if count==len(Library_management):
          print('查无此书')
      elif count!=0:
  #用户筛选查找结果
          user_input3=int(input('请输入您所要归还的书序号：'))
          i=0
          for book_find in Library_management:
              if book_find['book']==book_find_result[user_input3]['book'] and \
                 book_find['author']==book_find_result[user_input3]['author']:
                 Library_management[i]['number']+=1
              i+=1
          print('归还成功')
  elif user_input1==5:
      print('感谢使用')








