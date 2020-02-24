from django.shortcuts import render,redirect,get_object_or_404
from .models import User,Contact,Event,Book_Event
from django.core.mail import send_mail
import random
from django.conf import settings
from . forms import ContactForm 
# Create your views here.
def index(request):
	return render(request,'myapp/index.html')
def sports(request):
	sports=Event.objects.filter(event_category="Sports")
	return render(request,'myapp/sports.html',{'sports':sports})
def concerts(request):
	concerts=Event.objects.filter(event_category="Concerts")
	return render(request,'myapp/concerts.html',{'concerts':concerts})
def political(request):
	politicals=Event.objects.filter(event_category="Political")
	return render(request,'myapp/political.html',{'politicals':politicals})
def contact(request):
	try:
		user=get_object_or_404(User,pk=request.session['userpk'])
		contacts=Contact.objects.all()
		return render(request,'myapp/contact.html',{'user':user,'contacts':contacts})
	except:
		contacts=Contact.objects.all()
		return render(request,'myapp/contact.html',{'contacts':contacts})
def signup(request):
	return render(request,'myapp/signup.html')
def login(request):
	return render(request,'myapp/login.html')
def signup_user(request):
	u=User()
	print("Signup User Called")
	u.fname=request.POST['fname']
	u.lname=request.POST['lname']
	u.email=request.POST['email']
	u.mobile=request.POST['mobile']
	password=request.POST['password']
	cpassword=request.POST['cpassword']
	#u.save()
	
	try:
		user=User.objects.get(email=u.email)
		if user:
			error="This email is ia already used."
			return render(request,'myapp/signup.html',{'error':error,'u':u})
	except:
		if password==cpassword:
			User.objects.create(fname=u.fname,lname=u.lname,email=u.email,mobile=u.mobile,password=password,cpassword=cpassword)
			rec=[u.email,]
			subject="OTP"
			otp=random.randint(1000,9999)
			message="YOUR OTP FOR REGISTRATION IS "+str(otp)
			email_from=settings.EMAIL_HOST_USER
			send_mail(subject,message,email_from,rec)
			return render(request,'myapp/otp.html',{'otp':otp,'email':u.email})
		else:
			error="Password and Confirm Password Does Not Match"
			return render(request,'myapp/signup.html',{'error':error})
def login_user(request):
	u=User()
	u.email=request.POST['email']
	password=request.POST['password']
	
	try:
		user=User.objects.get(email=u.email,password=password)
		pk=user.pk
		if user.status=="active":
			request.session['userpk']=user.pk
			request.session['fname']=user.fname
			return render(request,"myapp/index.html")
		else:
			print("Hello Else")
			error1="Your Status Is Still Not Active."
			return render(request,"myapp/login.html",{'error1':error1,'pk':pk,'u':u})
	except:
		print("Hello Except")
		error="Email or Password Is Incorrect Or Status Is Inactive"
		return render(request,'myapp/login.html',{'error':error,'u':u})
def logout(request):
	try:
		del request.session['userpk']
		del request.session['fname']
		return render(request,'myapp/login.html')
	except:
		pass
def validate_otp(request):
	otp=request.POST['otp']
	email=request.POST['email']
	u_otp=request.POST['u_otp']
	user=User.objects.get(email=email)
	if otp==u_otp:
		user.status="active"
		user.save()
		return render(request,'myapp/login.html')
def submit_contact(request):
	Contact.objects.create(
		name=request.POST['name'],
		email=request.POST['email'],
		mobile=request.POST['mobile'],
		remarks=request.POST['remarks'])
	return redirect('contact')

def resend_otp(request,pk):
	user=get_object_or_404(User,pk=pk)
	rec=[user.email,]
	subject="OTP"
	otp=random.randint(1000,9999)
	message="YOUR OTP FOR ACTIVATING ACCOUNT IS "+str(otp)
	email_from=settings.EMAIL_HOST_USER
	send_mail(subject,message,email_from,rec)
	return render(request,'myapp/otp.html',{'otp':otp,'email':user.email})

def event_detail(request,pk):
	event=get_object_or_404(Event,pk=pk)
	return render(request,'myapp/event_detail.html',{'event':event})

def book_event(request,pk1,pk2):
	user=get_object_or_404(User,pk=pk1)
	event=get_object_or_404(Event,pk=pk2)
	Book_Event.objects.create(user=user,event=event)
	return render(request,'myapp/index.html')

def myevent(request,pk):
	user=get_object_or_404(User,pk=pk)
	be=Book_Event.objects.filter(user=user)
	return render(request,'myapp/myevent.html',{'be':be})

def cancel_event(request,pk):
	be=get_object_or_404(Book_Event,pk=pk)
	be.delete()
	user=get_object_or_404(User,pk=request.session['userpk'])
	be=Book_Event.objects.filter(user=user)
	return render(request,'myapp/myevent.html',{'be':be})
