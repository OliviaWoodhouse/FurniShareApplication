from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from .models import *
from operator import attrgetter



@login_required
def add_item(request):
	context={}
	if request.method=='POST':
		form=ItemForm(request.POST,request.FILES)
		if form.is_valid():
			item=form.save(commit=False)
			item.seller= request.user.userprofile
			item.save()
			return redirect('my_items')
		
	else:
		form=ItemForm()
		context['form']=form
	return render(request,'items/add_item.html',context)

@login_required
def my_items(request):
	context={}
	
	myprofile= request.user.userprofile
	items = Item.objects.filter(seller=myprofile)
	context['items']=items
	return render(request,'items/my_items.html',context)

# Return all listed items for news feed. Sorting/Filtering should be handled on front end.
def all_items(request):
	context={}
	items = sorted(Item.objects.all(), key=attrgetter('post_date'), reverse=True)
	context['item_listings'] = items

	return render(request, 'items/listings.html', context)

