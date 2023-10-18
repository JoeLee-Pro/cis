from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class People(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    LastName = models.CharField(max_length=40, db_column='LastName', unique=False, verbose_name='Last Name')
    FirstName = models.CharField(max_length=40, db_column='FirstName', unique=False, verbose_name='First Name')
    MiddleName = models.CharField(max_length=40, db_column='MiddleName', unique=False, blank=True, null=True, verbose_name='Middle Name')
    Birthday = models.DateField(db_column='Birthday', unique=False, blank=True, null=True, verbose_name='Birthday')
    Anniversary = models.DateField(db_column='Anniversary', unique=False, blank=True, null=True, verbose_name='Anniversary')
                                
    def __str__(self):
        fullName = self.FirstName + ' '
        if self.MiddleName is not None:
            fullName += self.MiddleName + ' '
        fullName += self.LastName
  
        return fullName
    
    class Meta:
        db_table = 'People'
        verbose_name_plural = 'People'
        ordering = ['LastName', 'FirstName',]


class ContactTypes(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    Type = models.CharField(max_length=30, db_column='Type', unique=False, verbose_name='Type')
    Description = models.CharField(max_length=254, db_column='Description', unique=False, blank=True, null=True, verbose_name='Description')
    
    def __str__(self):
        return self.Type
    
    class Meta:
        db_table='ContactTypes'
        verbose_name = 'Contact Type'
        verbose_name_plural = 'Contact Types'


class ContactEntries(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    PeopleId = models.ForeignKey(People, to_field='Id', verbose_name='People Id', on_delete=models.DO_NOTHING, related_name='CEPeopleId')
    ContactTypeId = models.ForeignKey(ContactTypes, to_field='Id', verbose_name='Contact Type Id', on_delete=models.DO_NOTHING, related_name='CEContactTypeId')
    Address = models.CharField(max_length=254, db_column='Address', unique=False, blank=True, null=True, verbose_name='Address')
    City = models.CharField(max_length=100, db_column='City', unique=False, blank=True, null=True, verbose_name='City')
    State = models.CharField(max_length=2, db_column='State', unique=False, blank=True, null=True, verbose_name='State')
    Zip = models.CharField(max_length=10, db_column='Zip', unique=False, blank=True, null=True, verbose_name='Zip')
    Phone = models.CharField(max_length=25, db_column='Phone', unique=False, blank=True, null=True, verbose_name='Phone')
    Email = models.EmailField(max_length=254, db_column='Email', unique=False, blank=True, null=True, verbose_name='Email')
    
    def __str__(self):
        fullAddress = self.Address + ', ' + self.City + ', ' + self.State + ' ' + self.Zip
        
        return fullAddress
    
    class Meta:
        db_table = 'ContactEntries'
        verbose_name = 'Contact Entry'
        verbose_name_plural = 'Contact Entries'


class Families(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    Surname = models.CharField(max_length=40, db_column='Surname', unique=False, blank=False, null=False)
    Address = models.CharField(max_length=254, db_column='Address', unique=False, blank=True, null=True, verbose_name='Address')
    City = models.CharField(max_length=100, db_column='City', unique=False, blank=True, null=True, verbose_name='City')
    State = models.CharField(max_length=2, db_column='State', unique=False, blank=True, null=True, verbose_name='State')
    Zip = models.CharField(max_length=10, db_column='Zip', unique=False, blank=True, null=True, verbose_name='Zip')
    Description = models.CharField(max_length=254, blank=True, null=True, db_column='Description')
    
    def __str__(self):
        return self.Description
    
    class Meta:
        db_table = 'Families'
        verbose_name = 'Family'
        verbose_name_plural = 'Families'


class FamilyRoles(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    Role = models.CharField(max_length=40, db_column='Role')
    Description = models.CharField(max_length=254, blank=True, null=True, db_column='Description')
    
    def __str__(self):
        return self.Role
    
    class Meta:
        db_table = 'FamilyRoles'
        verbose_name = 'Family Role'
        verbose_name_plural = 'Family Roles'


class FamilyMembers(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    PeopleId = models.ForeignKey(People, to_field='Id', verbose_name='People Id', on_delete=models.DO_NOTHING, related_name='FMPeopleId')
    FamilyId = models.ForeignKey(Families, to_field='Id', verbose_name='Family', on_delete=models.DO_NOTHING, related_name='FMFamilyId')
    FamilyRoleId = models.ForeignKey(FamilyRoles, to_field='Id', verbose_name='Family Roles', on_delete=models.DO_NOTHING, related_name='FMFamilyRoleId')
    
    def __str__(self):
        return self.PeopleId.FirstName + " " + self.PeopleId.LastName + ', the ' + self.FamilyRoleId.Role + ' of the ' + self.FamilyId.Surname + ' family'
    
    class Meta:
        db_table = 'FamilyMembers'
        verbose_name = 'Family Member'
        verbose_name_plural = 'Family Members'


class Departments(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    Name = models.CharField(max_length=40, db_column='Name')
    Description = models.CharField(max_length=254, blank=True, null=True, db_column='Description')
    
    def __str__(self):
        return self.Name
    
    class Meta:
        db_table = 'Departments'
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Grades(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    Grade = models.CharField(max_length=12, db_column='Grade')
    
    def __str__(self):
        return self.Grade
    
    class Meta:
        db_table = 'Grades'
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'


class GroupTypes(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    Type = models.CharField(max_length=40, db_column='Type')
    Description = models.CharField(max_length=254, blank=True, null=True, db_column='Description')
    
    def __str__(self):
        return self.Type
    
    class Meta:
        db_table = 'GroupTypes'
        verbose_name = 'Group Type'
        verbose_name_plural = 'Group Types'


class Groups(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    Name = models.CharField(max_length=40, db_column='Name')
    DepartmentId = models.ForeignKey(Departments, to_field='Id', verbose_name='Departments', on_delete=models.DO_NOTHING, related_name='GRDepartmentId')
    GroupTypeId = models.ForeignKey(GroupTypes, to_field='Id', verbose_name='Group Types', on_delete=models.DO_NOTHING, related_name='GRGroupTypeId')
    Description = models.CharField(max_length=254, blank=True, null=True, db_column='Description')
    
    def __str__(self):
        return self.Name
    
    class Meta:
        db_table = 'Groups'
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class GroupRoles(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    Role = models.CharField(max_length=40, db_column='Role')
    Description = models.CharField(max_length=254, blank=True, null=True, db_column='Description')
    
    def __str__(self):
        return self.Role
    
    class Meta:
        db_table = 'GroupRoles'
        verbose_name = 'Group Role'
        verbose_name_plural = 'Group Roles'


class GroupMembers(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    PeopleId = models.ForeignKey(People, to_field='Id', verbose_name='People Id', on_delete=models.DO_NOTHING, related_name='GMPeopleId')
    GroupId = models.ForeignKey(Groups, to_field='Id', verbose_name='Group', on_delete=models.DO_NOTHING, related_name='GMGroupId')
    GradeId = models.ForeignKey(Grades, to_field='Id', verbose_name='Grade', on_delete=models.DO_NOTHING, related_name='GMGradeId')
    GroupRoleId = models.ForeignKey(GroupRoles, to_field='Id', verbose_name='Group Roles', on_delete=models.DO_NOTHING, related_name='GMGroupRoleId')
    
    def __str__(self):
        return self.PeopleId.FirstName + " " + self.PeopleId.LastName + ', a ' + self.GroupRoleId.Role + ' of the ' + self.GroupId.Name + ' group'
    
    class Meta:
        db_table = 'GroupMembers'
        verbose_name = 'Group Member'
        verbose_name_plural = 'Group Members'


class PeopleNotes(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    PeopleId = models.ForeignKey(People, to_field='Id', verbose_name='People Id', on_delete=models.DO_NOTHING, related_name='PNPeopleId')
    Note = models.TextField(max_length=2048, blank=True, null=True, db_column='Note')

    class Meta:
        db_table = 'PeopleNotes'
        verbose_name = 'People Note'
        verbose_name_plural = 'People Notes'


class FamilyNotes(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    FamilyId = models.ForeignKey(Families, to_field='Id', verbose_name='Family', on_delete=models.DO_NOTHING, related_name='FNFamilyId')
    Note = models.TextField(max_length=2048, blank=True, null=True, db_column='Note')

    class Meta:
        db_table = 'FamilyNotes'
        verbose_name = 'Family Note'
        verbose_name_plural = 'Family Notes'


class GroupNotes(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    GroupId = models.ForeignKey(Groups, to_field='Id', verbose_name='Group', on_delete=models.DO_NOTHING, related_name='GNGroupId')
    Note = models.TextField(max_length=2048, blank=True, null=True, db_column='Note')

    class Meta:
        db_table = 'GroupNotes'
        verbose_name = 'Group Note'
        verbose_name_plural = 'Group Notes'

