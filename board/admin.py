from django.contrib import admin
from .models import Post,Reply,Author
# Register your models here.
admin.site.register(Post)
#admin.site.register(Category)
#admin.site.register(PostCategory)
admin.site.register(Reply)
admin.site.register(Author)