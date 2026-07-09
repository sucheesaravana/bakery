from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
import razorpay
from django.conf import settings
from django.shortcuts import render
from .forms import ContactForm, RegisterForm


def home(request):
    return render(request, 'bakeryapp/home.html')


def about(request):
    return render(request, 'bakeryapp/about.html')


def products(request):
    return render(request, 'bakeryapp/products.html')


def cake(request):
    return render(request, 'bakeryapp/cake.html')


def pastries(request):
    return render(request, 'bakeryapp/pastries.html')


def sweets(request):
    return render(request, 'bakeryapp/sweets.html')


def checkout(request):
    return render(request, 'bakeryapp/checkout.html')


def blog(request):
    return render(request, 'bakeryapp/blog.html')


def contact(request):
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()      # Save contact details
            success = True
            form = ContactForm()

    else:
        form = ContactForm()

    return render(
        request,
        "bakeryapp/contact.html",
        {
            "form": form,
            "success": success
        }
    )


def register(request):
    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )

            messages.success(request, "Registration Successful.")
            return redirect("login")

    else:
        form = RegisterForm()

    return render(
        request,
        "bakeryapp/register.html",
        {"form": form}
    )


def login_view(request):
    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            messages.error(request, "Invalid Email or Password")

    return render(request, "bakeryapp/login.html")

def payment(request):

    amount = int(request.GET.get("amount", 400))
    weight = request.GET.get("weight", "500 G")

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    order = client.order.create({
        "amount": amount * 100,
        "currency": "INR",
        "payment_capture": 1
    })

    context = {
        "amount": amount,
        "weight": weight,
        "order": order,
        "razorpay_key": settings.RAZORPAY_KEY_ID,
    }

    return render(request, "bakeryapp/payment.html", context)

def addtocard(request):
    return render(request, 'bakeryapp/addtocard.html')


def wishlist(request):
    return render(request, "bakeryapp/wishlist.html")