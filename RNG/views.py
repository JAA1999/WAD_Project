from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q

from RNG.models import Category, Game, Comment
from RNG.forms import CategoryForm, UserForm, GameForm, UserProfileForm, CommentForm

def visitor_cookie_handler(request):
	visits = int(request.COOKIES.get("visits","1"))
	last_visit_cookie=request.COOKIES.get("last_visit",str(datetime.now()))
	last_visit_time=datetime.strptime(last_visit_cookie[:-7], "%Y-%,-%d %H:%M:%S")
	if (datetime.now()-last_visit_time).days > 0:
		visits+=1
		request.session["last_visit"]=str(datetime.now())
	else:
		request.session["last_visit"]=last_visit_cookie
	request.session["visits"]=visits

def index(request):
    newGameList= Game.objects.order_by("-release_date")#newgames
    popGameList= Game.objects.order_by("rating")#popular games
    newGames= []
    popularGames= []
    for r in newGameList:
        print(r.name, r.release_date)
        
    for i in range(1,6):
        newGames.append(newGameList[i])
        popularGames.append(popGameList[i])
    
    context_dict={"newGames":newGames,
                  "popularGames": popularGames}
    return render(request, 'RNG/index.html', context=context_dict)

def about(request):
    context_dict={}
    return render(request, 'RNG/about.html', context=context_dict)

def signup(request):
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			
			profile = profile_form.save(commit=False)
			profile.user = user
			
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
				
			profile.save()
			
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
		
	return render(request,
				'RNG/signup.html',
				{'user_form': user_form,
				'profile_form': profile_form,
				'registered': registered})
				
def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)
		
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your RNG account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
			
	else:
		return render(request, 'RNG/signin.html', {})
		
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))
	
def show_categories(request):
	context_dict={}
	try:
		categorylist = []
		categorylist=Category.objects.order_by('name')
		context_dict['category']=categorylist
	except Category.DoesNotExist:
		context_dict['category']=None
	
	#if request.method=='POST':
		#query=request.POST['query'].strip()
		#if query:
			#result_list=run_query(query)
			#context_dict['query']=query
			#context_dict['result_list']=result_list
	return render(request, 'RNG/show_categories.html', context_dict)

def category(request, category_name_slug):
	context_dict={}
	try:
		category=Category.objects.get(slug=category_name_slug)
		games = Game.objects.filter(category=category, is_approved=True)
		context_dict['games']=games
		context_dict['category']=category
	except Category.DoesNotExist:
		context_dict['category']=None
		context_dict['games']=None
	#context_dict['query']=category.name
	#result_list=[]
	#if request.method=='POST':
		#query=request.POST['query'].strip()
		#if query:
			#result_list=run_query(query)
			#context_dict['query']=query
			#context_dict['result_list']=result_list
	return render(request, 'RNG/category.html', context_dict)
	
def gameV(request, category_name_slug, game_name_slug):

	game = Game.objects.get(slug=game_name_slug)
	comments = Comment.objects.filter(game=game).order_by('-timestamp')
				
	if request.method == 'POST':
		comment_form = CommentForm(request.POST or None)
		if comment_form.is_valid():
			content = request.POST.get('content')
			comment = Comment.objects.create(game=game, user=request.user, content=content)
			comment.save()
	else:
		comment_form = CommentForm()
		
	context_dict={'game':game, 
			'comments': comments,
			'comment_form': comment_form,}
			
	return render(request, 'RNG/game.html', context=context_dict)

def add_gameV(request):
	game_form = GameForm()
	if request.method == 'POST':
		game_form = GameForm(data=request.POST)
		
		if game_form.is_valid():
			game = game_form.save(commit=False)
			
			game.save()
			
			
			#if 'picture' in request.FILES:
				#profile.picture = request.FILES['picture']
				
			#profile.save()
			
			
		else:
			print(game_form.errors)
	else:
		game_form = GameForm()
		
			
			
	context_dict={'game_form':game_form}
	return render(request, "RNG/add_game.html", context_dict)

def search(request):
	if request.method == 'GET':
		game_name = request.GET.get('search')
		try:
			status = Game.objects.filter(name__icontains=game_name)
		except:
			return render(request, "wubba",{})
		return render(request, "RNG/search.html", {"games":status})
	else:
		return render(request, "RNG/search.html", {})

