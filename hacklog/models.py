from django.db import models
from openai import OpenAI

class Bot(models.Model):
    provider = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    system_prompt = models.CharField(max_length=200)
    temperature = models.FloatField()
    base_url = models.CharField(max_length=50)
    api_key = models.CharField(max_length=200)
    input_max_tokens = models.IntegerField()
    in_use = models.BooleanField(default=False)
    
    def send_prompt(self, prompt: str) -> dict: 
        client = OpenAI(
            api_key=self.api_key, 
            base_url=self.base_url
        )
        completion = client.chat.completions.create(
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
            ], 
            model = self.model,
            temperature = self.temperature
        )
        return {
            'text': completion.choices[0].message.content,
            'prompt_tokens': completion.usage.prompt_tokens,
            'response_tokens': completion.usage.completion_tokens,
            'bot': self
        }

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
