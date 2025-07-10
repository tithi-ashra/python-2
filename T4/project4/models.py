from django.db import models

# Create your models here.
class blogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='blog_images/',blank=True,null=True)
    reference_link = models.URLField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    publish_date = models.DateField()

    def __str__(self):
        return self.title
