from .models import Article
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponse


def archive(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            logout(request)
            return redirect("archive")
        else:
            username = request.user.username
            return render(request, 'archive_auth.html', {"posts": Article.objects.all(), "user": username})
    else:
        return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            logout(request)
            return redirect("archive")
        else:
            try:
                post = Article.objects.get(id=article_id)
                username = request.user.username
                return render(request, 'article_auth.html', {"post": post, "user": username})
            except Article.DoesNotExist:
                raise Http404
    else:
        try:
            post = Article.objects.get(id=article_id)
            return render(request, 'article.html', {"post": post})
        except Article.DoesNotExist:
            raise Http404


def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = u"Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
                new_article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=new_article.id)
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404


def create_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"], 'mail': request.POST["mail"], 'password': request.POST["password"]
        }
        u = 0
        m = 0
        try:
            User.objects.get(username=form["username"])
            u = 1
        except:
            pass  # this user not found
        try:
            User.objects.get(email=form["mail"])
            m = 1
        except:
            pass  # this user not found
        if form["username"] and form["mail"] and form["password"] and u == 0 and m == 0:
            User.objects.create_user(form["username"], form["mail"], form["password"])
            return redirect("archive")
        else:
            if u != 0 and m != 0:
                form['errors'] = u"Логин и почта уже используется"
            elif u != 0:
                form['errors'] = u"Данный логин занят"
            elif m != 0:
                form['errors'] = u"Данная почта используется"
            else:
                form['errors'] = u"Не все поля заполнены"
            return render(request, "registration.html", {'form': form})
    else:
        return render(request, 'registration.html', {})


def login_for_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"], 'password': request.POST["password"]
        }
        if form["username"] and form["password"]:
            user = authenticate(request, username=form["username"], password=form["password"])
            if user != None:
                login(request, user)
                return redirect("archive")
            else:
                form['errors'] = u"Такого пользователья не существует"
                return render(request, "login.html", {'form': form})
        else:
            form['errors'] = u"Не все поля заполнены"
            return render(request, "login.html", {'form': form})
    else:
        return render(request, 'login.html', {})
