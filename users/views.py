from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect

def Home(request):
    #if the user is authenticated, show the normal home page
    #with links to create and view tasks, as well as log out
    if request.user.is_authenticated:
        return render(request,'home.html')
    #if the user is not authenticated, show them a home page
    #with links to log in or create account
    return render(request,'home.html')

def CreateAccount(request):
    #if we recieved the user account creation data in the form,
    #create the user and show a screen indicate successful account
    #creation
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Home)
        else:
            return HttpResponse('Account Creation Failed')
    else:
        form = UserCreationForm()
        return render(request, 'create_account.html',{'form':form})

