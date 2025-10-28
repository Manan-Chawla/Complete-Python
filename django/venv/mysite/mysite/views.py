from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def home(request):
    data={
        'title':'HOME PAGE',
        'p':'This is just a text line to test the paragraph tag',
        'clist':['PHP','DJANGO','WORDPRESS'],
        'student':[
            {'name':'Max','age':'32'},
            {'name':'Emily','age':'30'}
        ],
        'number':[10,20,30,40,50]
    }
    return render(request,"index.html",data)

def pract(request):
    return render(request,"power.html")



def about(request):
    return render(request,"aboutus.html")


def service(request):
    return render(request,"service.html")

def contact(request):
    return render(request,"contactus.html")


def form(request):
    try:
        n=request.GET['name']
        a=request.GET['age']
        print(f"username : {n}") 
        print(f"age : {a}")
        
        return HttpResponseRedirect('/contact-us/')
    except:
        print("data is not fetched")
    return render(request,"form.html")



def postform(request):
    data = {}  

    if request.method == "POST":
        n = request.POST.get('name')
        a = request.POST.get('age')

        print(f"username : {n}")
        print(f"age : {a}")
        data = {
            'names': [n],
            'ages': [a]
        }

    return render(request, "postform.html", data)


# def aboutUS(request):
#     return HttpResponse("Welcome to our demo site")

# def projects(request):
#     return HttpResponse("welcome to our project pages")

# def projectdetail(request,projectid):
#     return HttpResponse("Project config")

# def projectdetail2(request,projectid):
#     return HttpResponse(projectid)

# def projectdetail3(request,projectid):
#     return HttpResponse(projectid)

# def powerranger(request):
#     return render(request,"power.html")


# def contactus(request):
#     return HttpResponse("Welcome to our contact us page")