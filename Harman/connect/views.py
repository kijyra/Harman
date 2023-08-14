from django.shortcuts import render
from .models import Connection, Printer

def connect_page(request):
    connections = Connection.objects.all()
    location_connections = []
    for i in connections:
        if i.location not in location_connections:
            location_connections.append(i.location)
    printers = Printer.objects.all()

    context = {
        'connections': connections,
        'location_connections': location_connections,
        'printers': printers,
    }
    return render(request, 'connection.html', context )