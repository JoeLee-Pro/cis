from django.contrib import admin
from api.models import People, ContactEntries, ContactTypes
from api.models import Families, FamilyRoles, FamilyMembers
from api.models import Departments, Grades, Groups, GroupRoles, GroupTypes, GroupMembers
from api.models import PeopleNotes, FamilyNotes, GroupNotes


# Register your inline tables here.
class GroupMembersInline(admin.TabularInline):
    model = GroupMembers
    verbose_name_plural = "Group Membership"


class FamilyMembersInline(admin.TabularInline):
    model = FamilyMembers
    verbose_name_plural = "Family Membership"


class ContactEntriesInline(admin.TabularInline):
    model = ContactEntries


# Register your models here.
class PeopleAdmin( admin.ModelAdmin ):
    model = People
    list_display = ('FirstName', 'MiddleName', 'LastName', 'Birthday', 'Anniversary')
    search_fields = ('LastName', 'FirstName')
    ordering = ('LastName', 'FirstName',)
    list_per_page = 20

    inlines = [ContactEntriesInline, GroupMembersInline, FamilyMembersInline]
    pass

admin.site.register(People, PeopleAdmin)


class ContactTypesAdmin( admin.ModelAdmin ):
    model = ContactTypes
    list_display = ('Type', 'Description')
    search_fields = ('Type',)
    ordering = ('Type',)
    pass

admin.site.register(ContactTypes, ContactTypesAdmin)


class ContactEntriesAdmin( admin.ModelAdmin ):
    model = ContactEntries
    list_display = ('PeopleId', 'ContactTypeId', 'Address', 'City', 'State', 'Zip', 'Phone', 'Email')
    list_filter = ('PeopleId', 'ContactTypeId', 'City', 'State', 'Zip')
    search_fields = ('City', 'State', 'Phone', 'Email')
    ordering = ('ContactTypeId',)
    pass

admin.site.register(ContactEntries, ContactEntriesAdmin)


class FamiliesAdmin( admin.ModelAdmin ):
    model = Families
    list_display = ('Surname', 'Description')
    list_filter = ('Surname',)
    search_fields = ('Surname',)
    ordering = ('Surname',)
    inlines = [FamilyMembersInline]

    pass

admin.site.register(Families, FamiliesAdmin)


class FamilyRolesAdmin( admin.ModelAdmin ):
    model = FamilyRoles
    list_display = ('Role', 'Description')
    search_fields = ('Role',)
    ordering = ('Role',)
    pass

admin.site.register(FamilyRoles, FamilyRolesAdmin)


class FamilyMembersAdmin( admin.ModelAdmin ):
    model = FamilyMembers
    list_display = ('PeopleId', 'FamilyId', 'FamilyRoleId')
    list_filter = ('FamilyId', 'FamilyRoleId')
    search_fields = ('PeopleId', 'FamilyId', 'FamilyRoleId')
    ordering = ('PeopleId',)

    pass

admin.site.register(FamilyMembers, FamilyMembersAdmin)


class DepartmentsAdmin( admin.ModelAdmin ):
    model = Departments
    list_display = ('Name', 'Description')
    search_fields = ('Name',)
    ordering = ('Name',)
    pass

admin.site.register(Departments, DepartmentsAdmin)


class GradesAdmin( admin.ModelAdmin ):
    model = Grades
    list_display = ('Grade',)
    search_fields = ('Grade',)
    ordering = ('Grade',)
    pass

admin.site.register(Grades, GradesAdmin)


class GroupTypesAdmin( admin.ModelAdmin ):
    model = GroupTypes
    list_display = ('Type', 'Description')
    search_fields = ('Type',)
    ordering = ('Type',)
    pass

admin.site.register(GroupTypes, GroupTypesAdmin)

class GroupsAdmin( admin.ModelAdmin ):
    model = Groups
    list_display = ('Name', 'GroupTypeId', 'Description')
    list_filter = ('GroupTypeId',)
    search_fields = ('Name',)
    ordering = ('Name',)
    
    inlines = [GroupMembersInline]
    pass

admin.site.register(Groups, GroupsAdmin)


class GroupRolesAdmin( admin.ModelAdmin ):
    model = GroupRoles
    list_display = ('Role', 'Description')
    search_fields = ('Role',)
    ordering = ('Role',)
    pass

admin.site.register(GroupRoles, GroupRolesAdmin)


class GroupMembersAdmin( admin.ModelAdmin ):
    model = GroupMembers
    list_display = ('PeopleId', 'GroupId', 'GradeId', 'GroupRoleId')
    list_editable = ('GroupId', 'GradeId', 'GroupRoleId')
    list_filter = ('GroupId', 'GradeId', 'GroupRoleId', 'PeopleId')
    #search_fields = ('PeopleId_id',)
    ordering = ('PeopleId',)
    list_per_page=20
    pass

admin.site.register(GroupMembers, GroupMembersAdmin)


class PeopleNotesAdmin( admin.ModelAdmin ):
    model = PeopleNotes
    list_display = ('PeopleId', 'Note')
    list_filter = ('PeopleId',)
    search_fields = ('PeopleId', 'Note')
    pass

admin.site.register(PeopleNotes, PeopleNotesAdmin)


class FamilyNotesAdmin( admin.ModelAdmin ):
    model = FamilyNotes
    list_display = ('FamilyId', 'Note')
    list_filter = ('FamilyId',)
    search_fields = ('FamilyId', 'Note')
    pass

admin.site.register(FamilyNotes, FamilyNotesAdmin)


class GroupNotesAdmin( admin.ModelAdmin ):
    model = GroupNotes
    list_display = ('GroupId', 'Note')
    list_filter = ('GroupId',)
    search_fields = ('GroupId', 'Note')
    pass

admin.site.register(GroupNotes, GroupNotesAdmin)


