from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from . import modelsrestaurants
# from . import modelsproduct
from .modelsrestaurant import restaurant

# Create your views here.
def index(request):
    title="餐廳管理"
    # product = modelsproduct.Product()
    res = restaurant()
    datas = res.all()
    return render(request,'R20/index.html',locals())

def create(request):
    title="餐廳新增"
    # print(request.method);
    #POST
    if request.method == "POST":
        #取得表單透過POST傳過來的資料
        rtype = request.POST['rtype']
        rname = request.POST['rname']
        rtel = request.POST['rtel']
        raddress = request.POST['raddress']
        rweb = request.POST['rweb']
        rintroduction = request.POST['rintroduction']

        #todo 把資料寫進資料庫
        res = restaurant() 
        data = tuple([rname,rtype,rtel,raddress,rweb,rintroduction])
        res.create(data)
       
        return redirect('/restaurant/')
        
    #GET
    #回傳一個網頁，讓使用者可以輸入資料
    category = modelsrestaurants.restaurants()
    datas = category.all()
    # print(datas)  #((),(),())
    return render(request,'R20/create.html',locals())
def beforeupdate(request):
    title="餐廳管理"
    # product = modelsproduct.Product()
    res = restaurant()
    datas = res.all()
    return render(request,'R20/beforeupdate.html',locals())

def update(request, id):
    #步驟二
    if request.method == "POST":
        # #上傳檔案
        # myFile = request.FILES["ProductImage"]
        # fs = FileSystemStorage()
        # fs.save(myFile.name, myFile)
        
        #取得表單透過POST傳過來的資料
        rtype = request.POST['rtype']
        rname = request.POST['rname']
        raddress = request.POST['raddress']
        rweb = request.POST['rweb']
        rtel = request.POST['rtel']
        rintroduction = request.POST['rintroduction']
        # ProductImage = myFile.name
        restaurantsid = request.POST['restaurantsid']

        res = restaurant() #modelsproduct.Product()
        data = tuple([rname,rtype,rtel,raddress,rweb,rintroduction,restaurantsid])
        res.update(data)
        return redirect('/restaurant/')

    title="餐廳修改"
    #步驟一
    res = restaurant()
    data = res.single(id)
    category = modelsrestaurants.restaurants()
    datas = category.all()
    return render(request,'R20/update.html',locals())

def delete(request, id):
    # print(id)
    res = restaurant() #modelsproduct.Product()
    res.delete(id)
    return redirect('/restaurant/beforeupdate')