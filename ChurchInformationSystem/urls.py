"""ChurchInformationSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  path(r'^blog/', include(blog_urls))
"""
from django.urls import include, re_path, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from api import views as api_views
from manager import views as manager_views
from website import views as website_views
from rest_framework import routers

router = routers.SimpleRouter()
#router.register(r'users', UserViewSet)
#router.register(r'accounts', AccountViewSet)

urlpatterns = [
    re_path(r'^$', website_views.home),
    re_path(r'^api-auth/', include('rest_framework.urls',)),
    re_path(r'^manager/home/', manager_views.home),
    re_path(r'^manager/generate_sunday_school_rolls', manager_views.generate_sunday_school_rolls),
    re_path(r'^api/v1/people/', api_views.get_people),
    re_path(r'^api/v1/groups/', api_views.get_groups),
    re_path(r'^api/v1/group_roles/', api_views.get_group_roles),
    re_path(r'^api/v1/contact_types/', api_views.get_contact_types),
    re_path(r'^api/v1/contact_entries/', api_views.get_contact_entries),
    re_path(r'^api/v1/group_members/', api_views.get_group_members),
    re_path(r'^api/v1/grades/', api_views.get_grades),
    re_path(r'^api/v1/youth_sermons/xml', api_views.youth_sermons_xml),
    re_path(r'^api/v1/youth_sermons/json', api_views.youth_sermons_json),
    re_path(r'^abundant-life-adults/', website_views.abundantlifeadults),
    re_path(r'^real-life-youth/', website_views.reallifeyouth),
    re_path(r'^kids-life-children/', website_views.kidslifechildren),
    re_path(r'^youth-sermon-library/page(?P<page>[0-9]+)/$', website_views.youthsermonlibrary),
    re_path(r'^beliefs/', website_views.beliefs),
    re_path(r'^mission-vision/', website_views.missionvision),
    re_path(r'^calendar/', website_views.calendar),
    re_path(r'^newsletters/', website_views.newsletters),
    re_path(r'^contact-directions/', website_views.contactdirections),
    re_path(r'^leadership/', website_views.leadership),
    re_path(r'^sermon-library', website_views.sermonlibrary),
    re_path(r'^unscripted-podcast', website_views.unscriptedpodcast),
    re_path(r'^admin/', admin.site.urls),
]

urlpatterns += router.urls

if settings.DEBUG is True:
    print("Media stuff: ")
    print(settings.MEDIA_URL)
    print(settings.MEDIA_ROOT)
    print(settings.DEBUG)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)