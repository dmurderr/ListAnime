from django.views.generic import CreateView ,DeleteView , UpdateView
from django.contrib.auth.forms import UserCreationForm


class userCreateView(CreateView):
    model = user
    template_name = ".html"
