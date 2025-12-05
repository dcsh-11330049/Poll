from django.shortcuts import render
from django.views.generic import ListView, DetailView, RedirectView
from django.urls import reverse
from .models import *
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.

def poll_list(req: HttpRequest) -> HttpResponse:
    polls = Poll.objects.all()
    return render(req, "default/list.html", {"poll_list": polls, "msg": "Hello!"})

class PollList(ListView):
    model = Poll

    # Searches for the template file: [<App name(in which the model is defined)>/<model name>_list.html] under the templates folder
    # templates/default/poll_list.html      (Filename is all undercase)

class PollView(DetailView):
    model = Poll

    def get_context_data(self, **kwargs) -> dict:
        ctx = super().get_context_data(**kwargs)
        option_list = Option.objects.filter(poll_id=self.object.id)
        ctx['option_list'] = option_list
        return ctx

    # Searches for the template file: [<App name(in which the model is defined)>/<model name>_detail.html] under the templates folder
    # templates/default/poll_detail.html    (Filename is all undercase)

class PollVote(RedirectView):
    # redirect_url = 'https://www.google.com/'  used for static urls
    def get_redirect_url(self, *args, **kwargs) -> str:
        option = Option.objects.get(id=self.kwargs['oid'])
        option.votes += 1
        option.save()
        return reverse('poll_view', kwargs={'pk': option.poll_id})