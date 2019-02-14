from django.shortcuts import render
from django.contrib.auth import decorators
from .models import Challenge, Member, Submission
from django.conf import settings
from .algorithms import ranking
# Create your views here.


def login(request):
    return render(request, 'pages/login.html')


@decorators.login_required(login_url='/login/')
def home(request):

    lst_chlg = Challenge.objects.all()
    data = dict()
    data['lst_chlg'] = lst_chlg
    return render(request, 'pages/home.html', data)


@decorators.login_required(login_url='/login/')
def challenge(request, id=1):
    data = dict()
    chlg = Challenge.objects.get(id=id)
    user = request.user
    if request.method == "POST" and request.FILES['submit_file']:
        submit_file = request.FILES['submit_file']
        max_size = int(settings.MAX_UPLOAD_SIZE)
        if submit_file.size > max_size:
            data['server_msg'] = "Your submission is denied. " \
                                 "The file is larger than {}MB".format(round(max_size/1048576))
        elif submit_file.name.split('.')[-1] not in settings.ALLOWED_EXTENSION:
            data['server_msg'] = "Your submission is denied. " \
                                 "Your file is not allowed"

        try:
            new_sub = Submission(member=user, challenge=chlg, file=submit_file)
            new_sub.save()
            data['server_msg'] = "Submit sucessfully"
        except Exception as e:
            data['server_msg'] = "Error while interacting with database. {}".format(e)

    if user.last_name is not None or user.first_name is not None:
        full_name = user.last_name + " " + user.first_name + " - Challenge {}".format(chlg)
    else:
        full_name = str(user.username) + " - Challenge {}".format(chlg)

    lst_chlg = Challenge.objects.all()

    data['lst_chlg'] = lst_chlg
    data['full_name'] = full_name
    data['show_chlg'] = chlg
    data['ranking_table'] = ranking(chlg)
    return render(request, 'pages/submit.html', data)
