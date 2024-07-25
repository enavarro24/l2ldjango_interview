from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from django.template.defaultfilters import register


@register.filter
def l2l_dt(value):
    try:
        date_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        date_obj = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

    formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_date


def index(request):
    now = datetime.now()
    iso_date = now.strftime("%Y-%m-%dT%H:%M:%S")

    formatted_now = l2l_dt(now.strftime("%Y-%m-%dT%H:%M:%S"))
    formatted_iso = l2l_dt(iso_date)

    template = loader.get_template('l2l/index.html')
    context = {
        'iso': iso_date,
        'now': formatted_now,
        'formatted_iso': formatted_iso
    }
    return HttpResponse(template.render(context, request))
