from django.contrib import admin
from django.urls import path
from mycare_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.Product_list),
    path('products/<int:id>', views.Product_rud),
]
