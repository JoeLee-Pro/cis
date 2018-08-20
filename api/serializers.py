from rest_framework import serializers
from api.models import *


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('Id', 'LastName', 'FirstName', 'MiddleName', 'Birthday', 'Anniversary')


class ContactTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactTypes
        fields = ('Id', 'Type', 'Description')


class ContactEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactEntries
        fields = ('Id', 'PeopleId', 'ContactTypeId', 'Address', 'City', 'State', 'Zip', 'Phone', 'Email')

class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups


class GroupMembersSerializer(serializers.ModelSerializer):
    PeopleId = PeopleSerializer()
    GroupId = GroupsSerializer()
    class Meta:
        model = GroupMembers
        fields = ('Id', 'PeopleId', 'GroupId')
