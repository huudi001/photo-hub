from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Post, tags, User

def trending_pics(request):
    date = dt.date.today()
    tag = tags.get_tags()
    posts = Post.todays_posts()
    return render(request, 'all_pics/trending_pics.html', {"date": date,"posts":posts, "tag":tag})

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

    if 'tag' in request.GET and request.GET["tag"]:
        search_term = request.GET.get("tag")
        searched_tags = tags.search_by_tag(search_term)
        single_tag = searched_tags[0]
        post = Post.objects.filter(tags=single_tag).all()
        message = f"{search_term}"

        return render(request, 'all_pics/search.html',{"title": title, "message":message, "post":post, "tags":searched_tags})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_pics/search.html',{"message":message})

def single_post(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all_pics/post.html", {"post":post})
def tag(request,tag_id):
    all_tags = tags.get_tags()
    try:
        tag = tags.objects.get(id=tag_id)
        posts = Post.objects.filter(tags=tag).all()
    except DoesNotExist:
        raise Http404()
    title = f'{tag.name}'
    return render(request, 'all_pics/tag.html', {"title":title, "all_tags":all_tags, "posts":posts, "tag":tag})
