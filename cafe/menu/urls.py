from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu),
    path("search/", views.search, name="Search"),
    path("feedback/", views.feedback, name="Feedback"),
    path("showdata/", views.showdata),
    path("about/", views.about),
    path("SeeFeedback/", views.SeeFeedback),
    path("OtherFeedback/", views.OtherFeedback),
    path("<str:name>/",views.singlecategory),
    ]
