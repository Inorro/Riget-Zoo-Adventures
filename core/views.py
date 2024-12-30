from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 
from .models import Hotelbook,Tickbooking
from .forms import UserForm,LoginForm
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

def index(request):
    context = {}

    if request.method == "POST":
        if "Sign_UP" in request.POST:
            form = UserForm(request.POST,request.FILES)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                if form.cleaned_data['conpass'] != form.cleaned_data['password']:
                    messages.success(request,"Passwords dont match")
                    return redirect("index")

                messages.success(request,"You have created an Account")
                user = form.save(commit=False)
                
                user.set_password(form.cleaned_data['password'])
                user.save()
            elif form.errors:
                messages.error(request,"Account already exists")
            return redirect("index")
        
        if "Log_IN" in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                # process the data in form.cleaned_data as required
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                print(email,password)
                user = authenticate(email=email,password=password)
                print(user)
                if user is not None:
                    login(request,user)
                    name = request.user.name
                    print(name)
                    messages.success(request,"You are logged in")
                    return redirect('index')
                else:
                    messages.error(request,"Wrong credentials")
                    return redirect('/')
        
    context = {
        'Uform' : UserForm(),
        'Lform' : LoginForm()
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def hotel(request):
    return render(request,"hotel.html")

def hotelpricecalc(suite):
    if suite == "suite1":
        return 68.99
    elif suite == "suite2":
        return 95.99
    elif suite == "suite3":
        return 74.99
    elif suite == "suite4":
        return 88.99

def hotelpt1(request):
    if request.method == "POST":
        if "hotel" in request.POST:
            suite = request.POST.get("suite")
            numrooms = request.POST.get("rooms")
            checkin = request.POST.get("checkin")
            checkout = request.POST.get("checkout")
            people = request.POST.get("people")
            if request.user.is_authenticated:
                email = request.user.get_username()
            else:
                email = request.POST.get("email1")
            date_format = '%Y-%m-%d'

            checkincalc = datetime.strptime(checkin, date_format)
            checkoutcalc = datetime.strptime(checkout, date_format)
            checkincalc=checkincalc.date()
            checkoutcalc=checkoutcalc.date()
            delta = checkoutcalc - checkincalc
            present = datetime.now()
            if delta.days <=0:
                messages.error(request,"You have entered invalid dates")
                return render(request,"hotelpt1.html")
            elif checkincalc < present.date():
                messages.error(request,"You have entered unavailable dates")
                return render(request,"hotelpt1.html")
            

            # If user booking has the same room type,check in 
            # and check out date as more than two previously stored 
            # bookings it will reject the booking on the basis of lack of vacancies

            if Hotelbook.objects.filter(checkin=checkin).count() > 2 and Hotelbook.objects.filter(checkout=checkout).count() > 2 and Hotelbook.objects.filter(suite=suite).count():
                messages.error(request,"Room already booked")
                return render(request,"hotelpt1.html")

            price = (hotelpricecalc(suite) * delta.days) * int(numrooms)

            booking = Hotelbook(suite=suite,numrooms=numrooms,checkin=checkin,checkout=checkout,people=people,email=email,price=price)

            booking.save()
            if request.user.is_authenticated:
                request.user.points += 200
                request.user.save()

            messages.success(request,"You have booked a hotel!")

            return render(request,"hotelpt1.html")
    
    return render(request,"hotelpt1.html")


def tickets(request):
    return render(request,"ticketing.html")

def ticketpt1(request):
    if request.method == "POST":
        check1 = request.POST.get("check1") == "True"
        check2 = request.POST.get("check2") == "True"
        check3 = request.POST.get("check3") == "True"
        check4 = request.POST.get("check4") == "True"
        num1 = request.POST.get("number1")
        num2 = request.POST.get("number2")
        num3 = request.POST.get("number3")
        num4 = request.POST.get("number4")
        tickdate = request.POST.get("tickdate")
        if request.user.is_authenticated:
            tickemail = request.user.get_username()
        else:
            tickemail = request.POST.get("tickemail")
        price = (int(num1) * 11.99) + (int(num2) * 14.99) + (int(num3) * 10.99) + (int(num4) * 12.99)

        date_format = '%Y-%m-%d'
        present = datetime.now()
        date = datetime.strptime(tickdate, date_format)
        # If user ticket has the same date as more than 100 previously stored 
        # tickets it will reject the booking on the basis of hitting max capacity

        if Tickbooking.objects.filter(date=tickdate).count() >= 99:
                messages.error(request,"Zoo visits are expecated to be at max capacity for that date")
                return render(request,"ticketfirstpt.html")
        elif date.date() < present.date():
                messages.error(request,"You have entered unavailable dates")
                return render(request,"ticketfirstpt.html")

        booking = Tickbooking(ticket1 = check1,ticket2 = check2,ticket3 = check3,ticket4 = check4,ticket1num=num1
                              ,ticket2num=num2,ticket3num=num3,ticket4num=num4,date=tickdate,email=tickemail,price=price)

        booking.save()
        if request.user.is_authenticated:
            request.user.points += 100
            request.user.save()

        messages.success(request,"You have booked a ticket!")

        return render(request,"ticketfirstpt.html")

    return render(request,"ticketfirstpt.html")

def loyalty(request):
    return render(request,"loyalty.html")

def SignOut(request):
    logout(request)
    return redirect("/")

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    pass