from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
# Create your views here.
from .models import Product


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def product_detail_view(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    return HttpResponse({'id': obj.id})


def product_api_detail_view(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Not Found"}, status=404)
    return JsonResponse({'id': obj.id})
