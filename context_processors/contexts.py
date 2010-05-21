from django.conf import settings
from ava.mainpage.models import Comment, Vote, Count

def count(request):
	count_data = Count.objects.get(id=1)
	appleC = count_data.apple
	adobeC = count_data.adobe
	totalC = appleC + adobeC
	ap_per = round(float(appleC) / float(totalC)*100)
	ad_per = 100 - ap_per
	chart_url = "http://chart.apis.google.com/chart?cht=p3&chd=t:"+str(ap_per)+","+str(ad_per)+"&chs=465x270&chl=Apple|Adobe&chf=bg,s,DDDDDD&chdl=Apple:%20"+str(int(ap_per))+"%|Adobe:%20"+str(int(ad_per))+"%&chco=8DC63F|3FA2C6&chdlp=b"
	return locals()
