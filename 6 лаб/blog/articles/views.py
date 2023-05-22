from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User


def archive(request):
    if request.user.is_authenticated:
        if request.method == "POST": # нажатие по кнопке
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
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                # если поля заполнены без ошибок
                if Article.objects.filter(title=form["title"]).exists():
                    return render(request, "create_post.html", {'form':form})
                article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=article.id)
            # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})

    else:
        raise Http404


def create_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"], 'mail': request.POST["mail"], 'password': request.POST["password"]
        }
        u = False
        try:
            User.objects.get(username=form["username"])
            u = True
        except:
            pass
        if form["username"] and form["mail"] and form["password"] and not u:
            User.objects.create_user(form["username"], form["mail"], form["password"])
            return redirect("archive")
        else:
            if u:
                form['errors'] = u"Логин уже используется"
            else:
                form['errors'] = u"Не все поля заполнены"
            return render(request, "registration.html", {'form': form})
    else:
        return render(request, 'registration.html', {})

def User_login(request):
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
