from django.conf.urls import include, url
from .views import MyBotView
urlpatterns = [url(r'^e56155e1e5e92208ad706c1ec3bda6add6ca93469268e501f0/?$', MyBotView.as_view()) ]