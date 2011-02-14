#template_scaffold.py
"""
Wrapper to call scaffold from the commandline to dynamically generate::
  from dfs import scaffold
  from app_name.forms import CustomForm
  form = CustomForm()
  print scaffold.as_ul(form)
"""

from dfs import scaffold
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = '<form_source> <form_name> <output_type>'
    help = """Wrapper to call form scaffolding from the commandline and output
static markup for a Django form, e.g.:
python manage.py form_scaffold my_app.forms MyCustomForm as_ul
"""

    def handle(self, *args, **options):
        form_sources = args[0]
        form_name = args[1]
        output_type = args[2]

        scaffolder = getattr(scaffold, output_type)
        form = __import__(form_name)
        print scaffolder(form)

