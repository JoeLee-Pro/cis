import sys
import logging
import glob
import csv

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    sermon_path_list = glob.glob("/home/joe/media/audio/*")
    sermon_name_list = []
    for sermon in sermon_path_list:
        sermon_pieces = sermon.split("/")
        sermon_name = sermon_pieces[5]
        if sermon_name.endswith("\n"):
            sermon_name = sermon_name[:-1]
        sermon_name_list.append(sermon_name)

    sermon_name_list.sort(reverse=True)

    print(sermon_name_list)

    return render(request, "website/home.html", {'sermon_name_list': sermon_name_list, 'bg_image': 'AS_Bible.jpg'})


def youthsermonlibrary(request, page=1):
    sermon_path_list = glob.glob("/home/joe/media/audio/*")
    sermon_names = []
    for sermon in sermon_path_list:
        sermon_pieces = sermon.split("/")
        sermon_name = sermon_pieces[5]
        if sermon_name.endswith("\n"):
            sermon_name = sermon_name[:-1]
        sermon_names.append(sermon_name)

    sermon_names.sort(reverse=True)

    paginator = Paginator(sermon_names, 5)

    #page = request.GET.get('page')
    try:
        sermon_name_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        sermon_name_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        sermon_name_list = paginator.page(paginator.num_pages)

    return render(request, "website/youthsermonlibrary.html", {'sermon_name_list': sermon_name_list, 'bg_image': 'YouthSermonLibrary.jpg'})


def abundantlifeadults(request):

    return render(request, "website/abundantlifeadults.html", {'bg_image': 'Adults.jpg'})


def reallifeyouth(request):
    sermon_path_list = glob.glob("/home/joe/media/audio/*")
    sermon_name_list = []
    for sermon in sermon_path_list:
        sermon_pieces = sermon.split("/")
        sermon_name = sermon_pieces[5]
        if sermon_name.endswith("\n"):
            sermon_name = sermon_name[:-1]
        sermon_name_list.append(sermon_name)

    sermon_name_list.sort(reverse=True)

    print(sermon_name_list)

    return render(request, "website/reallifeyouth.html", {'sermon_name_list': sermon_name_list, 'bg_image': 'Youth.jpg'})


def kidslifechildren(request):

    return render(request, "website/kidslifechildren.html", {'bg_image': 'Childrens.jpg'})


def beliefs(request):

    return render(request, "website/beliefs.html", {'bg_image': 'AS_CrossAlone.jpg'})


def missionvision(request):

    return render(request, "website/missionvision.html", {'bg_image': 'MissionVisionBG.jpg'})


def leadership(request):
    return render(request, "website/leadership.html", {'bg_image': 'LeadershipBG.jpg'})


def sermonlibrary(request):
    return render(request, "website/sermonlibrary.html", {'bg_image': 'SermonLibrary.jpg'})


def unscriptedpodcast(request):
    return render(request, "website/unscriptedpodcast.html", {'bg_image': 'UnscriptedPodcast.jpg'})


def calendar(request):

    calendar_items = []
    with open('/home/joe/media/calendar/calendar.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            calendar_item = row[0] + ' - ' + row[1]
            calendar_items.append(calendar_item)

    return render(request, "website/calendar.html", {'calendar_items': calendar_items})
    #return render(request, "website/calendar.html")


def newsletters(request):
    month = []
    month.append("Months")
    month.append("January")
    month.append("February")
    month.append("March")
    month.append("April")
    month.append("May")
    month.append("June")
    month.append("July")
    month.append("August")
    month.append("September")
    month.append("October")
    month.append("November")
    month.append("December")

    newsletters_path_list = glob.glob("/home/joe/media/newsletters/*")
    newsletter_names = []
    for newsletter in newsletters_path_list:
        newsletter_pieces = newsletter.split("-")
        newsletter_year_pieces = newsletter_pieces[0].split("/")
        newsletter_year = newsletter_year_pieces[5]
        newsletter_start_month = int(newsletter_pieces[1])
        newsletter_month = newsletter_pieces[2][0:2]
        newsletter_end_month = int(newsletter_month)

        print(newsletter_year)
        print(newsletter_start_month)
        print(newsletter_end_month)

        newsletter_name = \
            newsletter + month[newsletter_start_month] + "-" + month[newsletter_end_month] + " " + newsletter_year

        print(newsletter_name)
        newsletter_names.append(newsletter_name)

    newsletter_names.sort(reverse=True)

    return render(request, "website/newsletters.html", {'newsletter_names': newsletter_names, 'bg_image': 'WeekenderImage.jpg'})

def contactdirections(request):

    return render(request, "website/contactdirections.html", {'bg_image': 'ContactUs.jpg'})


