import re
from django import forms
from django.core.exceptions import ValidationError
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['full_name', 'email', 'phone', 'service', 'date_time']

    def clean_full_name(self):
        name = self.cleaned_data.get('full_name', '').strip()
        if not re.match(r'^[a-zA-ZáéíóöőúüűÁÉÍÓÖŐÚÜŰ\s-]+$', name):
            raise ValidationError('A név csak betűket, szóközt és kötőjelet tartalmazhat!')
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        if not re.match(r'^[0-9]{8,11}$', phone):
            raise ValidationError('A telefonszám csak számjegyekből állhat és maximum 11 karakter lehet!')
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip()
        email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        if not re.match(email_regex, email):
            raise ValidationError('Kérjük, adjon meg egy érvényes e-mail címet!')
        return email
