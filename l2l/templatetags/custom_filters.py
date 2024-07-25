from django import template
from datetime import datetime

register = template.Library()


@register.filter
def l2l_dt(value):
    # Parse the input date string in the format "%Y-%m-%dT%H:%M:%S"
    date_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")

    # Format the date object in the format "%Y-%m-%d %H:%M:%S"
    formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_date
