
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == "POST":

        # Records all information needed for checks and user creation
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = None
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # Checks if username has already been taken
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken.")
            return redirect("home")

        # VALIDATION GOES HERE
        # Makes sure that all characters in username are only alphanumeric
        if not username.isalnum():
            messages.error(request, "Make sure your username only contains numbers and letters.")
            return redirect("home")
    


        # Makes a new user and assigns basic properties, then saves that information to the Django database
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()

        # Outputs success message and redirects user to the sign in page
        messages.success(request, "Your account has been successfully created!")

        return redirect('signin')




    return render(request, "authentication/signup.html")
    

def signin(request):


    if request.method == "POST":

        # Retrieves information from database
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')


        # Checks if the information entered is in the database
        user = authenticate(username=username, password=pass1)

        # If the user exists, log them in and show them to the main page
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})

        # Else, return them to the home page with an error
        else:
            messages.error(request, "Incorrect Username or Password")
            return redirect("home")




    return render(request, "authentication/signin.html")
    
def signout(request):

    # Logs out lol
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')