from django.urls import include, re_path
from lists import views as list_views
from lists import urls as list_urls

urlpatterns = [
    # path("admin/", admin.site.urls),
    re_path(r"^$", list_views.home_page, name="home"),
    re_path(r"^lists/", include(list_urls)),
]
