from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .modelsrestaurant import restaurant
# from . import modelsproduct
from .modelsbook import Book
import datetime
import time

# Create your views here.
def index(request):
    booking = Book()
    datas = booking.alls()

    return render(request,'booking/index.html',locals())

def create(request):
    if request.method == "POST":
        #取得表單透過POST傳過來的資料
        restaurantid = request.POST['restaurantid']
        bookname = request.POST['bookname']
        bookperson = request.POST['bookperson']
        booktel = request.POST['booktel']
        bookdate = request.POST['bookdate']
        bookwhen = request.POST['bookwhen'] 
        booktime = time.strftime("%Y-%m-%d %H:%M", time.localtime()) 
        
        
        #todo 把資料寫進資料庫
        booking = Book() 
        book = tuple([restaurantid,bookname,bookperson,booktel,bookdate,bookwhen,booktime])
        booking.create(book)
        return redirect('/booking/')
    booking = restaurant()
    datas = booking.all()
    # now = datetime.datetime.now() 
    now = time.strftime("%Y-%m-%d", time.localtime()) 
    return render(request,'booking/create.html',locals())

def update(request, id):
    if request.method == "POST":
        #取得表單透過POST傳過來的資料
        bookname = request.POST['bookname']
        bookperson = request.POST['bookperson']
        booktel = request.POST['booktel']
        bookdate = request.POST['bookdate']
        bookwhen = request.POST['bookwhen'] 
        bookid = request.POST['bookid']
        booking = Book() 
        data = tuple([bookname,bookperson,booktel,bookdate,bookwhen,bookid])
        booking.update(data)
        return redirect('/booking/')
    #步驟一
    Booking = Book()
    data = Booking.single(id)
    restaurants = restaurant()
    datas = restaurants.all()
    now = time.strftime("%Y-%m-%d", time.localtime()) 
    return render(request,'booking/update.html',locals())
def delete(request, id):
    # print(id)
    restaurant = Book() 
    restaurant.delete(id)
    return redirect('/booking/')