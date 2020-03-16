import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

from django.utils.translation import ugettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks later (default 3 weeks).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        if data < datetime.date.today():
            raise ValidationError(_("Invalid Date - Renewal in past."))
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidatioError(_("Invalid Date - Renewal more than 4 weeks aheed"))
        return data
