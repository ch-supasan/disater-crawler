file = open("disasterDB.txt" , "w+")


import feedparser


url = "http://www.gdacs.org//rss.aspx?profile=ARCHIVE&from=2013-01-01&to=2013-11-17&alertlevel=&country=&eventtype=EQ,TC,TS,FL"
# url = "http://www.gdacs.org//rss.aspx?profile=ARCHIVE"

feed = feedparser.parse( url )

a_alert =[]
a_magnitude =[]
a_depth =[]
a_name =[]
a_speed =[]
a_id =[]
a_infodate =[]
a_lat =[]
a_long =[]
a_type =[]

for x in feed['entries']:

 	file.write (x['gdacs_eventtype']+"\n");
 	a_type.append(x['gdacs_eventtype'])

 	file.write ( x['gdacs_fromdate']+"\n");
 	a_infodate.append(x['gdacs_fromdate'])

 	file.write ( x['geo_lat']+"\n");
 	a_lat.append(x['geo_lat'])

 	file.write ( x['geo_long']+"\n");
 	a_long.append(x['geo_long'])

	if x['gdacs_eventtype'] == 'EQ':
		alertlevel = x['title'][ : x['title'].find('earthquake')]
		file.write ( alertlevel+"\n");
		a_alert.append(alertlevel)
		# print a

		data = x['title'][ x['title'].find('(')+1 : x['title'].find(')')]
		# print 'data',data

		magnitude = data[ data.find('Magnitude')+10 : data.find('M,')]
		# print magnitude
		file.write ( magnitude+"\n");
		a_magnitude.append(magnitude)

		depth = data[data.find('Depth:')+6: data.find('km')]
		# print depth
		file.write ( depth+"\n");	
		a_depth.append(depth)

		a_name.append("-")
		a_speed.append(0)

	elif x['gdacs_eventtype'] == 'TC':
		alertlevel = x['title'][ : x['title'].find('alert')]
		# print 'title', alertlevel
		file.write ( alertlevel+"\n");	
		a_alert.append(alertlevel)
		
		name = x['title'][x['title'].find('cyclone')+8 : x['title'].find('-13.')]
		# print 'name', name
		file.write ( name+"\n");
		a_name.append(name)	

		speed = x['title'][x['title'].find('(')+1 : x['title'].find('km/h')]
		# print 'speed',speed
		file.write ( speed+"\n");
		a_speed.append(speed)		

		a_magnitude.append(0)
		a_depth.append(0)


	elif x['gdacs_eventtype'] == 'FL':
		alertlevel = x['title'][ : x['title'].find('flood')]
		# print 'titleF', alertlevel
		file.write ( alertlevel+"\n");	
		a_alert.append(alertlevel)

		a_magnitude.append(0)
		a_depth.append(0)
		a_name.append("-")
		a_speed.append(0)


 	i=0
 	for y in x['links']:
 		if(i==1) :
 			getID = y['href'].split("eventid=");
 			file.write ( getID[1]+"\n");
 			a_id.append(getID[1])
 		i = i + 1
 		# exit(1)

file.close()

import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="", # your password
                      db="ihpc") # name of the data base

cursor = db.cursor()

for k in range(len(a_alert)): 

	sql = '''INSERT INTO `disaster_db`(`ID`, `Type`, `AlertLV`, `DateInfo`, `Magnitude`, `Depth`, `Speed`, `Lat`, `Long`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')'''%(str(a_id[k]),str(a_type[k]),str(a_alert[k]),str(a_infodate[k]),str(a_magnitude[k]),str(a_depth[k]),str(a_speed[k]),str(a_lat[k]),str(a_long[k]))

	cursor.execute(sql)
	
	db.commit()




db.close()

# print type(str(a_id[1]))

# print len(a_alert)
# print len(a_magnitude)
# print len(a_depth)
# print len(a_name)
# print len(a_speed)

# print a_speed
# print a_name
# print a_magnitude