from profiles.views import ProfileDetailView, ProfileListView
from django.urls import path


profiles_patterns = ([
    path('', ProfileListView.as_view(), name="list"),
    path('<username>/', ProfileDetailView.as_view(), name="detail"),
], "profiles")
