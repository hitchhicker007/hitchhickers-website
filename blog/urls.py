from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from posts.views import index,post,postlist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('postlist/', postlist,name='post-list'),
    path('',index,name='index'),
    path('post/<id>/',post,name='post-detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
