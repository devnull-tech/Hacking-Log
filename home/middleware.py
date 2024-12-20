from django.utils.deprecation import MiddlewareMixin
from home.models import Visitor
import datetime
import requests
import json

class VisitorMiddleware(MiddlewareMixin):
    def export_visitors_to_sql(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f'logs/visitors_export_{timestamp}.json'
        with open(output_file, 'w') as f:
            visitors_data = []
            for visitor in Visitor.objects.all():
                visitors_data.append({
                    'url': visitor.url,
                    'ip_address': visitor.ip_address,
                    'country': visitor.country,
                    'city': visitor.city,
                    'method': visitor.method,
                    'payload': visitor.payload,
                    'timestamp': visitor.timestamp.isoformat()
                })
            json.dump(visitors_data, f, indent=4)
    
    def process_view(self, request, view_func, *args, **kwargs):
        if request.path.startswith('/admin/'):
            return None
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', request.META['REMOTE_ADDR']).split(',')[0].strip()
        r = requests.get("http://ip-api.com/json/" + ip_address)
        ip_data = json.loads(r.text)
        payload = request.body.decode('utf-8') if request.body else ""
        Visitor.objects.create(
            url = request.build_absolute_uri(),
            ip_address = request.META['REMOTE_ADDR'],
            country = ip_data.get('country', 'Unknown'),
            city = ip_data.get('city', 'Unknown'),
            method = request.method,
            payload = payload
        )
        
        if Visitor.objects.count() >= 5000:
            self.export_visitors_to_sql()
            Visitor.objects.all().delete()
        return None
