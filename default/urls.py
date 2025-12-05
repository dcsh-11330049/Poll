"""
Consists of the Paths assigned to "default" app
"""
from django.urls import path
from .views import *

urlpatterns = [
    path("", poll_list),
    path("list", PollList.as_view(), name='poll_list'),
    path("<int:pk>/", PollView.as_view(), name='poll_view'),
    path("<int:oid>/vote", PollVote.as_view(), name='poll_vote'),
]
