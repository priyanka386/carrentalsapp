
from django.contrib import admin
from django.urls import path , include
from .import views
from .import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name=('homepage')),
    path('accounts/',include('allauth.urls')),
    path('product/', include('mycart.urls')),
    path('order_details/', views.order_details),
    path('my_order_list/', views.my_order_list , name='my_order_list'),
    path('show_cart_items/', views.show_cart_items, name='show_cart_items'),
    path('add_to_cart/',views.add_to_cart),
    path('remove_from_cart/', views.remove_from_cart),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
