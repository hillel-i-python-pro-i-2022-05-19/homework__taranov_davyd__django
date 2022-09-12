from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.humans.models import Human


class HumanEditView(UpdateView):
    model = Human
    fields = ["name", "age", "avatar"]
    success_url = reverse_lazy("humans:show_all")
