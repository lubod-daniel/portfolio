from django.urls import path
from . import views
from django.conf.urls import handler404

handler404='folioappp.views.custom_404'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('portfolio/<int:project_id>/', views.portfolio_details, name='portfolio_details'),
    path('send_email/', views.send_email, name='send_email'),
    path('leave-message/', views.leave_message, name='leave_message'),
    path('leave-message/thanks.html', views.thanks_page, name='thanks_page'),
    path('all_message/', views.all_messages, name='all_messages'),
    path('download/<str:filename>', views.download_file, name='download'),
    #path('404/', views.custom_404, name='404'),
    path('add_testimonial/appreciation.html', views.appreciation_page, name='appreciation_page'),
    path('add_testimonial/', views.add_testimonial, name='add_testimonial'),
    ]