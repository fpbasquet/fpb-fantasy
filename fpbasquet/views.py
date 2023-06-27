from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from .forms import NewUserForm
from django.contrib import messages
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from crispy_forms.helper import FormHelper


class HomeView(TemplateView):
    template_name = "index.html"


class RegisterView(generic.FormView):
    template_name = "register.html"
    form_class = NewUserForm
    success_url = "/"

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        helper = FormHelper()
        form.helper = helper
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form: NewUserForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)


class LoginView(generic.FormView):
    template_name = "login.html"
    form_class = AuthenticationForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        helper = FormHelper()
        form.helper = helper
        return form

    def form_valid(self, form: NewUserForm) -> HttpResponse:
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.info(self.request, f"You are now logged in as {username}.")
            return redirect("/")
        else:
            messages.error(self.request, "Invalid username or password.")
        return super().form_valid(form)
