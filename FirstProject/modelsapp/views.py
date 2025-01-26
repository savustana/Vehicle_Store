from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .form import NewUserForm, CarForm, BikeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.conf import settings
from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy

from .models import Car, Motorcycle


def index(request):
    year_filter_max = request.GET.get('year_max')
    year_filter_min = request.GET.get('year_min')
    type_filter_car = request.GET.get('type1')
    type_filter_bike = request.GET.get('type2')
    filter_price_max = request.GET.get('price_max')
    filter_price_min = request.GET.get('price_min')
    filter_price_min_val = request.GET.get('price_min_val')
    filter_price_max_val = request.GET.get('price_max_val')
    filter_search = request.GET.get('search')

    if True:
        if type_filter_car:
            car_list = Car.objects.all()
            if year_filter_max:
                car_list = Car.objects.filter_year_max()
            if year_filter_min:
                car_list = Car.objects.filter_year_min()
            if filter_price_max:
                car_list = Car.objects.filter_price_max()
            if filter_price_min:
                car_list = Car.objects.filter_price_min()
            if filter_price_min_val or filter_price_max_val:
                car_list = Car.objects.filter_custom_price(filter_price_min_val, filter_price_max_val)
        else:
            car_list = []
    if True:
        if type_filter_bike:
            bike_list = Motorcycle.objects.all()
            if year_filter_min:
                bike_list = Motorcycle.objects.filter_year_min()
            if year_filter_max:
                bike_list = Motorcycle.objects.filter_year_max()
            if filter_price_min:
                bike_list = Motorcycle.objects.filter_price_min()
            if filter_price_max:
                bike_list = Motorcycle.objects.filter_price_max()
            if filter_price_min_val or filter_price_max_val:
                bike_list = Motorcycle.objects.filter_custom_price(filter_price_min_val, filter_price_max_val)
        else:
            bike_list = []
    if True:
        if not type_filter_bike and not type_filter_car:
            bike_list = Motorcycle.objects.all()
            car_list = Car.objects.all()

            if filter_search:
                car_list = Car.objects.filter_search(filter_search)
                bike_list = Motorcycle.objects.filter_search(filter_search)
            if not filter_search:
                car_list = Car.objects.all()
                bike_list = Motorcycle.objects.all()
            if year_filter_max:
                bike_list = Motorcycle.objects.filter_year_max()
                car_list = Car.objects.filter_year_max()
            if year_filter_min:
                car_list = Car.objects.filter_year_min()
                bike_list = Motorcycle.objects.filter_year_min()
            if filter_price_min:
                bike_list = Motorcycle.objects.filter_price_min()
                car_list = Car.objects.filter_price_min()
            if filter_price_max:
                bike_list = Motorcycle.objects.filter_price_max()
                car_list = Car.objects.filter_price_max()
            if filter_price_min_val or filter_price_max_val:
                car_list = Car.objects.filter_custom_price(filter_price_min_val, filter_price_max_val)
                bike_list = Motorcycle.objects.filter_custom_price(filter_price_min_val, filter_price_max_val)

    context = {
        'car_list': car_list,
        'bike_list': bike_list,
        'MEDIA_URL': settings.MEDIA_URL,
    }

    return render(request, 'cars/index.html', context)


class HomePage(TemplateView):
    template_name = 'cars/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        car_list = Car.objects.all()

        year_filter_max = self.request.GET.get('year_max')
        year_filter_min = self.request.GET.get('year_min')
        filter_price_max = self.request.GET.get('price_max')
        filter_price_min = self.request.GET.get('price_min')
        filter_price_min_val = self.request.GET.get('price_min_val')
        filter_price_max_val = self.request.GET.get('price_max_val')
        filter_search = self.request.GET.get('search')

        if filter_search:
            car_list = Car.objects.filter_search(filter_search)
        if year_filter_max:
            car_list = Car.objects.filter_year_max()
        if year_filter_min:
            car_list = Car.objects.filter_year_min()
        if filter_price_max:
            car_list = Car.objects.filter_price_max()
        if filter_price_min:
            car_list = Car.objects.filter_price_min()
        if filter_price_min_val or filter_price_max_val:
            car_list = Car.objects.filter_custom_price(filter_price_min_val, filter_price_max_val)

        paginator = Paginator(car_list, 3)
        page_num = self.request.GET.get('page', 1)
        page = paginator.page(page_num)

        context['car_list'] = car_list
        context['MEDIA_URL'] = settings.MEDIA_URL
        context['page'] = page

        return context


class HomePageBike(TemplateView):
    template_name = 'motorcycles/motorcycle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bike_list = Motorcycle.objects.all()

        year_filter_max = self.request.GET.get('year_max')
        year_filter_min = self.request.GET.get('year_min')
        filter_price_max = self.request.GET.get('price_max')
        filter_price_min = self.request.GET.get('price_min')
        filter_price_min_val = self.request.GET.get('price_min_val')
        filter_price_max_val = self.request.GET.get('price_max_val')
        filter_search = self.request.GET.get('search')

        if filter_search:
            bike_list = Motorcycle.objects.filter_search(filter_search)
        if year_filter_max:
            bike_list = Motorcycle.objects.filter_year_max()
        if year_filter_min:
            bike_list = Motorcycle.objects.filter_year_min()
        if filter_price_max:
            bike_list = Motorcycle.objects.filter_price_max()
        if filter_price_min:
            bike_list = Motorcycle.objects.filter_price_min()
        if filter_price_min_val or filter_price_max_val:
            bike_list = Motorcycle.objects.filter_custom_price(filter_price_min_val, filter_price_max_val)

        paginator = Paginator(bike_list, 3)
        page_num = self.request.GET.get('page', 1)
        page = paginator.page(page_num)

        context['bike_list'] = bike_list
        context['MEDIA_URL'] = settings.MEDIA_URL
        context['page'] = page

        return context


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created!')
            return redirect('index.html')
        messages.error(request, 'Please correct the error below.')
    form = NewUserForm()
    return render(request, 'user/register.html', {'register_form': form})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in!')

                request.session['username'] = username
                request.session['visits'] = request.session.get('visits', 0)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the error below.')

    form = AuthenticationForm()

    return render(request, 'user/login.html', {'login_form': form})


def stats(request):
    username = request.session.get('username')
    visits = request.session['visits'] + 1
    # visits = request.session.get('visits', 0)
    context = {'username': username, 'visits': visits}
    return render(request, 'user/stats.html', context)



def logout_page(request):
    logout(request)
    messages.info(request, 'You have been logged out!')
    return redirect('index')


def add_new_car(request):
    if request.method == 'POST':
        car = CarForm(request.POST, request.FILES)
        if car.is_valid():
            car = car.save()
            return HttpResponseRedirect(reverse('info_car', kwargs={'car_id': car.pk}))
        else:
            context = {'form': car}
            return render(request, 'cars/add_car.html', context)
    else:
        car = CarForm(
        )
        context = {'form': car}
        return render(request, 'cars/add_car.html', context)


def info_car(request, car_id):
    car = Car.objects.get_first_by_id(car_id)
    context = {
        'car': car,
        'MEDIA_URL': settings.MEDIA_URL,
        'stars': range(1, 6)
    }
    return render(request, 'cars/info_car.html', context=context)


class CarListView(ListView):
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'car_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MEDIA_URL'] = settings.MEDIA_URL
        return context


class CarCreateView(CreateView):
    model = Car
    template_name = 'cars/add_car.html'
    fields = ['brand', 'model', 'year', 'description', 'image', 'video']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MEDIA_URL'] = settings.MEDIA_URL
        return context


def add_new_bike(request):
    if request.method == 'POST':
        bike = BikeForm(request.POST, request.FILES)
        if bike.is_valid():
            bike = bike.save()
            return HttpResponseRedirect(reverse('bike_info', kwargs={'bike_id': bike.pk}))
        else:
            context = {'form': bike}
            return render(request, 'motorcycles/add_bike.html', context)
    else:
        bike = BikeForm(
        )
        context = {'form': bike}
        return render(request, 'motorcycles/add_bike.html', context)


def delete_car(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        car.delete()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'cars/delete_car.html', {'car': car.pk})


def bike_info(request, bike_id):
    bike = Motorcycle.objects.get_first_by_id(bike_id)
    context = {
        'bike': bike,
        'MEDIA_URL': settings.MEDIA_URL,
        'stars': range(1, 6)
    }
    return render(request, 'motorcycles/bike_info.html', context=context)


class BikeCreateView(CreateView):
    model = Motorcycle
    template_name = 'motorcycles/add_bike.html'
    fields = ['brand', 'model', 'year', 'price', 'description', 'image', 'video']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MEDIA_URL'] = settings.MEDIA_URL
        return context


def delete_bike(request, pk):
    bike = Motorcycle.objects.get(pk=pk)
    if request.method == 'POST':
        bike.delete()
        return HttpResponseRedirect(reverse('motorcycles'))
    return render(request, 'motorcycles/delete_bike.html', {'bike': bike.pk})
