from django.db import models

class Layout(models.Model):
    layout_name = models.CharField(max_length=100)
    base64_banner = models.TextField()
    title = models.CharField(max_length=30)
    text_color = models.CharField(max_length=50)
    navbar_color = models.CharField(max_length=50)
    bg_color = models.CharField(max_length=50)
    footer_color = models.CharField(max_length=50)
    home_html = models.TextField()
    contact_html = models.TextField()
    in_use = models.BooleanField()
    