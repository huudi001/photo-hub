from django.shortcuts import render
import datetime as dt
from .models import Post,tags,User

def trending_pics(request):
    date = dt.date.today()
    posts = Post.todays_posts()
    all_posts = Post.display_post()
    return render(request, 'all_pics/trending_pics.html', {"date": date,"posts":posts,"all_posts": all_posts })
def search_results(request):

    if 'tag' in request.GET and request.GET["tag"]:
        search_term = request.GET.get("tag")
        searched_posts = Post.search_by_tag(search_term)
        message = f"{search_term}"

        return render(request, 'all_pics/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_pics/search.html',{"message":message})

def post(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all_pics/post.html", {"post":post})
