from django.urls import include, path
from rest_framework import routers

from snippet_app import views

router = routers.SimpleRouter()

router.register('snippets', viewset=views.SnippetViewSet, basename='snippets')
router.register('tags', viewset=views.TagViewSet, basename='tags')


urlpatterns = [
    path('', include(router.urls))
]