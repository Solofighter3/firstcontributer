from django.shortcuts import render,redirect
from list.models import Tasks
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from  django.db.models import Q
from django.contrib.auth.models import User
def index(request):
    context={'name':request.user.username}
    if request.method=='POST':
        task_name=request.POST.get("task")
        desc=request.POST.get("desc")
        task=Tasks(user=request.user,task_name=task_name,desc=desc)
        task.save()
        messages.success(request, "Profile details updated.")

    return render(request,"index.html",context)

def Login(request):
    if request.user.is_authenticated:
     return redirect("index")

    if request.method=="POST":
       username = request.POST.get("username")
       password = request.POST.get("password")
       user = authenticate(request, username=username, password=password)
       if user is not None:
          login(request, user)
          return redirect("index")
       else:
          return redirect("Login")
    return render(request,"login.html")

def Logout(request):
    logout(request)
    return redirect("Login")

def about(request):
  if request.user.is_authenticated:
     if "q" in request.GET:
         q=request.GET["q"]
         milti_qurrey=Q(Q(task_name=q)|Q(desc=q))
         alltasks=Tasks.objects.filter(milti_qurrey)
     else:
       user=request.user
       alltasks=Tasks.objects.filter(user=user)
     context={"tasks":alltasks}
     return render(request,"about.html",context)

def Signup(request):
  if request.method=="POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      password1 = request.POST.get("password1")
      email = request.POST.get("email")
      if User.objects.filter(username = username).first():
         messages.error(request, "This username is already taken please chose diffrent username")
      else:
        user = User.objects.create_user(username, email, password1)
        authenticate(request, username=username, password=password1)
        user.save()
        return redirect("index")



  return render(request,"signup.html")

def delete_todo(request,id):
       Tasks.objects.get(pk=id).delete()
       return redirect("about")

def update_todo(request,id):
    task_ch=Tasks.objects.get(pk=id)
    context={"taskn":task_ch.task_name,"task_dec":task_ch.desc,"task":task_ch}
    if request.method=='POST':
        task_name=request.POST.get("task")
        desc=request.POST.get("desc")
        task_ch.task_name=task_name
        task_ch.desc=desc
        task_ch.save()
        messages.success(request, "Profile details updated.")
        return redirect("index")
            
    return render(request,"update.html",context)
    
