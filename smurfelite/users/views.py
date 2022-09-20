from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate

from .models import User
from .forms import RegisterForm


def user_login(request):

    if not request.user.is_authenticated:
        # if this is a POST request we need to process the form data
        template = "users/login.html"

        if request.method == "POST":
            # Process the request if posted data are available
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Check username and password combination if correct
            user = authenticate(username=username, password=password)

            if user is not None:
                # Save session as cookie to login the user
                login(request, user)
                # Success, now let's login the user.
                return redirect("user:profile")
            else:
                # Incorrect credentials, let's throw an error to the screen.
                return render(
                    request,
                    "users/login.html",
                    {"error_message": "Incorrect username or password."},
                )
        else:
            # No post data availabe, let's just show the page to the user.
            return render(request, "users/login.html")
    else:
        return redirect("order:home")


def logout_user(request):
    logout(request)
    return redirect("user:login")


def user_register(request):

    if not request.user.is_authenticated:
        # if this is a POST request we need to process the form data
        template = "users/register.html"

        if request.method == "POST":
            # create a form instance and populate it with data from the request:
            form = RegisterForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                if User.objects.filter(username=form.cleaned_data["username"]).exists():
                    return render(
                        request,
                        template,
                        {"form": form, "error_message": "Username already exists."},
                    )
                elif User.objects.filter(email=form.cleaned_data["email"]).exists():
                    return render(
                        request,
                        template,
                        {"form": form, "error_message": "Email already exists."},
                    )
                elif form.cleaned_data["password"] != form.cleaned_data["password_repeat"]:
                    return render(
                        request,
                        template,
                        {"form": form, "error_message": "Passwords do not match."},
                    )
                else:
                    # Create the user:
                    user = User.objects.create_user(
                        form.cleaned_data["username"],
                        form.cleaned_data["email"],
                        form.cleaned_data["password"],
                    )
                    user.save()

                    # Login the user
                    login(request, user)

                    # redirect to accounts page:
                    return redirect("user:profile")

        # No post data availabe, let's just show the page.
        else:
            form = RegisterForm()

        return render(request, template, {"form": form})
    else:
        return redirect("order:home")


def profile(request):
    return render(request, "users/profile.html")
