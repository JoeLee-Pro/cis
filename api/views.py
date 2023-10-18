from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from api.models import *
from api.serializers import *
from urllib.parse import quote

import json
import glob
from django.core import serializers


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class XMLResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = XMLRenderer().render(data)
        kwargs['content_type'] = 'application/xml'
        super(XMLResponse, self).__init__(content, **kwargs)


def get_people(request):
    # people_as_json = serializers.serialize('json', People.objects.all())
    people = People.objects.all()
    people_serializer = PeopleSerializer(people, many=True)

    return JSONResponse(people_serializer.data)
    #return HttpResponse(people_as_json, content_type='json')


def get_groups(request):
    groups_as_json = serializers.serialize('json', Groups.objects.all())

    return HttpResponse(groups_as_json, content_type='json')


def get_group_roles(request):
    group_roles_as_json = serializers.serialize('json', GroupRoles.objects.all())

    return HttpResponse(group_roles_as_json, content_type='json')


def get_grades(request):
    grades_as_json = serializers.serialize('json', Grades.objects.all())

    return HttpResponse(grades_as_json, content_type='json')


def get_contact_types(request):
    contact_types = ContactTypes.objects.all()
    contact_types_serializer = ContactTypesSerializer(contact_types, many=True)

    return JSONResponse(contact_types_serializer.data)


def get_contact_entries(request):
    contact_entries = ContactEntries.objects.all()
    contact_entries_serializer = ContactEntriesSerializer(contact_entries, many=True)

    return JSONResponse(contact_entries_serializer.data)


def get_group_members(request):
    group_members = GroupMembers.objects.all()
    group_members_serializer = GroupMembersSerializer(group_members, many=True)

    return JSONResponse(group_members_serializer.data)


def get_youth_sermons():
    sermon_path_list = glob.glob("/home/joe/media/audio/*")
    sermon_names = []

    print(sermon_path_list)
    for sermon in sermon_path_list:
        sermon_pieces = sermon.split("/")
        sermon_name = sermon_pieces[5]
        if sermon_name.endswith("\n"):
            sermon_name = sermon_name[:-1]
        sermon_names.append(sermon_name)

    sermon_names.sort(reverse=True)
    print(sermon_names)
    sermon_list = []
    for sermon in sermon_names:
        sermon_information = {}
        sermon_month = sermon[5:7]
        sermon_day = sermon[8:10]
        sermon_year = sermon[:4]
        sermon_date = sermon_month + '/' + sermon_day + '/' + sermon_year
        sermon_title = sermon[11:-4]
        sermon_information['date'] = sermon_date
        sermon_information['title'] = sermon_title
        sermon_information['path'] = 'http://tricountynaz.net/media/audio/' + quote(sermon)
        sermon_list.append(sermon_information)

    return sermon_list


def youth_sermons_xml(request):
    sermon_list = get_youth_sermons()

    return XMLResponse(sermon_list)


def youth_sermons_json(request):
    sermon_list = get_youth_sermons()

    return JSONResponse(sermon_list)

