AAA = 7
print AAA
file = open("disater.txt" , "w+")


import feedparser


url = "http://www.gdacs.org//rss.aspx?profile=ARCHIVE&from=2010-01-01&to=2013-11-17&alertlevel=&country=&eventtype=EQ,TC,TS,FL"
# url = "http://www.gdacs.org//rss.aspx?profile=ARCHIVE"

feed = feedparser.parse( url )

for x in feed['entries']:

 	file.write (x['gdacs_eventtype']+"\n");
 	file.write ( x['gdacs_fromdate']+"\n");
 	file.write ( x['title']+"\n");
 	file.write ( x['geo_lat']+"\n");
 	file.write ( x['geo_long']+"\n");

	if x['gdacs_eventtype'] == 'EQ':
		title = x['title'][ : x['title'].find('earthquake')]
		print 'title', title

		data = x['title'][ x['title'].find('(')+1 : x['title'].find(')')]
		print 'data',data

		magnitude = data[ data.find('Magnitude')+10 : data.find('M,')]
		print magnitude

		depth = data[data.find('Depth:')+6: data.find('km')]
		print depth

	elif x['gdacs_eventtype'] == 'TC':
		title = x['title'][ : x['title'].find('alert')]
		print 'title', title
		
		name = x['title'][x['title'].find('cyclone')+8 : x['title'].find('-13.')]
		print 'name', name

		speed = x['title'][x['title'].find('(')+1 : x['title'].find('km/h')]
		print 'speed',speed

	elif x['gdacs_eventtype'] == 'FL':
		title = x['title'][ : x['title'].find('flood')]
		print 'titleF', title


 	i=0
 	for y in x['links']:
 		if(i==1) :
 			getID = y['href'].split("eventid=");
 			file.write ( getID[1]+"\n");
 		i = i + 1
 		# exit(1)

import MySQLdb

file.close()
