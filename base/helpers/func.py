import re
import time
from typing import List, Callable
import uuid
import datetime
from io import BytesIO
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.db.models import Lookup
from django.apps import apps


def create_slug(title: str, random_str: str = None) -> str:
    title = re.sub('[^A-Za-z ]+', ' ', title).lower().strip()
    title = re.sub(' +', '-', title)
    if random_str:
        return title + '-' + random_str
    return title


def entries_to_remove(data: dict, removeable_keys: tuple) -> dict:
    for k in removeable_keys:
        data.pop(k, None)
    return data


def remove_duplicate_from_list(iterable: List, key:  Callable = None) -> List:
    if key is None:
        def key(x): return x

    seen = set()
    for elem in iterable:
        k = key(elem)
        if k in seen:
            continue

        yield elem
        seen.add(k)


def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-", "")
    return random[0:string_length]


def convert_to_date(type: str, number: int) -> str:
    today = datetime.date.today()
    if type == "day":
        output_date = today + datetime.timedelta(days=number)
    elif type == "month":
        output_date = today + datetime.timedelta(days=number*30)
    elif type == "year":
        output_date = today + datetime.timedelta(days=number*365)
    return output_date


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return None


def unique_id_generate(number_of_id):
    unique_id_list = []
    for i in range(number_of_id):
        timespan = format(time.time(), '.14f')
        timespan = timespan.split('.')[1]
        unique_id_list.append(timespan)
        time.sleep(0.2)
    return unique_id_list


def format_filter_string(old_dict, keys):
    filtered_dict = {}
    for k in keys:
        if old_dict.get(k):
            filtered_dict[k] = old_dict.get(k)
    return filtered_dict


def get_model_from_any_app(model_name):
    for app_config in apps.get_app_configs():
        try:
            model = app_config.get_model(model_name)
            return model
        except LookupError:
            pass


def flatten(l_data):
    return [item for sublist in l_data for item in sublist]


def snake_to_title(string: str):
    return string.replace("_", " ").title()


class NotEqual(Lookup):
    lookup_name = 'ne'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s <> %s' % (lhs, rhs), params
