import sys
import logging

from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.core import serializers
from django.template import RequestContext, Context, loader

from api.models import *

from manager.utilities import FormattedPhoneNumber, FormattedDate

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, portrait, landscape
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import pink, black, red, blue, green
from reportlab.lib import colors

from datetime import datetime, timedelta, date


# Create your views here.
def home(request):

    logger = logging.getLogger('cis')

    logger.debug('Starting home...')

    people_json = serializers.serialize('json', People.objects.order_by('LastName'))
    people = People.objects.order_by('-LastName')
    person_tree = []
    for person in people:
        # sys.stdout.write(str(person) + '\n')
        current_person = dict()
        current_person['id'] = str(person.Id)
        current_person['person'] = person.FirstName + ' ' + person.LastName
        person_tree.append(current_person)

    sys.stdout.write(str(person_tree))

    contact_entries_json = serializers.serialize('json', ContactEntries.objects.order_by('Id'))
    return render_to_response(request, "manager/home.html", {'person_tree': person_tree, 'people_json': people_json, 'contact_entries_json': contact_entries_json})


def generate_sunday_school_rolls(request):
    logger = logging.getLogger('cis')
    logger.debug(request.POST.get('TitleTextbox'))
    logger.debug(request.POST.get('StartDateTextbox'))
    logger.debug(request.POST.get('EndDateTextbox'))

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="SundaySchoolReport.pdf"'

    # Create the PDF object, using the response object as its "file."
    pageCanvas = canvas.Canvas(response, pagesize=landscape(letter))

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    #p.drawString(100, 10, "Hello world.")
    #hello(p)
    design_sunday_school_rolls(pageCanvas, request.POST.get('TitleTextbox'), request.POST.get('StartDateTextbox'), request.POST.get('EndDateTextbox'))

    # Close the PDF object cleanly, and we're done.
    pageCanvas.showPage()
    pageCanvas.save()

    return response


def design_sunday_school_rolls(pageCanvas, quarterTitle, passedStartDate, passedEndDate):
    # quarterTitle = "Spring 2016"
    startYear, startMonth, startDay = passedStartDate.split('/')
    startDate = date(int(startYear), int(startMonth), int(startDay))

    endYear, endMonth, endDay = passedEndDate.split('/')
    endDate = date(int(endYear), int(endMonth), int(endDay))

    # We handle the first class differently, since we need no newpage for the first class.
    firstClass = True

    sundaySchoolGroups = Groups.objects.filter(GroupTypeId__Type = "Sunday School Class").order_by("Name")
    for sundaySchoolClass in sundaySchoolGroups:
        if sundaySchoolClass.Name == 'College & Career [Inactive]' or sundaySchoolClass.Name == 'Young Married [Inactive]' or sundaySchoolClass.Name == 'Young Married 1':
            continue

        print(sundaySchoolClass.GroupTypeId)
        numberOfWeeks = 0

        # We do not want a new page, which would be blank, for the first class.
        if firstClass:
            firstClass = False
        else:
            pageCanvas.showPage()

        ssClassMembers = GroupMembers.objects.filter(GroupId = sundaySchoolClass.Id).order_by("-GroupRoleId__Role", "PeopleId__LastName", "PeopleId__FirstName").select_related("PeopleId")

        oldGroupRoleId = ""
        textObject = None
        for ssClassMember in ssClassMembers:
            member = ssClassMember.PeopleId
            currentGroupRoleId = str(ssClassMember.GroupRoleId)
            print(oldGroupRoleId + " | " + currentGroupRoleId)
            if currentGroupRoleId != oldGroupRoleId:
                if textObject is None:
                    textObject, numberOfWeeks = new_page(pageCanvas, startDate, endDate, quarterTitle, sundaySchoolClass.Name, currentGroupRoleId)
                else:
                    textObject = new_page_if_needed(pageCanvas, textObject, startDate, endDate, quarterTitle, sundaySchoolClass.Name, currentGroupRoleId, True)

                oldGroupRoleId = currentGroupRoleId

            print(ssClassMember.GroupRoleId)
            if str(ssClassMember.GroupRoleId) == "Teacher" or str(ssClassMember.GroupRoleId) == "Leader":
                print("This is a Teacher or Leader...")
                textObject.setFillColor(colors.orange)
            elif str(ssClassMember.GroupRoleId) == "Prospect":
                print("This is a Prospect...")
                textObject.setFillColor(blue)
            elif str(ssClassMember.GroupRoleId) == "Other Member" or str(ssClassMember.GroupRoleId) == "Helper":
                print("This is a Other Member...")
                textObject.setFillColor(colors.green)
            elif str(ssClassMember.GroupRoleId) == "Outreach":
                print("This is an Outreach Member...")
                textObject.setFillColor(colors.red)
            else:
                print("This is a Member...")
                textObject.setFillColor(black)

            #print("***** Member: " + str(ssClassMember.PeopleId) + " | Class: " + sundaySchoolClass.Name)
            #PeopleList = People.objects.all()
            #for member in PeopleList:
            textObject.setFont("Times-Bold", 10)
            textObject.moveCursor(-textObject.getX() + inch * .35, 0)
            print(ssClassMember.GradeId)
            if str(ssClassMember.GradeId) != 'Adult':
                textObject.textOut(member.FirstName + ' ' + member.LastName + ' [' + str(ssClassMember.GradeId) + ']')
            else:
                textObject.textOut(member.FirstName + ' ' + member.LastName)
            textObject.setFont("Times-Roman", 10)

            sys.stdout.write(str(type(member.Birthday)) + "\n")

            if member.Birthday is not None:
                textObject.moveCursor(inch * 2, 0)
                #textObject.textOut("Birthday: " + FormattedDate(member.Birthday))
                textObject.textOut("Birthday: " + str(member.Birthday))
                textObject.moveCursor(inch, 0)
            else:
                textObject.moveCursor(inch * 3, 0)

            for a in range(1,numberOfWeeks + 1):
                textObject.moveCursor(inch * .5, 0)
                textObject.textOut("_____")

            textObject.moveCursor(-(inch * .5 * (numberOfWeeks + 6)), 0)
            textObject.textLine(" ")

            try:
                contactEntries = ContactEntries.objects.get(PeopleId = member.Id, ContactTypeId__Type = "Home")
                print(str(contactEntries.ContactTypeId) + " | " + member.LastName)

                if contactEntries is not None:
                    textObject.textOut(contactEntries.Address)

                    print(member.Anniversary)
                    if member.Anniversary is not None:
                        textObject.moveCursor(inch * 2, 0)
                        textObject.textOut("Anniversary: " + str(member.Anniversary))
                        textObject.moveCursor(-(inch * 2), 0)
                        textObject.textLine(" ")
                    else:
                        #textObject.moveCursor(inch * 2, 0)
                        textObject.textLine(" ")

                    print(contactEntries.City)
                    if contactEntries.City is not None and contactEntries.State is not None:
                        textObject.textLine(contactEntries.City + " " + contactEntries.State + " " + contactEntries.Zip)

                    #textObject.textLine(FormattedPhoneNumber(contactEntries.Phone))
                    if contactEntries.Phone is not None:
                        textObject.textLine(contactEntries.Phone)
                    else:
                        textObject.textLine(" ")

                    textObject = new_page_if_needed(pageCanvas, textObject, startDate, endDate, quarterTitle, sundaySchoolClass.Name, currentGroupRoleId, False)
                else:
                    if member.Anniversary is not None:
                        textObject.moveCursor(inch * 2, 0)
                        textObject.textOut("Anniversary: " + FormattedDate(member.Anniversary))
                        textObject.moveCursor(-inch * 2, 0)
                        textObject.textLine(" ")
                    else:
                        textObject.textLine(" ")

            except:
                #if member.Anniversary is not None:
                #    textObject.moveCursor(inch * 2, 0)
                #    textObject.textOut("Anniversary: " + FormattedDate(member.Anniversary))
                #    textObject.moveCursor(-inch *2, 0)
                #    textObject.textLine(" ")
                print(sys.exc_info()[0])

            textObject.textLine(" ")

        pageCanvas.drawText(textObject)


def new_page(pageCanvas, startDate, endDate, quarterTitle, ssClassName, currentGroupRoleId):
    topOfPage = inch * 8
    leftOfPage = inch * 0.35

    pageCanvas.setStrokeColor(black)

    pageText = pageCanvas.beginText()
    pageText.setTextOrigin(leftOfPage, topOfPage)

    #startDate = date(2014, 12, 7)
    #endDate = date(2015, 2, 22)

    pageText.setFont("Times-Bold", 10)
    pageText.textOut("Sunday School Rolls")
    pageText.moveCursor(inch * 2, 0)
    pageText.textLine(ssClassName)
    pageText.moveCursor(-(inch * 2), 0)
    pageText.textOut(quarterTitle)
    pageText.moveCursor(inch * 2, 0)

    if str(currentGroupRoleId) == "Teacher" or str(currentGroupRoleId) == "Leader":
        print("This is a Teacher or Leader...")
        pageText.setFillColor(colors.orange)
    elif str(currentGroupRoleId) == "Prospect":
        print("This is a Prospect...")
        pageText.setFillColor(blue)
    elif str(currentGroupRoleId) == "Other Member" or str(currentGroupRoleId) == "Helper":
        print("This is a Other Member...")
        pageText.setFillColor(colors.green)
    elif str(currentGroupRoleId) == "Outreach":
        print("This is an Outreach Member...")
        pageText.setFillColor(colors.red)
    else:
        print("This is a Member...")
        pageText.setFillColor(black)
    pageText.textOut(currentGroupRoleId.upper())
    pageText.setFillColor(black)

    pageText.moveCursor(inch * 1.5, 0)
    pageText.setFont("Times-Bold", 10)

    numberOfWeeks = 0
    currentDate = startDate
    while (currentDate <= endDate):
        #print("Current Date: " + FormattedDate(currentDate) + " | Start Date: " + FormattedDate(startDate) + " | End Date: " + FormattedDate(endDate))
        numberOfWeeks += 1
        pageText.textOut(FormattedDate(currentDate))
        pageText.moveCursor(inch * .5, 0)
        currentDate = currentDate + timedelta(days=7)

    #print(numberOfWeeks)
    pageText.moveCursor(-(inch * .5 * (numberOfWeeks + 7)), 0)
    pageText.textLine(" ")
    pageText.textLine(" ")
    pageText.textLine(" ")

    return (pageText, numberOfWeeks)


def new_page_if_needed(pageCanvas, textObject, startDate, endDate, quarterTitle, ssClassName, currentGroupRoleId, force):
    print("Current Y: " + str(textObject.getY()))

    if textObject.getY() <= inch or force:
        print("New page...")
        pageCanvas.drawText(textObject)
        pageCanvas.showPage()

        topOfPage = inch * 8
        leftOfPage = inch * 0.35

        pageCanvas.setStrokeColor(black)

        pageText = pageCanvas.beginText()
        pageText.setTextOrigin(leftOfPage, topOfPage)

        #startDate = date(2014, 12, 7)
        #endDate = date(2015, 2, 22)

        pageText.setFont("Times-Bold", 10)
        pageText.textOut("Sunday School Rolls")
        pageText.moveCursor(inch * 2, 0)
        pageText.textLine(ssClassName)
        pageText.moveCursor(-(inch * 2), 0)
        pageText.textOut(quarterTitle)
        pageText.moveCursor(inch * 2, 0)

        if str(currentGroupRoleId) == "Teacher" or str(currentGroupRoleId) == "Leader":
            print("This is a Teacher or Leader...")
            pageText.setFillColor(colors.orange)
        elif str(currentGroupRoleId) == "Prospect":
            print("This is a Prospect...")
            pageText.setFillColor(blue)
        elif str(currentGroupRoleId) == "Other Member" or str(currentGroupRoleId) == "Helper":
            print("This is a Other Member...")
            pageText.setFillColor(colors.green)
        elif str(currentGroupRoleId) == "Outreach":
            print("This is an Outreach Member...")
            pageText.setFillColor(colors.red)
        else:
            print("This is a Member...")
            pageText.setFillColor(black)
        pageText.textOut(currentGroupRoleId.upper())
        pageText.setFillColor(black)

        pageText.moveCursor(inch * 1.5, 0)
        pageText.setFont("Times-Bold", 10)

        numberOfWeeks = 0
        currentDate = startDate
        while (currentDate <= endDate):
            numberOfWeeks += 1
            pageText.textOut(FormattedDate(currentDate))
            pageText.moveCursor(inch * .5, 0)
            currentDate = currentDate + timedelta(days=7)

        print(numberOfWeeks)
        pageText.moveCursor(-(inch * .5 * (numberOfWeeks + 7)), 0)
        pageText.textLine(" ")
        pageText.textLine(" ")
        pageText.textLine(" ")

        return pageText
    else:
        return textObject
