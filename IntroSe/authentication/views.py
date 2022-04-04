from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

# Checks if a string has any of the special characters
def is_special_character(password):
    special_char = "!@#$%^&*-_./"
    if any(password in special_char for password in special_char):
        return True
    return False


# Signup page
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
        
        # Makes sure the password falls under specified character conditions
        if (not is_special_character(pass1)) or len(pass1) <= 8:
            messages.error(request, "Your password must include at least one of the following: \"! @ # $ % ^ & * - _ . /\" You must also include at least 8 characters.")
            return redirect("home")

        # Makes sure the user's name only has alphabetical letters
        if (not firstname.isalpha()) or (not lastname.isalpha()):
            messages.error(request, "Your first and last name must only include the letters a-z.")
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
    messages.success(request, "Logged out successfully")
    return redirect('home')

def del_auth(request):
    # Returns user to confirmation page to make sure they didn't missclick
    return render(request, "authentication/confirm.html")


def del_user(request):

    # Deletes user from Django database
    u = request.user
    u.delete()
    messages.success(request, "You have successfully deleted your account!")
    return redirect("home")