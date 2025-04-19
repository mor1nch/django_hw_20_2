from django.conf.urls.static import static
from django.urls import path

from catalog.views import product_list, product_detail, contact_us, main_menu
from skypro_online_store import settings

urlpatterns = [
    path('', main_menu, name='main_menu'),
    path('product/<int:product_id>', product_detail, name='product_detail'),
    path('contact_us/', contact_us, name='contact_us'),
    path('product_list/', product_list, name='product_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)