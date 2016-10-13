from django.shortcuts import render
import datetime
# Create your views here.

# localtime =  timezone('America/Los_Angeles').localize(datetime.datetime.now())




def index(request):
	localtime = datetime.datetime.now()
	
	context = {
		"date": localtime.strftime("%b %d %Y %I:%M:%S")
		# "date": localtime.strftime(%y)
	}

	return render(request, 'timedisplay/index.html', context)