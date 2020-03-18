from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from flashcards import views as flashcard_views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', flashcard_views.homepage, name='home' ),
    path('api/', include('flashcards.urls')),
    path('view_decks/', flashcard_views.view_decks, name='view_decks'),
    path('view_decks/new/', flashcard_views.new_deck, name='new_deck'),
    path('take_quiz/<int:pk>', flashcard_views.take_quiz, name='take_quiz'),
    path('view_decks/show_cards/<int:pk>', flashcard_views.show_cards, name='show_cards'),
    path('accounts/', include('registration.backends.default.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
