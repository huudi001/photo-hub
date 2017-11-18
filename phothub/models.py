from django.db import models
import datetime as dt

class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length =60)
    user = models.ForeignKey(User)
    description = models.CharField(max_length = 255)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'posts/')


    @classmethod
    def search_by_tag(cls,search_term):
        pics = cls.objects.filter(tags__icontains=search_term)
        return pics

    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        photos= cls.objects.filter(pub_date__date = today)
        return photos
