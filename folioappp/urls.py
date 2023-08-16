from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('portfolio/<int:project_id>/', views.portfolio_details, name='portfolio_details'),
    path('send_email/', views.send_email, name='send_email'),
    path('leave-message/', views.leave_message, name='leave_message'),
    path('leave-message/thanks.html', views.thanks_page, name='thanks_page'),
    path('all_message/', views.all_messages, name='all_messages'),
    path('download/<str:filename>', views.download_file, name='download'),

    
    #path('add_testimonial/', views.add_testimonial, name='add_testimonial'),
    #path('all_testimonial/', views.all_testimonials, name='all_testimonials'),
]