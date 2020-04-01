from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'banners': [
            {'src': '/static/images/banner-image-3.jpg'}
        ]
    }
    return render(request, 'frontend/index.html', context)
