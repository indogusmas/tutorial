from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.serializers import UserSerializer
from snippets import views


urlpatterns = [
    path('snippets/', views.UserList.as_view()),
    path('snippets/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)