from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class QueryForm(forms.Form):
    search = forms.CharField()
    category = forms.ChoiceField(choices=[
        ('sss', 'for sale'),
        ('hhh', 'housing'),
    ])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'search',
            'category',
            Submit('submit', 'Submit', css_class='btn-success')
        )
