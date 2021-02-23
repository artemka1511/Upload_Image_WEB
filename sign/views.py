from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import BaseRegisterForm


class HomePageView(TemplateView):
    template_name = 'main.html'


class RedirectView(TemplateView):
    template_name = 'sign/redirect.html'


class SuccessView(TemplateView):
    template_name = 'sign/success_registration.html'


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/sign/success/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('redirect')
        return super(BaseRegisterView, self).dispatch(request, *args, **kwargs)