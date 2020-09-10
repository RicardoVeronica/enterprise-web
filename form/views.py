from .forms import MyForm
from django.core.mail import EmailMessage
from django.urls import reverse
from django.shortcuts import redirect, render


def form(request):
    template = 'form/form.html'
    my_form = MyForm()
    context = {'form': my_form}

    if request.method == 'POST':
        my_form = MyForm(data=request.POST)

        if my_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            email = EmailMessage(
                "La Caffetiara: Nuevo mensaje",
                f"De {name} <{email}>\n\nEscribio:\n\n{content}",
                "no-contestar@inbox.mailtrap.io",
                ["setcain.ad@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('form') + "?ok")
            except Exception:
                return redirect(reverse('form') + "?fail")

    return render(request, template, context)
