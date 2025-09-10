from django.shortcuts import render, redirect
import requests
from news.models import Headline
from users.models import UserFeedback  # import this
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.http import urlencode

from django.shortcuts import redirect
from django.utils.http import urlencode
import requests
from news.models import Headline

from django.shortcuts import redirect
from news.models import Headline
import requests
from django.utils.http import urlencode

from django.shortcuts import render
import requests
from django.utils.http import urlencode


from django.shortcuts import render, redirect
import requests
from django.utils.http import urlencode
from news.models import Headline

def scrape(request):
    Headline.objects.all().delete()

    API_KEY = 'c5421a708e1f48868e758b0602bd8d87'
    base_url = "https://newsapi.org/v2/everything"

    # Extract individual query parameters as strings (NOT lists)
    selected_language = request.GET.get('lang', 'en')
    query = request.GET.get('q', 'news')
    from_date = request.GET.get('from', '')
    to_date = request.GET.get('to', '')
    source = request.GET.get('source', '')

    # Build clean query dictionary
    query_params = {
        'apiKey': API_KEY,
        'language': selected_language,
        'sortBy': 'publishedAt',
        'q': query,
    }

    if from_date:
        query_params['from'] = from_date

    if to_date:
        query_params['to'] = to_date

    if source:
        query_params['sources'] = source

    url = f"{base_url}?{urlencode(query_params)}"
    print("FILTERED API URL:", url)

    response = requests.get(url)
    data = response.json()

    if data.get("status") != "ok":
        print("Error:", data)
        return redirect(f"/?lang={selected_language}")

    for article in data.get("articles", []):
        Headline.objects.create(
            title=article.get('title', 'No Title'),
            url=article.get('url', '#'),
            image=article.get('urlToImage', ''),
            source=article.get("source", {}).get("name", ""),
            language=selected_language,
        )

    # Reconstruct cleaned URL to pass back
    redirect_params = {
        'lang': selected_language,
        'q': query,
        'from': from_date,
        'to': to_date,
        'source': source,
    }

    return redirect(f"/news/?{urlencode(redirect_params)}")

def scrape_by_category(request, name):
    Headline.objects.all().delete()

    API_KEY = 'c5421a708e1f48868e758b0602bd8d87'
    selected_language = request.GET.get('lang', 'en')

    url = f"https://newsapi.org/v2/everything?q={name}&sortBy=publishedAt&language={selected_language}&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    for article in data.get('articles', []):
        Headline.objects.create(
            title=article.get('title', 'No Title'),
            url=article.get('url', '#'),
            image=article.get('urlToImage', '')
        )

    return redirect(f"/?lang={selected_language}")


from users.models import UserFeedback
from django.db.models import Q

@login_required
def news_list(request):
    headlines = Headline.objects.all().order_by('-id')
    
    # Recommendation logic
    recommended = []
    if request.user.is_authenticated:
        liked_articles = UserFeedback.objects.filter(user=request.user, action='like')
        liked_keywords = []

        for item in liked_articles:
            # Use words from title as a basic way to extract keywords
            liked_keywords.extend(item.article_title.split())

        # Basic filtering using keywords from liked articles
        if liked_keywords:
            query = Q()
            for word in liked_keywords:
                query |= Q(title__icontains=word)
            recommended = Headline.objects.filter(query).exclude(
                url__in=liked_articles.values_list('article_url', flat=True)
            ).distinct()[:10]  # Limit to 10 suggestions

    categories = ["general", "business", "entertainment", "health", "science", "sports", "technology"]
    context = {
        "object_list": headlines,
        "categories": categories,
        "recommended_articles": recommended,  # 👈 Pass to template
    }
    return render(request, "news/home.html", context)


@csrf_exempt
@login_required
def toggle_feedback(request):
    if request.method == "POST":
        url = request.POST.get("url")
        action = request.POST.get("action")
        title = request.POST.get("title", "")
        image = request.POST.get("image", "")
        source = request.POST.get("source", "")

        # Try to update existing or create new
        feedback, created = UserFeedback.objects.update_or_create(
            user=request.user,
            article_url=url,
            defaults={
                "action": action,
                "article_title": title,
                "image": image,
                "source": source,
            }
        )
        return JsonResponse({"status": "ok", "created": created})
    return JsonResponse({"status": "error", "message": "Invalid method"})


from django.http import JsonResponse
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import requests
from bs4 import BeautifulSoup

import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# news/views.py

from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt

import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# news/views.py

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests

@csrf_exempt
def summarize_article_view(request):
    url = request.GET.get('url')
    if not url:
        return JsonResponse({'error': 'URL is required'}, status=400)

    try:
        api_url = "https://textanalysis-text-summarization.p.rapidapi.com/text-summarizer"

        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "8db9512274mshc892a7602373bffp18d29fjsned6f20adcd9e",  # ✅ Your real key
            "X-RapidAPI-Host": "textanalysis-text-summarization.p.rapidapi.com"
        }

        payload = {
            "url": url,
            "text": "",
            "sentnum": 6  # Change this number to control length of summary
        }

        response = requests.post(api_url, headers=headers, json=payload)
        data = response.json()

        if response.status_code == 200 and "sentences" in data:
            summary_sentences = data["sentences"]
            return JsonResponse({
                "title": "Summarized Article",
                "summary": " ".join(summary_sentences)
            })
        else:
            return JsonResponse({"error": "Failed to summarize article", "details": data}, status=500)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

from django.core.mail import send_mail
from django.http import HttpResponse

def test_email(request):
    send_mail(
        subject='📰 NewsDoot Test Email',
        message='This is a test email to confirm email setup is working!',
        from_email='banukuntalahari@gmail.com',
        recipient_list=['archanabhanukunta@gmail.com'],  # replace with your real email
        fail_silently=False,
    )
    return HttpResponse("Test email sent!")
