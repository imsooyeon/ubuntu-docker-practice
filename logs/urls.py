from django.urls import path

from logs.views import LogView

urlpatterns = [
    path('/infos', LogView.as_view())
]
# from logs.views import LogView

# urlpatterns = [
#     path('logs', LogView.as_view())
# ]