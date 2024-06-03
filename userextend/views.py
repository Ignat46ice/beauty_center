import random
from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView
from userextend.forms import UserForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    # form_valid este o metoda in clasa de view si este apelata atunci cand formularul este trimis catre salvare,
    # iar programatorul poate sa suplimenteze cu actiuni noi.

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_user = form.save(commit=False)
    #
    #         new_user.first_name = new_user.first_name.title()
    #         new_user.last_name = new_user.last_name.title()
    #
    #         # customizare username Usernameul sa fie compus din prima litera din:
    #         # first_name + last_name+_+6 cifre generate random ex:. hscurtu_123456
    #         new_user.username = f'{new_user.first_name[0].lower()}{new_user.last_name.replace("", "").lower()}_{random.randint(100000, 999999)}'
    #
    #         new_user.save()
    #         # atribui valoarea new_user.first_name.title() campului first_name al obiectului new_user
    #
    #         # trimitere mail FARA TEMPLATE
    #         subject = 'Cont nou in aplicatia DjangoProject'
    #         message = (f'Buna ziua, {new_user.first_name} {new_user.last_name}! Felicitari, contul tau a fost adaugat'
    #                    f' cu succes. Numele de utilizator pentru autentificare este: {new_user.username}')
    #         # send_mail(subject, message, EMAIL_HOST_USER, [new_user.email])
    #
    #         # trimitere mail CU TEMPLATE
    #
    #         details_user = {
    #             'fullname': f'{new_user.first_name} {new_user.last_name}',
    #             'user_name': new_user.username
    #         }
    #
    #         subject = 'Cont nou in aplicatia DjangoProject'
    #         message = get_template('mail.html').render(details_user)
    #         mail = EmailMessage(
    #             subject,
    #             message,
    #             EMAIL_HOST_USER,
    #             [new_user.email]
    #         )
    #         mail.content_subtype = 'html'
    #         mail.send()
    #
    #         # implemetare istoric
    #         log = (f'La data de {datetime.now()} a fost adaugat utilizator nou: first_name:{new_user.first_name},'
    #                f'last_name: {new_user.last_name}, email: {new_user.email} si username:{new_user.username}.')
    #
    #         UserHistory.objects.create(history_log=log)
    #
    #     return redirect('login')
