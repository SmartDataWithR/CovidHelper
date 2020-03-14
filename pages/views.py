from django.views.generic import TemplateView
from ipware import get_client_ip
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

def ip(request):
    ip, is_routable = get_client_ip(request)
    if ip is None:
        ip = "0.0.0.0"
    else:
        if is_routable:
            ipv = "Public"
        else:
            ipv = "Private"
    print(ip, ipv)
    return render(request, 'pages/home.html')