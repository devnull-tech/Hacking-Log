from django.db import models

class Term(models.Model):
    term = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.term

class Log(models.Model):
    vm_name = models.CharField(max_length=50)
    platform = models.CharField(max_length=3, choices=[
        ('VH', 'VulnHub'),
        ('HTB', 'HackTheBox')
    ])
    operating_system = models.CharField(max_length=20)
    tags = models.CharField(max_length=200)
    html_writeup = models.TextField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.vm_name
