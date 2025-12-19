from django.shortcuts import render
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import *
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.

def poll_list(req: HttpRequest) -> HttpResponse:
    polls = Poll.objects.all()
    return render(req, "default/poll_list.html", {"poll_list": polls, "msg": "Hello!"})

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

class PollCreate(CreateView):
    model = Poll
    fields = '__all__'  # ['topic', 'description']
    # 成功後要去的路徑固定，直接透過 success_url 屬性指定就可以了
    success_url = reverse_lazy('poll_list')

class PollEdit(UpdateView):
    model = Poll
    fields = '__all__'

    # 成功後要去的路徑不固定，則需定義 get_success_url() 方法來回傳
    def get_success_url(self) -> str:
        return reverse('poll_view', kwargs={'pk': self.object.id})

class OptionCreate(CreateView):
    model = Option
    fields = ['title']

    def form_valid(self, form) -> HttpResponse:
        form.instance.poll_id = self.kwargs['pid']
        return super().form_valid(form)
    def get_success_url(self) -> str:
        return reverse('poll_view', kwargs={'pk': self.kwargs['pid']})

class OptionEdit(UpdateView):
    model = Option
    fields=['title']
    pk_url_kwarg = 'oid'
    def get_success_url(self) -> str:
        return reverse('poll_view', kwargs={'pk': self.object.poll_id})
    
    # "self.object" refers to the current object

class PollDelete(DeleteView):
    model = Poll
    success_url = reverse_lazy('poll_list')

class OptionDelete(DeleteView):
    model = Option
    def get_success_url(self) -> str:
        return reverse('poll_view', kwargs={'pk': self.object.poll_id})