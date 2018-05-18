
from django.urls import re_path
from django.contrib import admin

from bot.views import (
    FacebookWebhookView
    )

app_name ='bot_webhooks'

urlpatterns = [
    re_path(r'^<webhook_endpoint>/$', FacebookWebhookView.as_view(), name='webhook'),
]
