# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactEntries',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('Address', models.CharField(null=True, verbose_name='Address', max_length=254, db_column='Address', blank=True)),
                ('City', models.CharField(null=True, verbose_name='City', max_length=100, db_column='City', blank=True)),
                ('State', models.CharField(null=True, verbose_name='State', max_length=2, db_column='State', blank=True)),
                ('Zip', models.CharField(null=True, verbose_name='Zip', max_length=10, db_column='Zip', blank=True)),
                ('Phone', models.CharField(null=True, verbose_name='Phone', max_length=25, db_column='Phone', blank=True)),
                ('Email', models.EmailField(null=True, verbose_name='Email', max_length=254, db_column='Email', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Entries',
                'verbose_name': 'Contact Entry',
                'db_table': 'ContactEntries',
            },
        ),
        migrations.CreateModel(
            name='ContactTypes',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('Type', models.CharField(verbose_name='Type', max_length=30, db_column='Type')),
                ('Description', models.CharField(null=True, verbose_name='Description', max_length=254, db_column='Description', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Types',
                'verbose_name': 'Contact Type',
                'db_table': 'ContactTypes',
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('Name', models.CharField(max_length=40, db_column='Name')),
                ('Description', models.CharField(null=True, max_length=254, db_column='Description', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Departments',
                'verbose_name': 'Department',
                'db_table': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Families',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('Surname', models.CharField(max_length=40, db_column='Surname')),
                ('Description', models.CharField(null=True, max_length=254, db_column='Description', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Families',
                'verbose_name': 'Family',
                'db_table': 'Families',
            },
        ),
        migrations.CreateModel(
            name='FamilyMembers',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('FamilyId', models.ForeignKey(related_name='FMFamilyId', to='api.Families', verbose_name='Family')),
            ],
            options={
                'verbose_name_plural': 'Family Members',
                'verbose_name': 'Family Member',
                'db_table': 'FamilyMembers',
            },
        ),
        migrations.CreateModel(
            name='FamilyNotes',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('Note', models.TextField(null=True, max_length=2048, db_column='Note', blank=True)),
                ('FamilyId', models.ForeignKey(related_name='FNFamilyId', to='api.Families', verbose_name='Family')),
            ],
            options={
                'verbose_name_plural': 'Family Notes',
                'verbose_name': 'Family Note',
                'db_table': 'FamilyNotes',
            },
        ),
        migrations.CreateModel(
            name='FamilyRoles',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('Role', models.CharField(max_length=40, db_column='Role')),
                ('Description', models.CharField(null=True, max_length=254, db_column='Description', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Family Roles',
                'verbose_name': 'Family Role',
                'db_table': 'FamilyRoles',
            },
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('Grade', models.CharField(max_length=12, db_column='Grade')),
            ],
            options={
                'verbose_name_plural': 'Grades',
                'verbose_name': 'Grade',
                'db_table': 'Grades',
            },
        ),
        migrations.CreateModel(
            name='GroupMembers',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('GradeId', models.ForeignKey(related_name='GMGradeId', to='api.Grades', verbose_name='Grade')),
            ],
            options={
                'verbose_name_plural': 'Group Members',
                'verbose_name': 'Group Member',
                'db_table': 'GroupMembers',
            },
        ),
        migrations.CreateModel(
            name='GroupNotes',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('Note', models.TextField(null=True, max_length=2048, db_column='Note', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Group Notes',
                'verbose_name': 'Group Note',
                'db_table': 'GroupNotes',
            },
        ),
        migrations.CreateModel(
            name='GroupRoles',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('Role', models.CharField(max_length=40, db_column='Role')),
                ('Description', models.CharField(null=True, max_length=254, db_column='Description', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Group Roles',
                'verbose_name': 'Group Role',
                'db_table': 'GroupRoles',
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('Name', models.CharField(max_length=40, db_column='Name')),
                ('Description', models.CharField(null=True, max_length=254, db_column='Description', blank=True)),
                ('DepartmentId', models.ForeignKey(related_name='GRDepartmentId', to='api.Departments', verbose_name='Departments')),
            ],
            options={
                'verbose_name_plural': 'Groups',
                'verbose_name': 'Group',
                'db_table': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='GroupTypes',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('Type', models.CharField(max_length=40, db_column='Type')),
                ('Description', models.CharField(null=True, max_length=254, db_column='Description', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Group Types',
                'verbose_name': 'Group Type',
                'db_table': 'GroupTypes',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('LastName', models.CharField(verbose_name='Last Name', max_length=40, db_column='LastName')),
                ('FirstName', models.CharField(verbose_name='First Name', max_length=40, db_column='FirstName')),
                ('MiddleName', models.CharField(null=True, verbose_name='Middle Name', max_length=40, db_column='MiddleName', blank=True)),
                ('Birthday', models.DateField(null=True, verbose_name='Birthday', blank=True, db_column='Birthday')),
                ('Anniversary', models.DateField(null=True, verbose_name='Anniversary', blank=True, db_column='Anniversary')),
            ],
            options={
                'ordering': ['LastName', 'FirstName'],
                'verbose_name_plural': 'People',
                'db_table': 'People',
            },
        ),
        migrations.CreateModel(
            name='PeopleNotes',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('Note', models.TextField(null=True, max_length=2048, db_column='Note', blank=True)),
                ('PeopleId', models.ForeignKey(related_name='PNPeopleId', to='api.People', verbose_name='People Id')),
            ],
            options={
                'verbose_name_plural': 'People Notes',
                'verbose_name': 'People Note',
                'db_table': 'PeopleNotes',
            },
        ),
        migrations.AddField(
            model_name='groups',
            name='GroupTypeId',
            field=models.ForeignKey(related_name='GRGroupTypeId', to='api.GroupTypes', verbose_name='Group Types'),
        ),
        migrations.AddField(
            model_name='groupnotes',
            name='GroupId',
            field=models.ForeignKey(related_name='GNGroupId', to='api.Groups', verbose_name='Group'),
        ),
        migrations.AddField(
            model_name='groupmembers',
            name='GroupId',
            field=models.ForeignKey(related_name='GMGroupId', to='api.Groups', verbose_name='Group'),
        ),
        migrations.AddField(
            model_name='groupmembers',
            name='GroupRoleId',
            field=models.ForeignKey(related_name='GMGroupRoleId', to='api.GroupRoles', verbose_name='Group Roles'),
        ),
        migrations.AddField(
            model_name='groupmembers',
            name='PeopleId',
            field=models.ForeignKey(related_name='GMPeopleId', to='api.People', verbose_name='People Id'),
        ),
        migrations.AddField(
            model_name='familymembers',
            name='FamilyRoleId',
            field=models.ForeignKey(related_name='FMFamilyRoleId', to='api.FamilyRoles', verbose_name='Family Roles'),
        ),
        migrations.AddField(
            model_name='familymembers',
            name='PeopleId',
            field=models.ForeignKey(related_name='FMPeopleId', to='api.People', verbose_name='People Id'),
        ),
        migrations.AddField(
            model_name='contactentries',
            name='ContactTypeId',
            field=models.ForeignKey(related_name='CEContactTypeId', to='api.ContactTypes', verbose_name='Contact Type Id'),
        ),
        migrations.AddField(
            model_name='contactentries',
            name='PeopleId',
            field=models.ForeignKey(related_name='CEPeopleId', to='api.People', verbose_name='People Id'),
        ),
    ]
