from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import Item
from ..loginApp.models import User
# Create your views here.

def index(request):
	user = User.objects.get(id = request.session['id'])
	list = Item.objects.filter(wishes = user).order_by('created_at')
	other = Item.objects.exclude(wishes = user).order_by('created_at')
	context = {
		"list": list,
		"user": user,
		"other": other
	}
	return render(request, "wishList/index.html", context)
	"""print "*"*80
	print reverse('secrets:delete', kwargs={'id': post.id})"""

def delete(request, id):
	Item.objects.get(id=id).delete()
	return redirect (reverse('wishlist:index'))

def add(request, id):
	new = Item.objects.get(id = id)
	user = User.objects.get(id = request.session['id'])
	user.items.add(new)
	return redirect(reverse('wishlist:index'))

def remove(request, id):
	new = Item.objects.get(id = id)
	user = User.objects.get(id = request.session['id'])
	user.items.remove(new)
	return redirect(reverse('wishlist:index'))

def create(request):
	if request.method == "POST":
		name = request.POST["name"]
		poster = User.objects.get(id = request.session['id'])
		check = Item.objects.validation(name)
		if not check == "Success":
			for i in range(len(check)):
				messages.add_message(request, messages.INFO, check[i])
			return redirect(reverse('wishlist:create'))
		Item.objects.create(name=name, creator = poster)
		new = Item.objects.get(name = name)
		poster.items.add(new)
		return redirect(reverse('wishlist:index'))
	return render(request, "wishList/create.html")
	
def show(request, id):
	item = Item.objects.get(id = id)
	users = User.objects.filter(items = item)
	context = {
		"item": item,
		"users": users
	}
	return render(request, "wishList/item.html", context)

def logout(request):
	del request.session['name']
	del request.session['id']
	return redirect(reverse('login:index'))