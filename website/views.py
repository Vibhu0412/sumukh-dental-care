from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings as conf_settings


def home(request):
    return render(request, 'website/home.html')


def about(request):
    return render(request, 'website/about.html')


def service(request):
    return render(request, 'website/service.html')


# def pricing(request):
#     return render(request, 'website/pricing.html')
#
#
# def blog(request):
#     return render(request, 'website/blog.html')
#
#
# def blog_details(request):
#     return render(request, 'website/blog_details.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['message_name']
        email = request.POST['message_email']
        message = request.POST['message']
        phone = request.POST['message_phone']

        if not name or not email or not phone or not message:
            return HttpResponse("All fields are required.", status=400)

        # send email to default address
        send_mail(
            'Follow up required for - ' + name,
            f"Message: {message}\n\nPhone: {phone}\n\nContact email: {email}",
            email,
            [conf_settings.CONTACT_US_FORM_EMAIL_TO],
            fail_silently=False,
        )

        messages.success(request,
                         f'Hi {name},Thanks for contacting us. We will follow up with you within next few business days.')
        return redirect('contact')
    else:
        return render(request, 'website/contact.html')
