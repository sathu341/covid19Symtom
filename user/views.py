from django.shortcuts import render
from . models import User_table
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def user_reg(request):
    if request.method=="POST":
        nam=request.POST.get("name")
        eml=request.POST.get("email")
        cnum=request.POST.get("contact_number")
        gen=request.POST.get("Gender")
        pword=request.POST.get("password")
        usernam=request.POST.get("username")
        obj=User_table.objects.create(nam=nam,eml=eml,cnum=cnum,gen=gen,password=pword,uname=usernam)
        obj.save()
        return HttpResponse("<h4> Successfully registered</h4> <a href='/register'>Login </a>  ")
    return render(request,'registration.html')
def login(request):
    if request.method=="POST":
        user=request.POST.get('user')
        passw=request.POST.get('passw')
        obj=User_table.objects.filter(uname=user,password=passw)#select * from tbl  where username
        
        if obj:
            for l in obj:
                idn=l.id
            request.session['dusername']=user
            request.session['dpassword']=passw
            request.session['didno']=idn
            return render(request,'index.html')  
        else:
            return render(request,'index.html',{'msg':"invalid username and password"})  


    return render(request,'index.html')   