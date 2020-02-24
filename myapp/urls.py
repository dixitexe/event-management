from django.urls import path
from . import views
print("myapp urls called")
urlpatterns = [
    path('',views.index,name='index'),
    path('sports/',views.sports,name='sports'),
    path('concerts/',views.concerts,name='concerts'),
    path('political/',views.political,name='political'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('signup_user/',views.signup_user,name='signup_user'),
    path('login_user/',views.login_user,name='login_user'),
    path('logout/',views.logout,name='logout'),
    path('validate_otp/',views.validate_otp,name='validate_otp'),
    path('submit_contact/',views.submit_contact,name='submit_contact'),
    path('resend_otp/<int:pk>/',views.resend_otp,name='resend_otp'),
    path('event_detail/<int:pk>/',views.event_detail,name='event_detail'),
    path('book_event/<int:pk1>/<int:pk2>/',views.book_event,name='book_event'),
    path('myevent/<int:pk>/',views.myevent,name='myevent'),
    path('cancel_event/<int:pk>/',views.cancel_event,name='cancel_event'),
]