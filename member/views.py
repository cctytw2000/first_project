from django.shortcuts import render,redirect
from .models import Member
from django.http import HttpResponse

# Create your views here.
def index(request):
    if 'name' in request.COOKIES:
        return render(request,'member/memberarea.html',locals())
    else:
        response = HttpResponse("<script>alert('請先登入喔!');location.href='/member/login'</script>")
        return response


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['userpassword']
   
        member = Member.objects.filter(username=username,password=pwd).values('username')
        if member:
            response = HttpResponse("<script>alert('登入成功');location.href='/restaurant'</script>")
            if 'rememberme' in request.POST:
                expiresdate = datetime.datetime.now() + datetime.timedelta(days=7)
                response.set_cookie("name",member[0]['username'],expires=expiresdate)
            else:
                response.set_cookie("name",member[0]['username'])
        else:
            response = HttpResponse("<script>alert('密碼錯誤');location.href='/member/login'</script>")
        return response
        
    title = "會員登入"
    return render(request,'member/login.html',locals())

def logout(request):
   response = HttpResponse("<script>alert('登出成功');location.href='/member/login'</script>")
   response.delete_cookie('name')
   return response

def create(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        useremail = request.POST["useremail"]
        userbirth = request.POST["userbirth"]

        #todo 接收到的會員資料寫進資料庫
        Member.objects.create(username=username,password=password,useremail=useremail,userbirth=userbirth)
        
        #todo 新增完成後轉到http://localhost:8000/member
        return redirect("/restaurant")
       
 
    return render(request,'member/create.html',locals())

def mybooking(request):
    if 'name' in request.COOKIES:
        name=request.COOKIES['name']
        # print(name)
        member = Member.objects.get(username=name)
        return render(request,'member/memberarea.html',locals())

    else:
        response = HttpResponse("<script>alert('請先登入喔!');location.href='/member/login'</script>")
        return response
        # return render(request,'member/memberarea.html',locals())


     