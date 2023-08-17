from django.shortcuts import render
from .models import Connection, Printer

def connect_page(request):
    connections = Connection.objects.all()
    locations = []
    cabinets = {
        'Главный склад': 'Склад',
        'СКС': 'Продажи',
        'Кондитерка (2 этаж)': 'Холодильник',
        'Сканеры': 'Бухгалтерия',
        'Подвал': 'АБК',
        'Конференц-зал': 'АБК',
        'Отдел закупок': 'Холодильник',
        'Кабинет операционного директора': 'Холодильник',
        'Кабинет начальника службы контроля': 'Холодильник',
        'Логисты': 'Бухгалтерия',
        'Бухгалтерия (1й кабинет)': 'Бухгалтерия',
        'Бухгалтерия (2й кабинет)': 'Бухгалтерия',
        'Бухгалтерия (3й кабинет)': 'Бухгалтерия',
        'Кабинет руководителя логистики': 'Продажи',
        'Отдел кадров': 'Продажи',
        'Отдел продаж': 'Продажи',
        'Кабинет Красногоровой Галины': 'Продажи',
        'Приёмная Р.О.': 'АБК',
        'Кабинет экономиста': 'АБК',
    }
    for i in connections:
        if i.location not in locations:
            locations.append(i.location)

    printers = Printer.objects.all()

    context = {
        'connections': connections,
        'locations': locations,
        'cabinets': cabinets,
        'printers': printers,
    }
    return render(request, 'connection.html', context )