from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

import datetime
import time
from .models import Booking , Restaurant

# Create your views here.
def index(request):
    name = request.COOKIES['name']
    bookings = Booking.objects.filter(bookname=name)
    # print(request.COOKIES['name'])
    # print(booking)
    return render(request,'booking/index.html',locals())

def create(request):
    if request.method == "POST":
        #取得表單透過POST傳過來的資料
        restaurantname = request.POST['restaurantname']
        bookname = request.POST['bookname']
        bookperson = request.POST['bookperson']
        booktel = request.POST['booktel']
        bookdate = request.POST['bookdate']
        bookwhen = request.POST['bookwhen'] 
        booktime = time.strftime("%Y-%m-%d %H:%M", time.localtime()) 
        
        
        #todo 把資料寫進資料庫
        Booking.objects.create(restaurantname=restaurantname,bookname=bookname,bookperson=bookperson,booktel=booktel,bookdate=bookdate,bookwhen=bookwhen,booktime=booktime)
        return redirect('/book/')
        
    restaurants = Restaurant.objects.all()
    now = time.strftime("%Y-%m-%d", time.localtime()) 
    return render(request,'booking/create.html',locals())

def update(request, id):
    pass
    if request.method == "POST":
        #取得表單透過POST傳過來的資料
        restaurantname = request.POST['restaurantname']
        bookname = request.POST['bookname']
        bookperson = request.POST['bookperson']
        booktel = request.POST['booktel']
        bookdate = request.POST['bookdate']
        bookwhen = request.POST['bookwhen']     
        Booking.objects.update(restaurantname=restaurantname,bookname=bookname,bookperson=bookperson,booktel=booktel,bookdate=bookdate,bookwhen=bookwhen)
        return redirect('/book/')
#     #步驟一
    books = list(Booking.objects.filter(id=id).values())
    books = books[0]
    print(books)
#     Booking = Book()
#     data = Booking.single(id)
#     restaurants = restaurant()
    restaurants = Restaurant.objects.all()
#     now = time.strftime("%Y-%m-%d", time.localtime()) 
    return render(request,'booking/update.html',locals())
def delete(request, id):
    booking = Booking.objects.get(id=int(id))
    booking.delete()
    return redirect('/book/')