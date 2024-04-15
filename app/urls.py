from django.contrib import admin
from django.urls import path
from indexing_link import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexing_links, name='indexing_links'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)