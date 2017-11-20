from django.shortcuts import render,redirect
import datetime as dt
from .models import Post

def trending_pics(request):
    date = dt.date.today()
    posts = Post.todays_posts()
    return render(request, 'all_pics/trending_pics.html', {"date": date,"posts":posts })

def past_days_posts(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(trending_pics)

    posts = Post.days_posts(date)
    return render(request, 'all_pics/past_days_posts.html',{"date": date,"posts":posts})
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
        post = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all_pics/post.html", {"post":post})
