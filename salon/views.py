from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Service, Appointment
from .forms import AppointmentForm

def index(request):
    services = Service.objects.all()[:3]
    return render(request, 'salon/index.html', {'services': services})

def services_view(request):
    services = Service.objects.all()
    return render(request, 'salon/services.html', {'services': services})

def booking_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        date_time_val = request.POST.get('date_time')
        
        if Appointment.objects.filter(date_time=date_time_val).exists():
            messages.error(request, 'Ez az időpont már foglalt! Kérjük válasszon piros jelzés nélküli időpontot.')
        elif form.is_valid():
            form.save()
            messages.success(request, 'Sikeres időpontfoglalás! Várunk szeretettel.')
            return redirect('booking')
    else:
        form = AppointmentForm()

    return render(request, 'salon/booking.html', {'form': form})

def booked_slots_api(request):
    appointments = Appointment.objects.values_list('date_time', flat=True)
    booked_times = [dt.strftime('%Y-%m-%dT%H:%M') for dt in appointments]
    return JsonResponse({'booked_slots': booked_times})

def about_view(request):
    return render(request, 'salon/about.html')

def contact_view(request):
    return render(request, 'salon/contact.html')
