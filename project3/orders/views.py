from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import UserDetail, Menu, ItemSize


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        context = {"message": None}
        return render(request, "orders/login.html", context)
    return HttpResponseRedirect(reverse("menu"))


def menu(request):
    menu_items = Menu.objects.all()
    sizes = ItemSize.objects.all()
    menu = []
    for item in menu_items:
        for size in sizes:
            new_menu_item = {}
            new_menu_item["size"] = size.size
            new_menu_item["item"] = item.item
            new_menu_item["price"] = item.base_price * size.pct_of_price / 100
            menu.append(new_menu_item)
    context = {"user": request.user, "menu": menu}
    return render(request, "orders/menu.html", context)


def register(request):
    context = {"message": None}
    return render(request, "orders/register.html", context)


def register_user(request):
    try:
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
    except KeyError:
        context = {"message": "username, email, or password missing"}
        return render(request, "orders/error.html", context)
    # TODO Check if user already exists
    if User.objects.filter(username=username).exists():
        context = {"message": "User Already exists"}
        return render(request, "orders/register.html", context)
    else:
        # Add User
        user = User.objects.create_user(username, email, password)
        user_detail = UserDetail(user=user)
        user_detail.save()
        context = {"message": "User Created, please login"}
        return render(request, "orders/login.html", context)


def login_view(request):
    try:
        username = request.POST["username"]
        password = request.POST["password"]
    except KeyError:
        context = {"message": "username or password missing"}
        return render(request, "orders/error.html", context)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        context = {"message": "Invalid Username or Password"}
        return render(request, "orders/login.html", context)


def logout_view(request):
    logout(request)
    context = {"message": "Logged Out"}
    return render(request, "orders/login.html", context)


def user_detail(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    user = request.user
    if UserDetail.objects.filter(user_id=user.id).exists():
        user_detail = UserDetail.objects.get(user_id=user.id)
    else:
        context = {"message": "No Details for for User"}
        return render(request, "orders/error.html", context)

    context = {
        "data": {
            "address": user_detail.address,
            "city": user_detail.city,
            "province": user_detail.province,
            "country": user_detail.country,
        }
    }
    return render(request, "orders/edituser.html", context)


def update_user(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    try:
        address = request.POST["address"]
        city = request.POST["city"]
        province = request.POST["province"]
        country = request.POST["country"]
    except KeyError:
        context = {"message": "Invalid Entry"}
        return render(request, "orders/error.html", context)
    user = request.user
    user_detail = UserDetail.objects.get(user_id=user.id)
    user_detail.address = address
    user_detail.city = city
    user_detail.province = province
    user_detail.country = country
    user_detail.save()
    return HttpResponseRedirect(reverse("user_detail"))
