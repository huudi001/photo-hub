from django.contrib import admin
from .models import User,Post,tags
class PostAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(User)
admin.site.register(Post,PostAdmin)
admin.site.register(tags)
