from django.db import connection

class restaurant:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from restaurants")
            datas = cursor.fetchall()
        return datas
    
    def single(self, id):
        with connection.cursor() as cursor:
            cursor.execute("select * from restaurants where id=%s",(id,))
            data = cursor.fetchone()
        return data


    def create(self, product):
        with connection.cursor() as cursor:
            sql = """insert into restaurants(rname,rtype,rtel,raddress,rweb,rintroduction)
                            values(%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, product)
        
    def update(self, product):
        with connection.cursor() as cursor:
            sql = """update restaurants set  rname=%s, rtype=%s, rtel=%s, raddress=%s,
                         rweb=%s, rintroduction=%s where id=%s"""
            cursor.execute(sql,product)

    def delete(self, id):
        with connection.cursor() as cursor:
            sql = "delete from restaurants where id=%s"
            cursor.execute(sql,(id,))