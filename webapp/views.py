from django.shortcuts import render

from scraping.api_request import request_activity_table


def index_view(request):
    return date_view(request, None)

def date_view(request, date):
    return render(
        request,
        'index.html',
        context={'table': request_activity_table(date)}
    )