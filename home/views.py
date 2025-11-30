from django.views.generic import TemplateView

from django.http import HttpResponse
from django.contrib.gis.geoip2 import GeoIP2

from .forms import LeadForm
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
import smtplib


# Create your views here.
class Home(TemplateView):
    template_name = 'home/home.html'


class Video(TemplateView):
    template_name = 'home/video.html'


class Gallery(TemplateView):
    template_name = 'home/gallery.html'


class Project(TemplateView):
    template_name = 'home/project.html'


class Designbuild(TemplateView):
    template_name = 'home/designbuild.html'


class Newconstruction(TemplateView):
    template_name = 'home/newconstruction.html'


class Kitchen(TemplateView):
    template_name = 'home/kitchen.html'


class Bathroom(TemplateView):
    template_name = 'home/bathroom.html'


class Garage(TemplateView):
    template_name = 'home/garage.html'


class Homeremodel(TemplateView):
    template_name = 'home/homeremodel.html'


class Homeadditions(TemplateView):
    template_name = 'home/homeadditions.html'


class Planspermits(TemplateView):
    template_name = 'home/planspermits.html'


class Fatjo(TemplateView):
    template_name = 'home/fatjo.html'


class Sjdowntown(TemplateView):
    template_name = 'home/sjdowntown.html'


class Laterrace(TemplateView):
    template_name = 'home/laterrace.html'


class Cheltenham(TemplateView):
    template_name = 'home/cheltenham.html'


class Piper(TemplateView):
    template_name = 'home/piper.html'


class Daves(TemplateView):
    template_name = 'home/daves.html'


def create_lead(request):
    if request.method == 'POST':
        lead_form = LeadForm(request.POST)
        if lead_form.is_valid():
            consultation_request = lead_form.save()

            # Prepare email content including selected consultation types
            consultation_types_display = consultation_request.get_consultation_types_display()
            full_message = (
                f"Name: {consultation_request.name}\n"
                f"Email: {consultation_request.email}\n"
                f"Phone: {consultation_request.phone}\n"
                f"Consultation Types: {consultation_types_display}\n\n"
                f"Message:\n{consultation_request.message}"
            )

            try:
                email_message = EmailMessage(
                    subject=f'Request Consultation from {consultation_request.name}',
                    body=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=['info@parvizconstruction.com'],
                )
                email_message.send(fail_silently=False)
                return redirect('home:create_lead_success')
            except smtplib.SMTPException:
                messages.error(request, 'There was an error sending your request. Please try again later.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        lead_form = LeadForm()

    return render(request, 'home/create_lead.html', {'lead_form': lead_form})


def create_lead_success(request):
    return render(request, 'home/createlead_success.html')


def get_client_ip(request):
    """Get real client IP even if behind proxy."""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def geoip_test(request):
    """Show detected IP + country for debugging."""
    ip = get_client_ip(request)
    g = GeoIP2()

    try:
        country_data = g.country(ip)
        country = country_data.get("country_code")
    except Exception as e:
        country = f"ERROR: {e}"

    return HttpResponse(f"""
        <h2>GeoIP Test</h2>
        <p><strong>Your IP:</strong> {ip}</p>
        <p><strong>Detected Country:</strong> {country}</p>
    """)
