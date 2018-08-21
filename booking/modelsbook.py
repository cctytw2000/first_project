from django.db import connection

class Book:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("""select * from book""") #SQL語法  找BOOK TABLE的全部資料
            datas = cursor.fetchall()  #執行SQL語法 並取多筆 放進 DATAS
        return datas  #回傳DATAS
    def alls(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT *
            FROM booking.book A ,booking.restaurants B 
            where A.restaurantid =  B.restaurantid;""")
            datas = cursor.fetchall()
        return datas
    
    def single(self, id):
        with connection.cursor() as cursor:
            cursor.execute("select * from book where bookid=%s",(id,))  #用ID 來找  BOOK的單筆資料
            data = cursor.fetchone()   #執行SQL語法  並只取一筆  放進DATAS
        return data    #回傳DATAS


    def create(self, booking):
        with connection.cursor() as cursor:
            sql = """insert into book(restaurantid,bookname,bookperson,booktel,bookdate,bookwhen,booktime)
                            values(%s,%s,%s,%s,%s,%s,%s)"""   #新增 BOOK 名單
            cursor.execute(sql, booking)     
        
    def update(self, booking):
        with connection.cursor() as cursor:
            sql = """update book set bookname=%s, bookperson=%s, booktel=%s,
                         bookdate=%s , bookwhen=%s where bookid=%s"""
            cursor.execute(sql,booking)

    def delete(self, id):
        with connection.cursor() as cursor:
            sql = "delete from book where bookid=%s"
            cursor.execute(sql,(id,))