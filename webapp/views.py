import requests
from django.shortcuts import render
from scraping.api_request import build_activity_report_query


def index(request):
    url, headers = build_activity_report_query('2018-05-16')
    resp = requests.get(url, headers=headers)
    return render(
        request,
        'index.html',
        context={'table': str(resp.text)}
    )