from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('card', views.CardView)
router.register('figure-card', views.FigureCardView )
router.register('text-card', views.TextCardView )
router.register('deck', views.DeckView )


urlpatterns = [
   path('', include(router.urls)),
   
]