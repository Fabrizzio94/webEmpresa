from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # redireccion
            email_message = EmailMessage(
                    "La Cafeteria: Nuevo mensaje de contacto", # Asunto
                    "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content), #Cuerpo
                    "no-contestar@inbox.mailtrap.io", #Email_origen
                    ['gmail.com- SMTP'],# Email_destino
                    reply_to=[email]
                    )
            try:
                    email_message.send()
                    #Todo ha ido bien, redireccionamos a ok
                    return redirect(reverse('contact')+'?ok')
            except:
                    #Algo a saliido mal, redireccionamos fail
                    return redirect(reverse('contact')+'?fail')
        # return redirect(reverse('contact')+'?ok')
    return render(request, "contact/contact.html", {'form': contact_form})