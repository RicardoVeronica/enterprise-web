from .forms import ContactForm
from django.urls import reverse
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage


def contact(request):
    """
    Contact view with form
    """
    print(f'My debugger: REQUEST METHOD {request.method}')

    template = 'contact/contact.html'
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            # send email and redirect
            email = EmailMessage(
                "La Caffetiara: Nuevo mensaje",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["setcain.ad@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('contact_url')+'?ok')
            except Exception:
                return redirect(reverse('contact_url')+'?fail')

    return render(request, template, {'form': contact_form})
