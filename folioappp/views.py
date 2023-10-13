from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from .models import *
from django.core.mail import send_mail
from .forms import VisitorMessageForm, TestimonialForm
from django.http import Http404, FileResponse, HttpResponseNotFound
from django.conf import settings
import os
import mimetypes
# Create your views here.

def homepage(request):
    projects = project.objects.all()
    qualifications=qualification.objects.all()
    employments = employment.objects.all()
    dev_employments = dev_employment.objects.all()
    professional_courses=professional_course.objects.all()
    testimonials = testimonial.objects.all()
    count=projects.count
    
    context = {
        'projects': projects,
        'qualifications':qualifications,
        'employments': employments,
        'professional_courses':professional_courses,
        'testimonials': testimonials,
        'count': count,
        'dev_employments': dev_employments
    }
    return render(request, 'homepage.html', context)

def acc_homepage(request):
    projec = project.objects.all()
    qualificatio=qualification.objects.all()
    employmen = employment.objects.all()
    dev_employmen = dev_employment.objects.all()
    professional_cours=professional_course.objects.all()
    testimonia = testimonial.objects.all()
    
    context = {
        'projec': projec,
        'qualificatio':qualificatio,
        'employmen': employmen,
        'professional_cours':professional_cours,
        'testimonia': testimonia,
        'dev_employmen': dev_employmen
    }
    return render(request, 'acc_homepage.html', context)
    
def portfolio_details(request, project_id):
    portfolio = get_object_or_404(project, pk=project_id)
    pictures=more_image.objects.filter(identifier=portfolio.identifier)
    pictures=more_image.objects.filter(project=portfolio)

    context = {'portfolio': portfolio,
               'pictures': pictures,

                }
    return render(request, 'portfolio_details.html', context)
    
def send_email(request):
    recipient_email = 'daniel-lubod@outlook.com'
    subject = 'Hello Daniel'
    body = 'This is the body of the email'

    mailto_link = f"mailto:{recipient_email}?subject={subject}&body={body}"
    
    return render(request, 'send_email.html', {'mailto_link': mailto_link})

def leave_message(request):
    if request.method == 'POST':
        form = VisitorMessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Save the message to the database
            visitor_message = VisitorMessage(name=name, email=email, message=message)
            visitor_message.save()

            return redirect('thanks_page')  # Redirect to "thanks.html" page after successful submission
    else:
        form = VisitorMessageForm()

    return render(request, 'message.html', {'form': form})

def all_messages(rqt):
    messages = VisitorMessage.objects.all()
    context = {
        'messages': messages,    
     }
    return render(rqt, 'all_messages.html', context)

def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            remark = form.cleaned_data['remark']
            name = form.cleaned_data['name']
            position = form.cleaned_data['position']
            organization = form.cleaned_data['organization']

            # Save the message to the database
            testimonial_mes = testimonial(remark=remark, name=name, position=position, organization=organization,)
            testimonial_mes.save()

            return redirect('appreciation_page')
    else:
        form = TestimonialForm()

    return render(request, 'add_testimonial.html', {'form': form})
    
def thanks_page(request):
    return render(request, 'thanks.html')

def appreciation_page(request):
    return render(request, 'appreciation.html')

def download_file(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/folioappp/static/folio/files/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'homepage.html')
    
#def download_file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, '/folioappp/static/folio/files/', filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = FileResponse(file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
    else:
       return render(request, 'homepage.html')
    
def custom_404(request, exception):
    previous_page = request.META.get('HTTP_REFERER', '/')
    context={
        'previous_page':previous_page,
    }
    return render(request, '404.html', context, status=404)
