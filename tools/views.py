from . import models
from home.models import Layout
from django.shortcuts import get_object_or_404, render

def index(request):
    layout_data = Layout.objects.filter(in_use=True).first()
    tools = models.Tool.objects.all()
    return render(request, 'tools/index.html', {
        'layout_data': layout_data,
        'tools': tools
    })

def tool(request, tool_id):
    layout_data = Layout.objects.filter(in_use=True).first()
    tool = get_object_or_404(models.Tool, id=tool_id)
    return render(request, 'tools/tool.html', {
        'layout_data': layout_data,
        'tool': tool
    })
