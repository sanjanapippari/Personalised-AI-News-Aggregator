from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from users.models import CustomUser
from news.models import Headline  # assuming you store scraped news
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = 'Send daily news emails to users'

    def handle(self, *args, **kwargs):
        users = CustomUser.objects.all()

        for user in users:
            location = user.location or "general"
            
            # Fetch top 5-10 headlines for user location
            headlines = Headline.objects.filter(source__icontains=location).order_by('-id')[:10]



            if not headlines:
                headlines = Headline.objects.all().order_by('-id')[:10]

            news_list = "\n".join([f"{i+1}. {h.title} - {h.url}" for i, h in enumerate(headlines)])

            # Send the email
            send_mail(
                subject="📰 Your Daily News Digest",
                message=f"Hi {user.username},\n\nHere are your top headlines for today:\n\n{news_list}\n\nThanks for using NewsDoot!",
                from_email="banukuntalahari@gmail.com",  # update in settings.py
                recipient_list=[user.email],
                fail_silently=False,
            )

        self.stdout.write("Daily news emails sent.")
