from django.urls import re_path
from lists import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    re_path(r"^$", views.home_page, name="home"),
    # path("", views.home_page, name="home"),
    re_path(r"^lists/new$", views.new_list, name="new_list"),
    # path("lists/new", views.new_list, name="new_list"),
    re_path(r"^lists/(.+)/$", views.view_list, name="view_list"),
]
