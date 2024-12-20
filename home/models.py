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
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # TODO: Get country and more data
    def __str__(self) -> str:
        return self.ip_address
    