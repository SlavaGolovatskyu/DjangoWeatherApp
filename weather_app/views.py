import requests as _requests

from django.shortcuts import render

from . import models
from .forms import CityForm


def index(request):
    user_ip = request.META.get("REMOTE_ADDR")

    try:
        user = models.UserIP.objects.get(ip=user_ip)
    except:
        user = models.UserIP(ip=user_ip)
        user.save()
    
    if request.method == 'POST':
        city_model = models.City(name=request.POST.get('name'), user=user)
        city_model.save()

        all_cities_user = models.City.objects.filter(user=user)

        # Сохраняем максимум 2 города в базе данных привязаных к ip человека
        if len(all_cities_user) > 2:
            oldest_city = all_cities_user[0]
            oldest_city.delete()
        
    form = CityForm()

    api_key = '6d362e7f2d4bf5439595d0ab38b67c1c'

    cities = models.City.objects.filter(user=user).order_by('timestamp').distinct().reverse()[:5]

    cities_inf = []
    errors = {}

    if not cities:
        pass
    else:
        for city in cities:
            url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&appid={1}' \
                  .format(city.name, api_key)
            req = _requests.get(url).json()

            try:
                info = {
                    'city_name': city.name,
                    'temp': req['main']['temp'],
                    'icon': req['weather'][0]['icon']
                }
                cities_inf.append(info)
            except KeyError:
                errors['city_error'] = f'По вашему запросу города: {city.name} небыло найдено.'
                city.delete()

    context = {'info': cities_inf, 'form': form, 'errors': errors}

    return render(request, 'weather/index.html', context)


def support(request):
    context = {}
    errors = {}



    return render(request, 'support.html', context)