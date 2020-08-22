import os
def linkgo(point,p):
	i=0
	start=0
	for i in range(0,point):
		if p[i]==' ':
				start=i
	end=p.find(" ",point,len(p))
	x=p[start+1:end]					
	os.system('start chrome %s'% x)
#instructions
print('\nHello Dear\n')
print("INSTRUCTIONS : ")
print(' . Our Features\n')
print('   .   Chrome                 .   Microsoft Edge')
print('   .   Notepad                .   Windows media player')
print('   .   excel                  .   Paint')
print('   .   File Explorer          .   vs code')
print('   .   Google search          .   Type any url')
print('   .   youtube(on chrome)     .   facebook(on chrome)')
print('   .   instagram(on chrome)   .   WhatsApp(on chrome)')
print('   .   search any video after running youtube (on chrome)\n')
print(' . Type back() to take one step back')
print(' . Type exit() to close all')
while True:
	print("Type Here : " ,end='')
	# main input
	p=input()
	p=p.replace('  ',' ')
	if not (p.find('how')>=0 or p.find('what')>=0 or p.find('why')>=0 or p.find('when')>=0 or p.find('where')>=0 ):
		p=p.replace('  ',' ')
		p=p.replace('find ','')
		p=p.replace('search ','')
	if "dont " in p or "don't" in p or "do not " in p or "donot " in p or "not " in p:# if user to run command in negative sence
		if "exit"in p or "end" in p  or "exit" in p  or "terminate" in p or "close" in p or "execute" in p or "start" in p or "run" in p or "launch" in p or "go" in p or "shutdown" in p or "open" in p:
			continue
		else:
			p=p.replace(" ","+")
			os.system('start chrome https://www.google.com/search?q=%s'% p)	 		
	elif "back()"in p or "exit()" in p:#end program
		break	
	elif ".c"in p :
		point=p.find(".c")										  
		linkgo(point,p)											
	elif ".i"in p :
		point=p.find(".i")										  
		linkgo(point,p)											
	elif ".g"in p :
		point=p.find(".g")										  
		linkgo(point,p)											
	elif ".net"in p :												#any link
		point=p.find(".net")										  
		linkgo(point,p)											
	elif ".org"in p :
		point=p.find(".org")										  
		linkgo(point,p)											
	elif ".tk"in p :
		point=p.find(".tk")										  
		linkgo(point,p)											
	elif ".ml"in p :
		point=p.find(".ml")										  
		linkgo(point,p)	
	elif ".xyz"in p :
		point=p.find(".xyz")										  
		linkgo(point,p)										
	elif p=="":#if user press enter 
		continue
	elif "facebook in chrome" in p or "fb in chrome" in p or "facebook on chrome" in p or "fb on chrome" in p or  "facebook in the chrome" in p or "fb in the chrome" in p or "facebook on the chrome" in p or "fb on the chrome" in p:	#to open facebook in chrome			
		os.system('start chrome https://www.facebook.com')						
	elif "whatsapp in chrome" in p or "whatsapp on chrome" in p or "whatsapp in the chrome" in p or "whatsapp on the chrome" in p:#to open whaatsapp in chrome				
		os.system('start chrome https://web.whatsapp.com/')						
	elif "insta in chrome" in p or "insta on chrome" in p or "instagram in chrome" in p or "instagram on chrome" in p or  "insta in the chrome" in p or "insta on the chrome" in p or "instagram in the chrome" in p or"instagram on the chrome" in p :	#to open instagram in chrome			
		os.system('start chrome https://www.instagram.com')						
	elif "on youtube" in p or "in youtube" in p or "on the youtube" in p or "in the youtube" in p:#to search any thing on youtube(chrome)
		p=p.replace('in chrome','')
		p=p.replace('in the chrome','')
		p=p.replace(' on youtube','')											
		p=p.replace(' in youtube','')		
		p=p.replace(" ","+")
		os.system('start chrome https://www.youtube.com/results?search_query=%s'% p)
	elif "youtube in chrome" in p or "yt in chrome" in p or "youtube in chrome" in p or "yt in chrome" in p or "youtube in the chrome" in p or "yt in the chrome" in p or "youtube in the chrome" in p or "yt in the chrome" in p:#to open yt in chrome
		while True: 
			print('\nWhat you want to search on youtube : ' ,end='')
			x=input()
			if not (x.find('how')>=0 or x.find('what')>=0 or x.find('why')>=0 or x.find('when')>=0 or x.find('where')>=0 ):
				p=p.replace('  ',' ')
				p=p.replace('find ','')
				p=p.replace('search ','')
			if "back()"in x:
				break
			if "exit()"in x:													
				break
			elif x=="":
				continue
			else:
				x=x.replace(" ","+")
				os.system('start chrome https://www.youtube.com/results?search_query=%s'% x)
		if "exit()"in x:
			break
	elif "on chrome" in p or "in chrome" in p or "on the chrome" in p or "in the chrome" in p:#to search anything on chrome
		p=p.replace(' on chrome','')
		p=p.replace(' in chrome','')
		p=p.replace(" ","+")
		os.system('start chrome https://www.google.com/search?q=%s'% p)
	elif "facebook in microsoft edge" in p or "fb in microsoft edge" in p or "facebook on microsoft edge" in p or "fb on microsoft edge" in p or  "facebook in the microsoft edge" in p or "fb in the microsoft edge" in p or "facebook on the microsoft edge" in p or "fb on the microsoft edge" in p:	#to open facebook in chrome			
		os.system('start microsoft-edge: https://www.facebook.com')				
	elif "whatsapp in microsoft edge" in p or "whatsapp on microsoft edge" in p or "whatsapp in the microsoft edge" in p or "whatsapp on the microsoft edge" in p:	#to open whatsapp in chrome			
		os.system('start microsoft-edge: https://web.whatsapp.com/')			
	elif "insta in microsoft edge" in p or "insta on microsoft edge" in p or "instagram in microsoft edge" in p or "instagram on microsoft edge" in p or  "insta in the microsoft edge" in p or "insta on the microsoft edge" in p or "instagram in the microsoft edge" in p or "instagram on the microsoft edge" in p :#to open instagram in chrome				
		os.system('start microsoft-edge: https://www.instagram.com')			
	elif "youtube in microsoft edge" in p or "yt in microsoft edge" in p or "youtube on microsoft edge" in p or "yt on microsoft edge" in p or  "youtube in the microsoft edge" in p or "yt in the microsoft edge" in p or "youtube on the microsoft edge" in p or "yt on the microsoft edge" in p:	#to open yt in microsoft edge			
		while True: 
			print('\nWhat you want to search on youtube : ' ,end='')
			x=input()
			if not (x.find('how')>=0 or x.find('what')>=0 or x.find('why')>=0 or x.find('when')>=0 or x.find('where')>=0 ):
				p=p.replace('  ',' ')
				p=p.replace('find ','')
				p=p.replace('search ','')
			if "back()"in x:
				break
			if "exit()"in x:													
				break
			elif x=="":
				continue
			else:
				x=x.replace(" ","+")
				os.system('start micrisoft-edge: https://www.youtube.com/results?search_query=%s'% x)
		if "exit()"in x:
			break
	elif "on microsoft edge" in p or "in microsoft edge" in p or "on the microsoft edge" in p or "in the microsoft edge" in p:#to search anything on chrome
		p=p.replace(' on microsoft edge','')
		p=p.replace(' in microsoft edge','')												
		p=p.replace('find ','')		
		p=p.replace('search ','')	
		p=p.replace(" ","+")
		os.system('start microsoft-edge: https://www.bing.com/search?q=%s'% p)	
	elif "execute " in p or "start " in p or "run " in p or "launch " in p  or "open " in p: #start applications
		if "notepad" in p or "text editor" in p:								#run notepad
			os.system("notepad")
		elif "media" in p and "player" in p:									#run windows media player
			os.system("start wmplayer")
		elif "chrome" in p:														#run chrome
			while True: 
				print('\nWhat you want to search : ' ,end='')
				x=input()
				if not (x.find('how')>=0 or x.find('what')>=0 or x.find('why')>=0 or x.find('when')>=0 or x.find('where')>=0 ):
					p=p.replace('  ',' ')
					p=p.replace('find ','')
					p=p.replace('search ','')
				if "back()"in x:
					break
				if "exit()"in x:
					break
				elif x=="":
					continue
				elif ".c"in p :
					point=p.find(".c")										  
					linkgo(point,p)											
				elif ".i"in p :
					point=p.find(".i")										  
					linkgo(point,p)											
				elif ".g"in p :
					point=p.find(".g")										  
					linkgo(point,p)											
				elif ".net"in p :												#any link
					point=p.find(".net")										  
					linkgo(point,p)											
				elif ".org"in p :
					point=p.find(".org")										  
					linkgo(point,p)											
				elif ".tk"in p :
					point=p.find(".tk")										  
					linkgo(point,p)											
				elif ".ml"in p :
					point=p.find(".ml")										  
					linkgo(point,p)	
				elif ".xyz"in p :
					point=p.find(".xyz")										  
					linkgo(point,p)				
				else:
					x=x.replace(" ","+")
					os.system('start chrome https://www.google.com/search?q=%s'% x)
			if "exit()"in x:
				break
		elif "youtube" in p:														#run youtube (by default in chrome)
			while True: 
				print('\nWhat you want to search : ' ,end='')
				x=input()
				if not (x.find('how')>=0 or x.find('what')>=0 or x.find('why')>=0 or x.find('when')>=0 or x.find('where')>=0 ):
					x=x.replace('  ',' ')
					x=x.replace('find ','')
					x=x.replace('search ','')
				if "back()"in x:
					break
				if "exit()"in x:
					break
				elif x=="":
					continue
				else:
					x=x.replace(" ","+")
					os.system('start chrome https://www.youtube.com/results?search_query=%s'% x)
			if "exit()"in x:
				break
		elif "microsft edge" in p or "ms edge" in p or "ms-edge" in p or "edge" in p:									#run ms edge
			while True: 
				print('\nWhat you want to search : ' ,end='')
				x=input()
				if not (x.find('how')>=0 or x.find('what')>=0 or x.find('why')>=0 or x.find('when')>=0 or x.find('where')>=0 ):
					p=p.replace('  ',' ')
					p=p.replace('find ','')
					p=p.replace('search ','')
				if "back()"in x:
					break
				if "exit()"in x:
					break
				elif x=="":
					continue
				else:
					os.system('start microsoft-edge : https://www.bing.com/search?q%s'% x)
			if "exit()"in x:
				break
		elif "excel" in p:														#run excel
			os.system("start  excel")	
		elif "vscode" in p or "vs code"in p or "vs-code" in p or "virtual studio" in p  or "virtual studio code" in p:#run vscode
			os.system("start vscode:")											
		elif "paint" in p:														#paint
			os.system("mspaint")
		elif "explorer" in p or ('file' in p and 'manager' in p ):														#paint
			os.system("explorer")
		else:
			print("Does not support")
			print("Do You want to search it on google")
			while True:
				x=input()
				if "yes" in x:
					p=p.replace('open','')
					p=p.replace(" ","+")
					os.system('start chrome https://www.google.com/search?q=%s'% p)		
				elif "no" in x:
					continue
				if "back()"in x:
					break
				if "exit()"in x:
					break
				else:
					print('Action is not identified')
					print("Do You want to search it on google")
			if "exit()"in x:
				break											
	else:
		if not (p.find('how')>=0 or p.find('what')>=0 or p.find('why')>=0 or p.find('when')>=0 or p.find('where')>=0 ):
			p=p.replace('find ','')
			p=p.replace('search ','')
			p=p.replace(' in google','')
			p=p.replace(' in the google','')
			p=p.replace(' on google','')
			p=p.replace(' on the google','')
		p=p.replace(" ","+")
		os.system('start chrome https://www.google.com/search?q=%s'% p)