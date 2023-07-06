from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.core.mail import send_mail
from .forms import VisitorMessageForm
from django.http import Http404

# Create your views here.

def homepage(rqt):
    projects = project.objects.all()
    qualifications=qualification.objects.all()
    employments = employment.objects.all()
    professional_courses=professional_course.objects.all()
    context = {
        'projects': projects,
        'qualifications':qualifications,
        'employments': employments,
        'professional_courses':professional_courses,
        
    }
    return render(rqt, 'homepage.html', context)

def portfolio_details(request, portfolio_id):
    portfolio_id=1
    portfolio = get_object_or_404(project, pk=portfolio_id)
    context = {'portfolio': portfolio}
    
    return render(request, 'portfolio_details.html', context)
    
def send_email(request):
    recipient_email = 'daniel-lubod@outlook.com'
    subject = 'Hello World'
    body = 'This is the body of the email'

    mailto_link = f"mailto:{recipient_email}?subject={subject}&body={body}"
    
    return render(request, 'send_email.html', {'mailto_link': mailto_link})

def leave_message(request):
    if request.method == 'POST':
        form = VisitorMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'message.html', {'form': form, 'show_modal': True})  # Redirect to a thank you page
    else:
        form = VisitorMessageForm()
    
    return render(request, 'message.html', {'form': form, 'show_modal': False})

    
def thanks_page(request):
    return render(request, 'thanks.html')
