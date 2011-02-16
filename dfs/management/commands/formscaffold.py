"""
Wrapper to call scaffold from the commandline to dynamically generate::
  from dfs import scaffold
  from app_name.forms import CustomForm
  form = CustomForm()
  print scaffold.as_ul(form)
"""

from dfs import scaffold
from django.core.management.base import BaseCommand, CommandError

def do_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

class Command(BaseCommand):
    help = "Wrapper to call form scaffolding from the commandline, e.g.\nformscaffold my_app.forms MyForm as_p"
    args = "<form module> <form class name> <output type>"

    def handle(self, *args, **options):
        module_path = args[0]
        form_name = args[1]
        output_type = args[2]

        scaffolder = getattr(scaffold, output_type)
        form = getattr(do_import(module_path), form_name)
        self.stdout.write(scaffolder(cls=form))
        self.stdout.write("\n")
