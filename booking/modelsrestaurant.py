from django.db import connection

class restaurant:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from restaurants")
            datas = cursor.fetchall()
        return datas
    def alls(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT *
FROM booking.book A ,booking.restaurants B 
where A.restaurantid =  B.restaurantid;""")
            datas = cursor.fetchall()
        return datas

    # def create(self):
    #     pass

    # def update(self):
    #     pass