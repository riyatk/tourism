from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),
    path('create/', views.create_package, name='create_package'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/<int:pk>/', views.edit_package, name='edit_package'),
    path('delete/<int:pk>/', views.delete_package, name='delete_package'),
    path('pay/', views.payment, name='payment_page'),



]
