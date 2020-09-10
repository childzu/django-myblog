from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=256)
    slug = models.SlugField(max_length=512, unique=True)
    content = models.TextField (max_length= 5000)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True)
    create_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_post"

    def slug(self):
        return slugify(self.title)
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=128)
    message = models.TextField (max_length= 512)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True)
    create_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_comment"