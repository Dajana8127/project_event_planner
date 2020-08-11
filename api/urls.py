from django.urls import path
from .views.event1_views import Events, EventDetail
from .views.rsvp_views import RSVPs, RSVPDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
	# Restful routing
    path('events/', Events.as_view(), name='events'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event1_detail'),
    path('rsvps/', RSVPs.as_view(), name='rsvps'),
    path('rsvps/<int:pk>/', RSVPDetail.as_view(), name='rsvp_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password')
]
