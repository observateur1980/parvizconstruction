from django.contrib.sites import requests
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from home.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
class Home(TemplateView):
    template_name = 'home/home.html'


class Gallery(TemplateView):
    template_name = 'home/gallery.html'


class Project(TemplateView):
    template_name = 'home/project.html'


class Video(TemplateView):
    template_name = 'home/video.html'

class Kitchen(TemplateView):
    template_name = 'home/kitchen.html'

class GetQuote(TemplateView):
    template_name = 'home/getquote.html'


class Contact(FormView):
    template_name = 'home/contact.html'
    success_url = 'success_sent'
    form_class = ContactForm

    def get_context_data(self, *args, **kwargs):
        context = super(Contact, self).get_context_data(*args, **kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        structure = form.cleaned_data['structure']
        if structure == '1':
            structure = 'Choose Structure'
        elif structure == '2':
            structure = 'Sunroom'
        elif structure == '3':
            structure = 'Retractable Pergola'
        elif structure == '4':
            structure = 'Louvered Roof'

        message = form.cleaned_data['message']
        final_message = 'Name: ' + name + '\n' + 'Phone: ' + phone + '\n' + 'Email: ' + email + '\n' + structure + '\n' + message
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['info@parvizconstruction.com', ]
        send_mail('some data', final_message, email_from, recipient_list)
        return super(Contact, self).form_valid(form)

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


class Contact_Local(FormView):
    template_name = 'home/contact_local.html'
    success_url = 'success_sent'
    form_class = ContactForm

    def get_context_data(self, *args, **kwargs):
        context = super(Contact_Local, self).get_context_data(*args, **kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        structure = form.cleaned_data['structure']
        if structure == '1':
            structure = 'Choose Structure'
        elif structure == '2':
            structure = 'Sunroom'
        elif structure == '3':
            structure = 'Retractable Pergola'
        elif structure == '4':
            structure = 'Louvered Roof'

        message = form.cleaned_data['message']
        final_message = 'Name: ' + name + '\n' + 'Phone: ' + phone + '\n' + 'Email: ' + email + '\n' + structure + '\n' + message
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['info@parvizconstruction.com', ]
        send_mail('data from parvizconstruction.com', final_message, email_from, recipient_list)
        return super(Contact_Local, self).form_valid(form)

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


class LouveredRoof(FormView):
    template_name = 'home/louveredroof.html'
    success_url = 'success_sent'
    form_class = ContactForm

    def get_context_data(self, *args, **kwargs):
        context = super(LouveredRoof, self).get_context_data(*args, **kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        structure = form.cleaned_data['structure']
        if structure == '1':
            structure = 'Choose Structure'
        elif structure == '2':
            structure = 'Sunroom'
        elif structure == '3':
            structure = 'Retractable Pergola'
        elif structure == '4':
            structure = 'Louvered Roof'

        message = form.cleaned_data['message']
        final_message = 'Name: ' + name + '\n' + 'Phone: ' + phone + '\n' + 'Email: ' + email + '\n' + structure + '\n' + message
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['info@parvizconstruction.com', ]
        send_mail('data from parvizconstruction.com', final_message, email_from, recipient_list)
        return super(LouveredRoof, self).form_valid(form)

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


class Sunroom(FormView):
    template_name = 'home/sunroom.html'
    success_url = 'success_sent'
    form_class = ContactForm

    def get_context_data(self, *args, **kwargs):
        context = super(Sunroom, self).get_context_data(*args, **kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        structure = form.cleaned_data['structure']
        if structure == '1':
            structure = 'Choose Structure'
        elif structure == '2':
            structure = 'Sunroom'
        elif structure == '3':
            structure = 'Retractable Pergola'
        elif structure == '4':
            structure = 'Louvered Roof'

        message = form.cleaned_data['message']
        final_message = 'Name: ' + name + '\n' + 'Phone: ' + phone + '\n' + 'Email: ' + email + '\n' + structure + '\n' + message
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['info@parvizconstruction.com', ]
        send_mail('some data', final_message, email_from, recipient_list)
        return super(Sunroom, self).form_valid(form)

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


class SuccessSent(TemplateView):
    template_name = 'home/success_sent.html'


class WorkFlow(TemplateView):
    template_name = 'home/workflow.html'


class Retractable(FormView):
    template_name = 'home/retractable.html'
    success_url = 'success_sent'
    form_class = ContactForm

    def get_context_data(self, *args, **kwargs):
        context = super(Retractable, self).get_context_data(*args, **kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        structure = form.cleaned_data['structure']
        if structure == '1':
            structure = 'Choose Structure'
        elif structure == '2':
            structure = 'Sunroom'
        elif structure == '3':
            structure = 'Retractable Pergola'
        elif structure == '4':
            structure = 'Louvered Roof'

        message = form.cleaned_data['message']
        final_message = 'Name: ' + name + '\n' + 'Phone: ' + phone + '\n' + 'Email: ' + email + '\n' + structure + '\n' + message
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['info@parvizconstruction.com', ]
        send_mail('some data', final_message, email_from, recipient_list)
        return super(Retractable, self).form_valid(form)

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


class WinDoor(FormView):
    template_name = 'home/win-door.html'
    success_url = 'success_sent'
    form_class = ContactForm

    def get_context_data(self, *args, **kwargs):
        context = super(WinDoor, self).get_context_data(*args, **kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        structure = form.cleaned_data['structure']
        if structure == '1':
            structure = 'Choose Structure'
        elif structure == '2':
            structure = 'Sunroom'
        elif structure == '3':
            structure = 'Retractable Pergola'
        elif structure == '4':
            structure = 'Louvered Roof'

        message = form.cleaned_data['message']
        final_message = 'Name: ' + name + '\n' + 'Phone: ' + phone + '\n' + 'Email: ' + email + '\n' + structure + '\n' + message
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['info@parvizconstruction.com', ]
        send_mail('some data', final_message, email_from, recipient_list)
        return super(WinDoor, self).form_valid(form)

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


class Sunshade(FormView):
    template_name = 'home/sunshade.html'
    success_url = 'success_sent'
    form_class = ContactForm

    def get_context_data(self, *args, **kwargs):
        context = super(Sunshade, self).get_context_data(*args, **kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        structure = form.cleaned_data['structure']
        if structure == '1':
            structure = 'Choose Structure'
        elif structure == '2':
            structure = 'Sunroom'
        elif structure == '3':
            structure = 'Retractable Pergola'
        elif structure == '4':
            structure = 'Louvered Roof'

        message = form.cleaned_data['message']
        final_message = 'Name: ' + name + '\n' + 'Phone: ' + phone + '\n' + 'Email: ' + email + '\n' + structure + '\n' + message
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['info@parvizconstruction.com', ]
        send_mail('some data', final_message, email_from, recipient_list)
        return super(Sunshade, self).form_valid(form)

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)



from django.http import HttpResponse
from django.contrib.gis.geoip2 import GeoIP2




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