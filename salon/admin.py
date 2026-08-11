import openpyxl
from django.contrib import admin
from django.http import HttpResponse
from .models import Service, Appointment

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_minutes')

# Custom action Excel exportáláshoz
@admin.action(description='Kijelölt foglalások exportálása Excelbe (.xlsx)')
def export_to_excel(modeladmin, request, queryset):
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename="foglalasok.xlsx"'

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Foglalások"

    # Fejléc sor
    headers = ['Teljes név', 'E-mail cím', 'Telefonszám', 'Szolgáltatás', 'Foglalás időpontja']
    ws.append(headers)

    # Adatsorok betöltése
    for app in queryset:
        ws.append([
            app.full_name,
            app.email,
            app.phone,
            app.service.name,
            app.date_time.strftime('%Y-%m-%d %H:%M')
        ])

    wb.save(response)
    return response

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'service', 'date_time', 'phone', 'email')
    
    # Közvetlen módosíthatóság a listában: az időpont és szolgáltatás helyben átírható!
    list_editable = ('service', 'date_time')
    
    list_filter = ('date_time', 'service')
    search_fields = ('full_name', 'email', 'phone')
    
    # Custom Excel export akció hozzáadása a műveletekhez
    actions = [export_to_excel]