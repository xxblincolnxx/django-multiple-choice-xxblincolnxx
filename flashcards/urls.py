from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('card', views.CardView)
router.register('deck', views.DeckView )


urlpatterns = [
   path('', include(router.urls)),
]