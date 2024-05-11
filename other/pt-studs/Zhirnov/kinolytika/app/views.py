from datetime import timedelta

from django.contrib.auth import authenticate, login
import django.contrib.auth.forms as auth_forms
import django.contrib.auth.views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
import django.views.generic as generic_views

from app.models import Film, FilmShow, Genre, Hall, HallPlace, Ticket


class LoginView(auth_views.LoginView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        register_form: auth_forms.UserCreationForm = context.get('register_form')
        if register_form:
            context['register_form'] = auth_forms.UserCreationForm(data=register_form.data)
        else:
            context['register_form'] = auth_forms.UserCreationForm()
        context['register_form'].fields['username'].help_text = 'Только буквы, цифры и символы @/./+/-/_'
        context['register_form'].fields['password1'].help_text = 'Ваш пароль должен содержать как минимум 8 символов'
        context['register_form'].fields['password2'].help_text = 'Для подтверждения введите, пожалуйста, пароль ещё раз'
        return context


class RegisterView(generic_views.FormView):
    form_class = auth_forms.UserCreationForm
    success_url = reverse_lazy('index')
    http_method_names = ['post']

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class FilmsView(generic_views.ListView):
    template_name = 'films.html'

    def get_queryset(self):
        active_films = sorted(FilmShow.objects.filter(datetime__gt=timezone.now()), key=lambda f: f.datetime)
        return active_films


class AddFilmView(generic_views.TemplateView):
    template_name = 'add_film.html'

    def post(self, request, *args, **kwargs):
        hall_id = self.request.POST.get('hall_id')
        filmshow_id = self.request.POST.get('filmshow_id')
        number = self.request.POST.get('number')
        if not hall_id or not number or not filmshow_id:
            context = {'response': 'Во время оплаты произошла ошибка...'}
        else:
            place = HallPlace.objects.get(hall_id=hall_id, number=number)
            ticket = Ticket(owner=self.request.user, filmshow_id=filmshow_id, place=place)
            ticket.save()
            context = {'response': 'Оплата прошла успешно. Билет появился у вас в профиле...'}
        return render(request, self.template_name, context)


class ProfileView(generic_views.ListView):
    template_name = 'profile.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return {*sorted(FilmShow.objects.filter(datetime__gt=timezone.now(), ticket__owner=self.request.user), key=lambda f: f.datetime)}
        else:
            return []


class StatisticsView(generic_views.TemplateView):
    template_name = 'statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        l2w = timezone.now() - timedelta(days=14)
        for_data = lambda c: c[1]

        shows = FilmShow.objects.filter(datetime__gt=l2w)
        tickets = Ticket.objects.filter(datetime__gt=l2w)
        films = Film.objects.all()
        halls = Hall.objects.all()
        genres = Genre.objects.all()

        context['shows_l2w_films'] = sorted([[film.title, shows.filter(film=film).count()] for film in films if shows.filter(film=film).count() != 0], key=for_data, reverse=True)
        context['shows_l2w_films_size'] = max(map(for_data, context['shows_l2w_films']))
        context['shows_l2w_halls'] = sorted([[hall.title, shows.filter(hall=hall).count()] for hall in halls if shows.filter(hall=hall).count() != 0], key=for_data, reverse=True)
        context['shows_l2w_halls_size'] = max(map(for_data, context['shows_l2w_halls']))
        context['shows_l2w_genres'] = sorted([[genre.title, shows.filter(film__genres=genre).count()] for genre in genres if shows.filter(film__genres=genre).count() != 0], key=for_data, reverse=True)
        context['shows_l2w_genres_size'] = max(map(for_data, context['shows_l2w_genres']))

        context['tickets_l2w_films'] = sorted([[film.title, tickets.filter(filmshow__film=film).count()] for film in films if tickets.filter(filmshow__film=film).count() != 0], key=for_data, reverse=True)
        context['tickets_l2w_films_size'] = max(map(for_data, context['tickets_l2w_films']))
        context['tickets_l2w_halls'] = sorted([[hall.title, tickets.filter(filmshow__hall=hall).count()] for hall in halls if tickets.filter(filmshow__hall=hall).count() != 0], key=for_data, reverse=True)
        context['tickets_l2w_halls_size'] = max(map(for_data, context['tickets_l2w_halls']))
        context['tickets_l2w_genres'] = sorted([[genre.title, tickets.filter(filmshow__film__genres=genre).count()] for genre in genres if tickets.filter(filmshow__film__genres=genre).count() != 0], key=for_data, reverse=True)
        context['tickets_l2w_genres_size'] = max(map(for_data, context['tickets_l2w_genres']))

        return context
