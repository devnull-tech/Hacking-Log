from django.db import models

class Layout(models.Model):
    layout_name = models.CharField(max_length=100)
    base64_banner = models.TextField()
    title = models.CharField(max_length=30)
    home_html = models.TextField()
    contact_html = models.TextField()
    in_use = models.BooleanField()

    def __str__(self) -> str:
        return self.layout_name

class Visitor(models.Model):
    url = models.URLField()
    ip_address = models.GenericIPAddressField()
    country = models.CharField(max_length=70)
    city = models.CharField(max_length=200)
    method = models.TextField(default="GET")
    payload = models.TextField(default="")
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.ip_address
    