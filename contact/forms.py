from django import forms


class ContactForm(forms.Form):
    """
    Contact form for contact app
    """
    name = forms.CharField(label='Name', required=True,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Write your name here'
                               }
                           ), min_length=3, max_length=25)

    email = forms.EmailField(label='Email', required=True,
                             widget=forms.EmailInput(
                                 attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Write your email here'
                                 }
                             ), min_length=10, max_length=100)

    content = forms.CharField(label='Content', required=True,
                              widget=forms.Textarea(
                                  attrs={
                                      'class': 'form-control',
                                      'rows': 3,
                                      'placeholder': 'Write your message here'
                                  }
                              ), min_length=10, max_length=800)
