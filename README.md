#  Team - INTELLICAST 
#  Track - Digital Dawn + AI Solution

#  NewsDoot – Personalized News Aggregator using AI

An AI powered Personalized News Aggregator that delivers real time, relevant, and engaging news tailored to user preferences.  
Built with Django + NewsAPI + Python, the platform combines personalization, interactivity, and scalability to transform how people consume news.  

##  Problem Statement
In today’s digital era, users are overwhelmed with generic and biased news.  
Existing platforms lack personalization, interactivity, and accessibility across languages.  
Users need a smart, adaptive system that filters clutter and delivers trustworthy, engaging, and user focused news .

## Proposed Solution

NewsDoot solves this by:
* Aggregating news in real time from trusted sources.  
* Providing personalized recommendations using Like/Dislike feedback and sentiment analysis.  
* Enhancing engagement with chatbot queries, multi-language support, and community discussions .  
* Offering a clean dashboard with Light/Dark themes, filtering, newsletters, and analytics.  
* Built on a scalable Django backend with modular APIs.

## Key Features

*  Real time Aggregation – NewsAPI integration for trusted, live updates  
*  Personalization – Like/Dislike feedback loop + sentiment analysis  
*  Chatbot – Ask for suggestions  
*  Multi language Support – Regional + international news (supports different languages) 
*  Community Discussions – Share their comments.
*  Save & Share – Bookmark articles, share via WhatsApp/Telegram
*  Analytics Dashboard – Track reading habits and preferences  
*  Light/Dark Mode – Modern UI experience  
*  Daily Newsletters – Personalized email updates  

## Tech Stack

* Backend: Python, Django  
* Frontend: HTML, CSS, JS  
* Database: SQLite    
* APIs: NewsAPI for real time news  
* ML Model : Logistic Regression(best for fast and provides interpretability) for sentiment analysis  

## Simple yet effective System Architecture

			 ↗  ML Layer (Sentiment Analysis) 
NewsAPI → Django Backend →  Frontend Dashboard (HTML/JS)    → Database
                         ↘  Chatbot, Analytics, Newsletters
        ----------------------------------------------------------------------------------------


## How To Use

#### Software Requirements

Python3

#### Installation

Install the dependencies by running:
```html  
    pip install bs4
    pip install requests
    pip install django-social-share
```

#### Run using Command Prompt

Navigate to the News-Aggregator folder which has manage.py file then run the following command on cmd

```html
python manage.py runserver
```

### Tech stack

`Backend` : Python3,Beautiful soup <br>
`Framework` : Django <br>
`Database` : Sqlite3 <br>
`Frontend` : Html,CSS,Bootstrap <br>
