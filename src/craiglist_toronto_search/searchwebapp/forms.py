"""
Creates the form that we display on our website.
This is the format of the text we take in.
"""

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class QueryForm(forms.Form):
    search = forms.CharField()
    # given from craigslist website
    category = forms.ChoiceField(choices=[
        ('sss', 'for sale'),
        ('hhh', 'housing'),
        ('ccc', 'community'),
        ('bbb', 'services'),
        ('jjj', 'jobs'),
        ('ggg', 'gigs'),
        ('rrr', 'resumes'),
    ])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'

        # submit button is bootstrap css
        self.helper.layout = Layout(
            'search',
            'category',
            Submit('submit', 'Submit', css_class='btn-success')
        )
