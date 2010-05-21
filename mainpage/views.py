from django.shortcuts import render_to_response
from django.template import RequestContext
from ava.mainpage.models import Count, Vote, Comment
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.list_detail import object_list
from ava.mainpage.forms import *
from ava.decorators import *
import datetime


def index(request,pagination_id=1):
	return object_list(request, Comment.objects.all().order_by('-date'), paginate_by = 70, allow_empty = True, page = pagination_id, template_name = 'index.html')


def comment(request):
	global voteid
	form = newVote(request.POST)
	if form.is_valid():
		choiceN = form.cleaned_data['choice']
		commentN= form.cleaned_data['comment']
		emailN= form.cleaned_data['email']
		dateN = datetime.datetime.now()
		nameN =  form.cleaned_data['name']

		if not 'vote' in request.session and not 'vote' in request.COOKIES:
			p = Vote(choice=choiceN, date=dateN,info=request.META['HTTP_USER_AGENT']+' '+request.META['REMOTE_ADDR'])
			c = Count.objects.get(id=1)

			if choiceN == 'Apple': c.apple += 1
			else: c.adobe += 1

			p.save()
			c.save()
			request.session['vote'] = p.id
			response = HttpResponseRedirect('/')
			response.set_cookie('vote',p.id,max_age=648000)
			p.comment_set.create(text=commentN,name=nameN,date=dateN,email=emailN,like=0,choice=choiceN)
			p.save()
			return response

		if commentN or emailN:
			if 'vote' in request.session:
				p = Vote.objects.get(id=int(request.session['vote']))
			elif 'vote' in request.COOKIES:
				p = Vote.objects.get(id=int(request.COOKIES['vote']))
			p.comment_set.create(text=commentN,name=nameN,date=dateN,email=emailN,like=0,choice=choiceN)
			p.save()

		return HttpResponseRedirect('/')
	else:
		error = "You didnt make any choice or your e-mail is invalid (if provided)"
		return HttpResponseRedirect('/page1')


def like(request,comment_id,pm):
	c = Comment.objects.get(id=comment_id)
	pm = int(pm) 
	if pm == 1: c.like += 1
	else: c.like -= 1

	if 'like' in request.session:
		if str(comment_id)  in request.session:
			error = "You already voted for that opinion"
			return HttpResponseRedirect('/')
		else:
			c.save()
			request.session[str(c.id)] = 1
	else:
		c.save()
		request.session['like'] = 1
		request.session[str(c.id)] = 1

	return HttpResponseRedirect('/')


