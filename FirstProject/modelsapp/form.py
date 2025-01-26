from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Car, Motorcycle


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CarForm(forms.ModelForm, forms.ImageField):
    class Meta:
        model = Car
        fields = ('brand', 'model', 'year', 'price', 'description', 'engine', 'speed',
                  'transmission', 'fuel_system', 'image', 'video', 'rate')

    def save(self, commit=True):
        car = super(CarForm, self).save(commit=False)
        if commit:
            car.save()
        return car


class BikeForm(forms.ModelForm, forms.ImageField):
    class Meta:
        model = Motorcycle
        fields = ('brand', 'model', 'year', 'price', 'description', 'engine', 'speed',
                  'size', 'fuel_system', 'image', 'video', 'rate')

    def save(self, commit=True):
        bike = super(BikeForm, self).save(commit=False)
        if commit:
            bike.save()
        return bike
