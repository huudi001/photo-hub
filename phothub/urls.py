from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url(r'^$',views.trending_pics,name='photosToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^post/(\d+)',views.single_post,name = 'post'),
    url( r'^tag/(\d+)', views.tag, name="tag"),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_posts,name = 'pastPosts')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
