from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
# Create your views here.
from app.forms import TODOForm
from app.models import TODO
#decorators allow us to add more functionality to the project.
from django.contrib.auth.decorators import login_required

#user can only go  to  homepage  if the user login .
#so  we  used  login required.
#if user is not logged in then login page will be shown..
@login_required(login_url='login')
def home(request):
    #the below 2 line code is written fr  getting the logged user
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        #here user=user for getting all the todos of only the logged in user 
        #filter is used when any  condition us used.
        todos = TODO.objects.filter(user = user).order_by('priority')
        return render(request , 'index.html' , context={'form' : form , 'todos' : todos})

def login(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form" : form1
        }
        return render(request , 'login.html' , context)
    else:
        
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            #for this we imported  login  as loginuser.. and cleaned data is a dictionary
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            #after alll the above three steps the user  is authenticated.
            #we use login methid for saving the object in session.after  the user is  authenticated..
            if user is not None:
                loginUser(request , user)
                return redirect('home')
        else:
            context = {
                "form" : form
            }
            return render(request , 'login.html' , context )


def signup(request):

    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request , 'signup.html' , context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)  
        context = {
            "form" : form
        }
        # if from is valid then we will save the form in user variable and then after successfully
        # creating the account if user is not none that maeans if user successfully created an
        # account then we will use not  none  and redirect login
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request , 'signup.html' , context)



@login_required(login_url='login')
def add_todo(request):
    #first it will check the user is authenticated and then the rquest willbe passed to the user
   #and then the user will be printed
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        #first iw will check the form is valid or not then it will print the data in the format of key value pair
        if form.is_valid():
            print(form.cleaned_data)
            #for printing todo first we will save the form and then todo.user for getting the user
            #and then saving the todo and printing it.
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else: 
            context={'form' : form}
            return render(request , 'index.html' , context)

# here we used id for getting the id  of the todo..
def delete_todo(request , id ):
    print(id)
    # here we will get the id and then delete the id..
    TODO.objects.get(pk = id).delete()
    return redirect('home')

def change_todo(request , id  , status): 
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')

# Forsignout we used logout function.
#first we will logout the logged user by using the logout(request)
def signout(request):
    logout(request)
    return redirect('login')