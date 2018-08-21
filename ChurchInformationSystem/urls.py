"""ChurchInformationSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
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
    url(r'^$', website_views.home),
    url(r'^api-auth/', include('rest_framework.urls',)),
    url(r'^manager/home/', manager_views.home),
    url(r'^manager/generate_sunday_school_rolls', manager_views.generate_sunday_school_rolls),
    url(r'^api/v1/people/', api_views.get_people),
    url(r'^api/v1/groups/', api_views.get_groups),
    url(r'^api/v1/group_roles/', api_views.get_group_roles),
    url(r'^api/v1/contact_types/', api_views.get_contact_types),
    url(r'^api/v1/contact_entries/', api_views.get_contact_entries),
    url(r'^api/v1/group_members/', api_views.get_group_members),
    url(r'^api/v1/grades/', api_views.get_grades),
    url(r'^api/v1/youth_sermons/xml', api_views.youth_sermons_xml),
    url(r'^api/v1/youth_sermons/json', api_views.youth_sermons_json),
    url(r'^abundant-life-adults/', website_views.abundantlifeadults),
    url(r'^real-life-youth/', website_views.reallifeyouth),
    url(r'^kids-life-children/', website_views.kidslifechildren),
    url(r'^youth-sermon-library/page(?P<page>[0-9]+)/$', website_views.youthsermonlibrary),
    url(r'^beliefs/', website_views.beliefs),
    url(r'^mission-vision/', website_views.missionvision),
    url(r'^calendar/', website_views.calendar),
    url(r'^newsletters/', website_views.newsletters),
    url(r'^contact-directions/', website_views.contactdirections),
    url(r'^leadership/', website_views.leadership),
    url(r'^sermon-library', website_views.sermonlibrary),
    url(r'^unscripted-podcast', website_views.unscriptedpodcast),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += router.urls

if settings.DEBUG is True:
    print("Media stuff: ")
    print(settings.MEDIA_URL)
    print(settings.MEDIA_ROOT)
    print(settings.DEBUG)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)