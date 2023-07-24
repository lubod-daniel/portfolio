from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('portfolio/<int:portfolio_id>/', views.portfolio_details, name='portfolio_details'),
    path('send_email/', views.send_email, name='send_email'),
    path('leave-message/', views.leave_message, name='leave_message'),
    path('leave-message/thanks.html', views.thanks_page, name='thanks_page'),
    path('all_message/', views.all_messages, name='all_messages'),
]