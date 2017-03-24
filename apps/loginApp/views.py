from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import User
import bcrypt
# Create your views here.
def index(request):
	return render(request, "loginApp/index.html")
	
def register(request):
	if not "hashes" in request.session:
		request.session["hashes"] = {}
	name = request.POST['name']
	username = request.POST['username']
	password = request.POST['password']
	confirm = request.POST['confirm']
	date = request.POST['date']
	check = User.objects.validation(name, username, password, confirm)
	if not check == "Success":
		for i in range(len(check)):
			messages.add_message(request, messages.INFO, check[i])
		return redirect(reverse('login:index'))
	try:
		temp = User.objects.get(username = username)
	except ObjectDoesNotExist:
		pass
	else:
		messages.add_message(request, messages.INFO, "Username already taken")
		return redirect(reverse('login:index'))
	password = password.encode(encoding = "utf-8")
	hashed = bcrypt.hashpw(password, bcrypt.gensalt())
	request.session["hashes"][password] = hashed
	request.session["name"] = name
	User.objects.create(name = name, username = username, password = hashed, date = date)
	query = User.objects.filter(username=username).filter(password=hashed)
	request.session["id"] = query[0].id
	return redirect(reverse('login:success'))
	
def login(request):
	username = request.POST['username']
	password = request.POST['password']
	password = password.encode(encoding = "utf-8")
	"""print "*"*80
	print password"""
	if not "hashes" in request.session:
		request.session["hashes"] = {}
	"""print "*"*80
	print request.session["hashes"]"""
	if not password in request.session["hashes"]:
		messages.add_message(request, messages.INFO, "Invalid Password")
		return redirect(reverse('login:index'))
	##print "*"*80
	hashed = bcrypt.hashpw(password, request.session["hashes"][password].encode(encoding = "utf-8"))
	query = User.objects.filter(username=username).filter(password=hashed)
	if len(query) < 1:
		messages.add_message(request, messages.INFO, "Invalid Credentials")
		return redirect(reverse('login:index'))
	request.session["name"] = query[0].name
	request.session["id"] = query[0].id
	return redirect(reverse('login:success'))
	

def success(request):
	return redirect(reverse('wishlist:index'))