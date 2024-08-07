from django.urls import path

from .views import IndexView, PageView

app_name = 'pages'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:url>', PageView.as_view(), name='page')
]
