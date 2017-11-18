from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url(r'^$',views.trending_pics,name='photosToday'),
     url(r'^search/', views.search_results, name='search_results'),
     url(r'^post/(\d+)',views.post,name ='post')


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
