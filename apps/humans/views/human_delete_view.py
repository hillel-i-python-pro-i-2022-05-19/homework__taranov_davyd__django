# from django.contrib import messages
# from django.shortcuts import redirect
# from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.humans.models import Human


class HumanDeleteView(DeleteView):
    model = Human
    success_url = reverse_lazy("humans:show_all")
