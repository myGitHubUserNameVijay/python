from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.http import Http404



monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for atleast 20 minutes everyday!",
    "march": "Learn Django for atleast 20 minutes everyday!",
    "april": "Eat no meat for the entire month!",
    "may": "Learn Django for atleast 20 minutes everyday!",
    "june": "Walk for atleast 20 minutes everyday!",
    "july": "Walk for atleast 20 minutes everyday!",
    "august": "Walk for atleast 20 minutes everyday!",
    "september": "Walk for atleast 20 minutes everyday!",
    "october": "Walk for atleast 20 minutes everyday!",
    "november": "Walk for atleast 20 minutes everyday!",
    "december": None
}
# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges\index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    if month > 12:
        return HttpResponse("Invalid Month!")

    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"text": challenge_text, "month_name": month})
    except:
        response_data = render_to_string("404.html")
        raise Http404()
