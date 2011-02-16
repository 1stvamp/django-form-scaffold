from django.utils.encoding import force_unicode
from django.forms.forms import BoundField
from django.utils.html import conditional_escape


def as_p(instance=None, cls=None):
    "Returns this form rendered as HTML <p>s."
    if not instance and not cls:
        return TypeError('as_p takes at least 1 argument (0 given)')
    elif instance and cls:
        return TypeError('as_p takes at most 1 argument (2 given)')
    elif cls:
        # This might not always work, if your form requires params,
        # pass an instance instead of a class!
        instance = cls()

    return html_output(
        instance,
        normal_row = u'<p%(html_class_attr)s>%(label)s %(field)s%(help_text)s</p>',
        error_row = u'%s',
        row_ender = '</p>',
        help_text_html = u' %s',
        errors_on_separate_row = True)

def as_div(instance=None, cls=None):
    "Returns this form rendered as HTML <div>s."
    if not instance and not cls:
        return TypeError('as_div takes at least 1 argument (0 given)')
    elif instance and cls:
        return TypeError('as_div takes at most 1 argument (2 given)')
    elif cls:
        # This might not always work, if your form requires params,
        # pass an instance instead of a class!
        instance = cls()

    return html_output(
        instance,
        normal_row = u'<div%(html_class_attr)s>%(label)s %(field)s%(help_text)s</div>',
        error_row = u'%s',
        row_ender = '</div>',
        help_text_html = u' %s',
        errors_on_separate_row = True)

def as_table(instance=None, cls=None):
    "Returns this form rendered as HTML <tr>s -- excluding the <table></table>."
    if not instance and not cls:
        return TypeError('as_table takes at least 1 argument (0 given)')
    elif instance and cls:
        return TypeError('as_table takes at most 1 argument (2 given)')
    elif cls:
        # This might not always work, if your form requires params,
        # pass an instance instead of a class!
        instance = cls()

    return html_output(
        instance,
        normal_row = u'<tr%(html_class_attr)s><th>%(label)s</th><td>%(errors)s%(field)s%(help_text)s</td></tr>',
        error_row = u'<tr><td colspan="2">%s</td></tr>',
        row_ender = u'</td></tr>',
        help_text_html = u'<br />%s',
        errors_on_separate_row = False)

def as_ul(instance=None, cls=None):
    "Returns this form rendered as HTML <li>s -- excluding the <ul></ul>."
    if not instance and not cls:
        return TypeError('as_ul takes at least 1 argument (0 given)')
    elif instance and cls:
        return TypeError('as_ul takes at most 1 argument (2 given)')
    elif cls:
        # This might not always work, if your form requires params,
        # pass an instance instead of a class!
        instance = cls()

    return html_output(
        instance,
        normal_row = u'<li%(html_class_attr)s>%(errors)s%(label)s %(field)s%(help_text)s</li>',
        error_row = u'<li>%s</li>',
        row_ender = '</li>',
        help_text_html = u' %s',
        errors_on_separate_row = False)

def html_output(form, normal_row, error_row, row_ender, help_text_html, errors_on_separate_row):
    "Helper function for outputting HTML. Used by as_table(), as_ul(), as_p()."
    top_errors = form.non_field_errors() # Errors that should be displayed above all fields.
    output, hidden_fields = [], []

    for name, field in form.fields.items():
        html_class_attr = ''
        bf = BoundField(form, field, name)
        bf_errors = form.error_class([conditional_escape(error) for error in bf.errors]) # Escape and cache in local variable.
        if bf.is_hidden:
            if bf_errors:
                top_errors.extend([u'(Hidden field %s) %s' % (name, force_unicode(e)) for e in bf_errors])
            hidden_fields.append(unicode(bf))
        else:
            # Create a 'class="..."' atribute if the row should have any
            # CSS classes applied.
            css_classes = bf.css_classes()
            if css_classes:
                html_class_attr = ' class="%s"' % css_classes

            if errors_on_separate_row:
                output.append(error_row % \
                              '{%% if form.%s.errors %%}{%% for error in form.%s.errors %%}{{ error }}{%% endfor %%}{%% endif %%}' \
                              % (name, name,))

            output.append(normal_row % {
                'errors': \
                  '{%% if form.%s.errors %%}{%% for error in form.%s.errors %%}{{ error }}{%% endfor %%}{%% endif %%}' \
                  % (name, name,),
                'label': '{{ form.%s.label_tag }}' % (name,),
                'field': '{{ form.%s }}' % (name,),
                'help_text': '',
                'html_class_attr': html_class_attr
            })

    if top_errors:
        output.insert(0,
                      r'{% if form.errors %}{% for field, error in form.errors %}(Hidden field {{ field }}) {{ error }}{% endfor %}{% end if %}'
        )

    if hidden_fields: # Insert any hidden fields in the last row.
        str_hidden = u'{%% for field in form.hidden_fields %%}{{ field }}{%% endfor %%}'
        if output:
            last_row = output[-1]
            # Chop off the trailing row_ender (e.g. '</td></tr>') and
            # insert the hidden fields.
            if not last_row.endswith(row_ender):
                # This can happen in the as_p() case (and possibly others
                # that users write): if there are only top errors, we may
                # not be able to conscript the last row for our purposes,
                # so insert a new, empty row.
                last_row = (normal_row % {'errors': '', 'label': '',
                                          'field': '', 'help_text':'',
                                          'html_class_attr': html_class_attr})
                output.append(last_row)
            output[-1] = last_row[:-len(row_ender)] + str_hidden + row_ender
        else:
            # If there aren't any rows in the output, just append the
            # hidden fields.
            output.append(str_hidden)
    return u'\n'.join(output)
