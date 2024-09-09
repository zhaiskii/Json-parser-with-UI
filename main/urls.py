from django.urls import path


from . import views


urlpatterns = [
    path("", views.basic),
    path("first/", views.first, name="first"), # why we do naming
    path("second/", views.second, name="second"),  # why we do naming
    path("third/", views.third, name="third"),  # why we do naming
    path("fourth/", views.fourth, name="fourth"),  # why we do naming
    path("fifth/", views.fifth, name="fifth"),  # why we do naming
    path("sixth/", views.sixth, name="sixth"),  # why we do naming
    path("seventh/", views.seventh, name="seventh"),  # why we do naming
    path("eighth/", views.eighth, name="eighth"),  # why we do naming
    path("ninth/", views.ninth, name="ninth"),  # why we do naming
    path("tenth/", views.tenth, name="tenth"),
    path("eleventh/", views.eleventh, name="eleventh"),
    path("twelfth/", views.twelfth, name="twelfth"),
    path("thirtieth/", views.thirtieth, name="thirtieth"),
]