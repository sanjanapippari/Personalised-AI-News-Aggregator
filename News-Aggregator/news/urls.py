from django.urls import path
from news.views import scrape_by_category, scrape, news_list
from .views import toggle_feedback, summarize_article_view, test_email
from django.views.i18n import set_language

urlpatterns = [
    path("", news_list, name="home"),

    # 🌐 Filter news by keywords, language, source
    path("filter/", scrape, name="scrape_filters"),

    # 📂 Browse by category (requires argument!)
    path("scrape/<str:name>/", scrape_by_category, name="scrape_by_category"),

    # 💬 Feedback and Summary
    path('toggle-feedback/', toggle_feedback, name='toggle_feedback'),
   
    path('summarize/', summarize_article_view, name='summarize_article'),

    # 🌍 Language support
    path('i18n/setlang/', set_language, name='set_language'),

    # 📧 Test email
    path('test-email/', test_email, name='test_email'),
]
