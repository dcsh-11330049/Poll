"""
Consists of the Paths assigned to "default" app
"""
from django.urls import path
from .views import *

urlpatterns = [
    #path("", poll_list),
    path("", PollList.as_view(), name='poll_list'),
    path("<int:pk>/", PollView.as_view(), name='poll_view'),
    path("<int:oid>/vote", PollVote.as_view(), name='poll_vote'),
    path("create", PollCreate.as_view(), name='poll_create'),
    path("<int:pk>/edit", PollEdit.as_view(), name='poll_edit'),
    path("<int:pid>/add-option", OptionCreate.as_view(), name="option_create"),
    path("<int:oid>/modify", OptionEdit.as_view(), name="option_edit"),
    path("<int:pk>/delete", PollDelete.as_view(), name='poll_delete'),
    path("<int:pk>/remove", OptionDelete.as_view(), name='option_delete'),
]
