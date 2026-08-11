from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Szolgáltatás neve")
    description = models.TextField(verbose_name="Leírás")
    price = models.IntegerField(verbose_name="Ár (Ft)")
    duration_minutes = models.IntegerField(default=60, verbose_name="Időtartam (perc)")
    image_url = models.URLField(blank=True, null=True, verbose_name="Kép URL (vagy Helyőrző)")

    def __str__(self):
        return f"{self.name} ({self.price} Ft)"

class Appointment(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Teljes név")
    email = models.EmailField(verbose_name="E-mail cím")
    phone = models.CharField(max_length=20, verbose_name="Telefonszám")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Kiválasztott szolgáltatás")
    date_time = models.DateTimeField(verbose_name="Foglalás időpontja")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return f"{self.full_name} - {self.service.name} ({self.date_time.strftime('%Y-%m-%d %H:%M')})"