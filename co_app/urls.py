
from django.contrib import admin
from django.urls import path
from co_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about,name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('testimonials/', views.testimonials, name='testimonials'),
]
