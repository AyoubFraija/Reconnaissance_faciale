from django.urls import path
from pages import views

urlpatterns = [
    path("", views.login_page, name="login_page"),
    path("seconnecter/", views.seconnecter, name="seconnecter"),
    path("inscription_1/", views.inscription_1, name="inscription_1"),
    path("home/<str:username>/", views.home, name="home"),
    path("inscription/", views.inscription, name="inscription"),
    path("inscription_2/",views.inscription_2,name="inscription_2"),
    path("scan/",views.scan,name="scan"),
    path("train/",views.train,name="train"),
    path("detection_page/",views.detection_page,name="detection_page"), 
    path("detection/",views.detection,name="detection"),
    path("deconnecter/",views.deconnecter,name="deconnecter")
]
    