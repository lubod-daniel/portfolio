from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.core.mail import send_mail
from .forms import VisitorMessageForm
from django.http import Http404

# Create your views here.

def homepage(request):
    projects = project.objects.all()
    qualifications=qualification.objects.all()
    employments = employment.objects.all()
    professional_courses=professional_course.objects.all()
    testimonials = testimonial.objects.all()
    count=projects.count
    
    context = {
        'projects': projects,
        'qualifications':qualifications,
        'employments': employments,
        'professional_courses':professional_courses,
        'testimonials': testimonials,
        'count': count 
    }
    return render(request, 'homepage.html', context)
    
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

#def add_testimonial(request):
    if request.method == 'POST':
        form = testimonialform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = testimonialform()

    return render(request, 'add_testimonial.html', {'form': form})

#def all_testimonials(rqt):
    testimonials = testimonial.objects.all()
    context = {
        'testimonials': testimonials,    
     }
    return render(rqt, 'all_testimonials.html', context)

    
def thanks_page(request):
    return render(request, 'thanks.html')