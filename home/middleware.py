from django.utils.deprecation import MiddlewareMixin
from home.models import Visitor

class VisitorMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, *args, **kwargs):
        Visitor.objects.create(
            url = request.build_absolute_uri(), 
            ip_address = request.META['REMOTE_ADDR']
        )
        return None