from django.shortcuts import render
import datetime as dt
from .models import Post

def trending_pics(request):
    date = dt.date.today()
    photos = Post.todays_photos()
    return render(request, 'all_pics/trending_pics.html', {"date": date,"photos":photos})
def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_tag(search_term)
        message = f"{search_term}"

        return render(request, 'all_pics/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_pics/search.html',{"message":message})

def post(request,post_id):
    try:
        post = Article.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all_pics/post.html", {"post":post})
