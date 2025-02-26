import re

from django.forms import ModelForm, ImageField

from apps.models import User, Order


class ProfileForm(ModelForm):
    photo = ImageField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'email')


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = 'product', 'full_name', 'phone_number'

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        return re.sub('\D', '', phone_number)


# class StreamForm(ModelForm):
#     class Meta:
#         model = Stream
#         fields = 'name', 'discount', 'product', 'owner'
