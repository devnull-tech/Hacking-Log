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
    