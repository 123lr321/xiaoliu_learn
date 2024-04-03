import pymysql


def test_insert():
    conn = pymysql.connect(host='192.168.226.204', port=3306,
                           user='root', password='liu0325',
                           db='liutest', charset='utf8')
    try:
        with conn.cursor() as cursor:
            result = cursor.execute("insert into t_student values (1,'liurun','101')")
            if result == 1:
                print('添加成功')
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()


def test_del():
    no = input('请输入需删除学生编号:')
    conn = pymysql.connect(host='192.168.226.204', port=3306,
                           user='root', password='liu0325',
                           db='liutest', charset='utf8')
    try:
        with conn.cursor() as cursor:
            result = cursor.execute("delete from t_student where no=%s", (no,))
            if result == 1:
                print('删除成功')
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()


def test_select():
    t_select_list=[]
    cno = input('请输入需查询班级编号:')
    conn = pymysql.connect(host='192.168.188.204', port=3306,
                           user='root', password='liu0325',
                           db='liutest', charset='utf8')
    try:
        with conn.cursor() as cursor:
            cursor.execute("select no,name,cno from t_student where cno=%s",(cno, ))
            print(cursor.fetchone())
            for row in cursor.fetchall():
                t_select_list.append({"no":row[0],"name":row[1],"con":row[2]})
            print(t_select_list)
    except pymysql.MySQLError as error:
        print(error)
    finally:
        conn.close()


if __name__ == '__main__':
    test_select()
