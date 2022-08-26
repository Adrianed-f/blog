from django.conf import settings
from django.contrib import admin
from django.urls import path

from posts.views import index as posts_index
from profiles.views import index as profiles_index

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', posts_index, name='posts_index'),
]

if settings.DEBUG:
   from django.conf.urls.static import static
   from django.contrib.staticfiles.urls import staticfiles_urlpatterns

   # Serve static and media files from development server
   urlpatterns += staticfiles_urlpatterns()
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)