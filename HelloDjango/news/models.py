from django.db import models
from django.contrib.auth.models import User
from members.models import Members
class Document(models.Model):
    type_choices = (
        ('notification','Хабарландыру'),
        ('contract','Келісімшарт'),
        ('report','Есеп'),
        ('instruction','Нұсқаулық'),
    )

    title = models.CharField(max_length = 300)
    member = models.ForeignKey(Members, on_delete = models.CASCADE, null = True, related_name = 'member_document')
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, related_name = 'user_document')
    type = models.CharField(max_length = 100,choices = type_choices)
    file = models.FileField(upload_to='documents/')
    date = models.DateField(auto_now_add=True,null = True)
    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length = 500)
    sub_title = models.TextField()
    user = models.ForeignKey('auth.User', on_delete = models.CASCADE, null = True, related_name = 'user_news')
    cover_img = models.ImageField(upload_to='img/news_img/')
    news_details = models.ManyToManyField('NewsDetails', related_name = 'news_det',related_query_name='news_det')
    date = models.DateField(auto_now_add=True)
    send_email_newsletter = models.BooleanField(default = False)
    def __str__(self):
        return f'{self.title}'

class NewsDetails(models.Model):
    title = models.CharField(max_length = 300,null=True,blank=True)
    text = models.TextField(null = True,blank =True )
    video = models.URLField(null = True,blank =True)
    img = models.ImageField(null = True,blank =True,upload_to='img/news_img/')
    def __str__(self):
        return f"{self.title}" 

    
class NewsSubscribeList(models.Model):
    email = models.CharField(max_length = 100)
    def __str__(self):
        return str(self.email)