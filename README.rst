``django-form-scaffold`` is a package of helper functions for generating Django template code with markup from Django form instances.

It solves the problem of generating, over and over again, markup for a full form which is effectively a templated version of the
``BaseForm`` ``as_p``, ``as_ul`` and ``as_table`` methods output (which output static values, rather than dyanmic Django template code).

``django-form-scaffold`` outputs in the same form as these methods, but uses the template placeholders for all the form and field values,
which is what I find myself doing time and time again as it's easier to control the individual format/styling etc. of fields in a form,
and is also generally easier for designers to get their heads around a form template.

For example, outputting a login form, rather than doing::

    {{ form.as_p }}

We would do::

    <p>
    {% if form.username.errors %}
      {% for error in form.username.errors %}{{ error }}{% endfor %}
    {% endif %}
    {{ form.username.label }} {{ form.username }}
    </p>
    <p>
    {% if form.password.errors %}
      {% for error in form.password.errors %}{{ error }}{% endfor %}
    {% endif %}
    {{ form.password.label }} {{ form.password }}
    </p>

Requirements
============

 * Django >= 1.1


Installation
============

Install ``django-form-scaffold`` using easy_install (or pip)::

    easy_install django-form-scaffold

Or from the setup script::

    python setup.py install


Usage
=====

Form scaffolding is meant for generating content to then be placed in your template files, so you wouldn't called ``scaffold.as_p``
from within a template itself.

The best way to call the scaffold functions are from within a bootstraped Django Python shell, using the management script::

    python manage.py shell

Then just import scaffold from the ``dfs`` namespace, import your form(s), and pass an instance to one of the functions::

    >>> from dfs import scaffold
    >>> from MyProject.MyApp.forms import MyForm
    >>> form = MyForm()
    >>> print scaffold.as_p(form)
    {% if form.email.errors %}{% for error in form.email.errors %}{{ error }}{% endfor %}{% endif %}
    <p>{{ form.email.label }} {{ form.email }}</p>
    {% if form.password1.errors %}{% for error in form.password1.errors %}{{ error }}{% endfor %}{% endif %}
    <p>{{ form.password1.label }} {{ form.password1 }}</p>
    {% if form.password2.errors %}{% for error in form.password2.errors %}{{ error }}{% endfor %}{% endif %}
    <p>{{ form.password2.label }} {{ form.password2 }}</p>

    >>> # We can also use a form class rather than an instance, but
    >>> # this won't always work if your form requires params etc.,
    >>> # this just creates an instance for you anyway.
    >>> print scaffold.as_ul(cls=MyForm)
    <li>{% if form.email.errors %}{% for error in form.email.errors %}{{ error }}{% endfor %}{% endif %}{{ form.email.label }} {{ form.email }}</li>
    <li>{% if form.password1.errors %}{% for error in form.password1.errors %}{{ error }}{% endfor %}{% endif %}{{ form.password1.label }} {{ form.password1 }}</li>
    <li>{% if form.password2.errors %}{% for error in form.password2.errors %}{{ error }}{% endfor %}{% endif %}{{ form.password2.label }} {{ form.password2 }}</li>

The following helper functions available in ``dfs.scaffold``:

*as_p*
  Outputs the same markup <p> style as the inbuilt Django ``BaseForm.as_p``.

*as_ul*
  Outputs the same markup <ul> style as the inbuilt Django ``BaseForm.as_ul``.

*as_table*
  Outputs the same markup <table> style as the inbuilt Django ``BaseForm.as_table``.

*as_div*
  Extra scaffold-only helper to output an alternative <div> based form layout, similar in layout to ``as_p`` but with <div>s.

Management command
==================

As of v1.1.0 *django-form-scaffold* ships with the management command ``formscaffold``, which acts as a simple wrapper around the scaffold functions.

To use the command just add ``dfs`` to your ``INSTALLED_APPS`` setting and use via ``python manage.py`` (or ``bin/django`` if you're using buildout) like so::

  $ python manage.py formscaffold myapp.forms MyForm as_p

This just use the class-based generation functionality of scaffold functions (pass in a class and they init a blank instance), if you need any customisations performing to the form instance before hand, use from within a Django-ized Python shell as above (e.g. with ``manage.py shell``).
