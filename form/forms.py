from django import forms


class MyForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True,
                           widget=forms.TextInput(
                               attrs={
                                   "class": "form-control",
                                   "placeholder": "Escribe tu nombre",
                               }
                           ), min_length=3, max_length=50)

    email = forms.EmailField(label="Email", required=True,
                             widget=forms.EmailInput(
                                 attrs={
                                   "class": "form-control",
                                   "placeholder": "Escribe tu email",
                                 }
                             ), min_length=6, max_length=150)

    content = forms.CharField(label="Mensaje", required=True,
                              widget=forms.Textarea(
                                  attrs={
                                      "class": "form-control",
                                      "placeholder": "Escribe tu mensaje",
                                      "rows": 3,
                                  }
                              ), min_length=1, max_length=500)
