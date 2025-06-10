from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:book_id>/edit/', views.book_update, name='book_update'),
    path('books/<int:book_id>/delete/', views.book_delete, name='book_delete'),
    path('register/', views.register_view, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('rent/<int:book_id>/', views.rent_book, name='rent_book'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)