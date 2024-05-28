from django.db import models


class Social(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=30)
    url = models.URLField()
    def __str__(self):
        return self.name

        
class MemberDetail(models.Model):
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date_of_join = models.DateField()
    social = models.ManyToManyField(Social, related_name='member_social')
    about_text = models.TextField(null=True, blank=True)
    about_image = models.ImageField(upload_to='images/member_about_image/',null=True, blank=True)
    about_video = models.URLField(null=True, blank=True)
    region  = models.ForeignKey('account.Region', on_delete=models.CASCADE, null=True, blank=True)
    price_per_m3 = models.FloatField(default=0.0)
    def __str__(self):
        return self.address


class Members(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/members_logo/')
    detail = models.ForeignKey(MemberDetail,null=True, blank=True, on_delete=models.CASCADE, related_name='member_detail')
    def __str__(self):
        return self.name
