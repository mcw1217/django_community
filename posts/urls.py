from django.urls import path
from posts.views import feeds

app_name = "posts"
urlpatterns = [
    path("feeds/",feeds, name="feeds"),
]

