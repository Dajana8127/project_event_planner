from django.urls import path
from .views.event_views import Events, EventDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
	# Restful routing
    path('events/', Events.as_view(), name='events'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
