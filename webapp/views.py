from datetime import date
from django.shortcuts import render
from scraping.api_request import request_activity_table
from webapp.dateutils import shift_date, is_date_valid

_DATE_FORMAT = '%d-%m-%Y'

def index_view(request):
    yesterday = shift_date(date.today(), days_to_shift=-1)
    return _render_report(request, request_date=yesterday)

def date_view(request, year, month, day):
    if is_date_valid(year, month, day):
        return _render_report(request, request_date=date(year, month, day))
    else:
        return render(
            request,
            'index.html',
            context={ 'error_msg': 'Invalid date, please select date in format YYYY/MM/DD.'})


def _render_report(request, request_date):
    return render(
        request,
        'report.html',
        context={
            'table': request_activity_table(request_date),
            'date': date.strftime(request_date, _DATE_FORMAT),
            'prev_date': date.strftime(shift_date(request_date, days_to_shift=-1), _DATE_FORMAT),
            'next_date': date.strftime(shift_date(request_date, days_to_shift=+1), _DATE_FORMAT),
        })
