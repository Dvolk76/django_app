from django.shortcuts import render
from django.http import HttpResponse
from phonebook.models import City
# with open(file) as f:
#     for line in f:
#         city = parse(line)
#         City.objects.create(name=city[0])

# Create your views here.
def home_page(request):
    city = City.objects.first()
    return HttpResponse(f"Первый добавленный город {city.name}. pk - {city.pk}")