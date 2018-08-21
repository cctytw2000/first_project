from django.db import connection

class restaurants:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from restaurants")
            datas = cursor.fetchall()
        return datas

    # def create(self):
    #     pass

    # def update(self):
    #     pass