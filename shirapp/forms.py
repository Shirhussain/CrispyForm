from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Snippet
from django.core.validators import RegexValidator

class NameWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        super().__init__([
            forms.TextInput(),
            forms.TextInput()
        ], attrs)

    # This one is counter part of the compres one that we have bellow to this class 
    def decompress(self, value):
        # the value is what ever the comprese function return is basicly 
        # first value and second value
        if value:
            return value.split(' ')
        return ['', '']
        # ['firstvalue', 'secondvalue]


# mulity value field 
# it means that if one field have money submfield we cat do it like this 
class NameField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+','Enter a valid first name (only leters')
            ]), # test
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+','Enter a valid second name (only letters')
            ]), # none
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        # data_list = ['test', 'none']
        return f'{data_list[0]} {data_list[1]}'
        # first value and second value with space in bettwen 




class ContactForm(forms.Form):
    name = NameField()
    email = forms.EmailField(label='E--Mail')
    category = forms.ChoiceField(choices =[('question','Question'),('other','Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = "post"  # it is the method that i gnna use in the backend.

        self.helper.layout = Layout(
            'name',
            'email',
            'category',
            'subject',
            'body',
            Submit('submit','submit', css_class='btn-success')
        )

    

class FormSnippet(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('name','body')
        
