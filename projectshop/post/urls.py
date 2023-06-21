from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Основной url
    path('',views.HomePage, name='home'),
    path('about/', views.aboutPage, name='about'),
    path('profiles/', views.profilesPage, name='profiles'),
    path('about/<int:pk>/', views.aboutdetail, name='aboutdetail'),
    path('profile1/', views.profile1Page, name='profile1'),
    path('profile2/', views.profile2Page, name='profile2'),
    path('new/', view=views.newPostPage, name='newpage'),

    # url для регистрации
    path('login/',  auth_views.LoginView.as_view(),  name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Доска обьявлении
    path('dashboard/', views.dashboard, name='dashboard'),

    # Смена пароля
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    # Сброс пароля
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uid64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Регистрация
    path('register/', views.register, name='register' ),

    # Редактирования
    path('edit/', views.edit, name='edit'),
]

