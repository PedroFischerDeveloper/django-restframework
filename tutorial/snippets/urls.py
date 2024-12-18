from django.urls import include, path
from rest_framework.routers import DefaultRouter

from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('snippets', views.SnippetViewSet)
router.register('users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]