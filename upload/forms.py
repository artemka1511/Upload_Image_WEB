from django import forms
from django.core.exceptions import ValidationError


def file_size(value):
    limit = 0.2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Одно из изображений превышает 200кб, загрузка отменена')


class FileFieldForm(forms.Form):
    file_field = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}),
                                  validators=[file_size], label='')
