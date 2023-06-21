from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

def HomePage(request):
    return render(request, 'post/index.html')

def aboutPage(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post/about.html', context) 

def profilesPage(request):
    return render(request, 'post/profiles.html')

def aboutdetail(request, pk):
    post = get_object_or_404(Post,id=pk)
    comments = Comment.objects.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'post': post
    }
    return render(request, 'post/aboutdetail.html', context)


def profile1Page(request):
    return render(request, 'post/profile1.html')

def profile2Page(request):
    return render(request, 'post/profile2.html')


def newPostPage(request):

    if request.method == 'POST':
        
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():    
            form.save()
            return HttpResponseRedirect(redirect_to='/about/')
    else:
        form = PostForm()
    
    context = {
        'form': form
    }
    return render(request=request, template_name='post/newpost.html', context=context)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse(
                        'Вы успешно вошли на сайт'
                    )
                else:
                    return HttpResponse('Такого аккаунта не существует')
            else:
                return HttpResponse('Неверный пароль')
    else:
        form =LoginForm()

    context = {
        'form': form
    }   
    return render(request, 'registration/login.html', context)

@login_required   
def dashboard(request):
    context = {
        'section': dashboard
    }
    return render(request, 'registration/dashboard.html', context)

    
def register(request):
    if request.method == "POST":
        user_form = UserRegistration(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()

            Profile.objects.create(user=new_user) 

            context = {
                'new_user':new_user
            }
            return render(request, 'registration/register_done.html', context=context)
        
    else:
        user_form = UserRegistration()

    context = {
        'user_form': user_form
    }

    return render(request, 'registration/register.html', context)


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)

        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль успешно редактирован')
        else:
    
            messages.success(request, 'Ошибка при редактировании')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {

        'user_form': user_form,
        'profile_form': profile_form
        }
    return render(request, 'registration/edit.html', context)
