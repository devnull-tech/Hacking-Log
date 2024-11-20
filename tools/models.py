from django.db import models

class Tool(models.Model):
    tool_name = models.CharField(max_length=50)
    description = models.TextField()
    zip_url = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.tool_name
