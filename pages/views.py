from django.shortcuts import render


def home(request):
    """
    Home view
    """
    template = 'pages/home.html'
    return render(request, template)


def about(request):
    """
    About view
    """
    template = 'pages/about.html'
    return render(request, template)


def timetable(request):
    """
    Timetable view
    """
    template = 'pages/timetable.html'
    return render(request, template)
