from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,Field, HTML
from django.urls import reverse



class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper=FormHelper()
        self.helper.form_method="POST"
        self.helper.layout=Layout(
            'username',
            'password',
            HTML("<p class='mt-3'>Don't have an account? <a href='{}'>Register here</a>.</p>".format(reverse('main:register'))),
            Submit('submit', 'Log in',css_class='mt-2')
        )


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.helper = FormHelper()
        self.helper.form_method="POST"
        self.helper.layout = Layout(
            'username',
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'email',
            'password1',
            'password2',
            HTML('<p class="mt-3">Already have an account? <a href="{}">Log in here</a>.</p>'.format(reverse('main:login'))),
            Submit('submit', 'Register',css_class='mt-2')
        )


