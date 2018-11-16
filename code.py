from stack import stack
#opening file
ff= open("input.txt", "r")
fp=open("precedence.txt","r")
#reading line
line = ff.readlines()
precline=fp.readlines()
#total number of lines
count_lines=len(line)
count_preclines=len(precline)
parsestack=stack()
production={}
operator={'$':[0,'']}
precrel=[]
precrelorder={}

#parse the sentence
def parse(ip):
	parsestack.push('$')
	i=0
	while(i<len(ip)):
		top2=parsestack.top
		if parsestack.st[parsestack.top] not in operator.keys():
			while parsestack.st[top2] not in operator.keys() and top2>0:
				top2-=1
		#print("top2="+str(top2))
		ipo=ip[i]
		if (parsestack.st[top2] not in precrelorder.keys()):
			return "error"
	
		if ipo!='id' and ipo!='$':	
			j=i+1
			while(ip[j]!='id' and ip[j]!='$'):
				ipo=ipo+ip[j]
				j=j+1
			if (ipo not in precrelorder.keys()):
				print(ipo)
				return "error"
		a=precrelorder[parsestack.st[top2]]
		b=precrelorder[ipo]
		if parsestack.st[top2]==ipo:
			if parsestack.st[top2]=='$':
				return "accepted"
			elif parsestack.st[top2]=='id':
				print (len(ipo))
				return "error"
		action=precrel[b][a]
			
		if action=='>':
			#shift
			print("shift:"+ipo)
			parsestack.push(ipo)
			print(parsestack.st)
			print("\n")
			if (ipo=='id'):
				i+=1
			else:
				i+=len(ipo)
		elif action=='<': 
			#reduce
			print("reduce "+ipo+" "+parsestack.st[top2])
			temp=""
			while(temp not in production.keys()):
				d=parsestack.pop()
				if d=="empty":
					return "error"
				temp=d+temp
			for k in production.keys():
				if k==temp:
					break
			parsestack.push(production[k])
			print(production[k]+'->'+k)
			print(parsestack.st)
			print("\n")
			
		
				
#check operator grammar
def checkopgram():
	for i in range (0,count_lines):
		line[i]=line[i].strip()
    		#print line[i]
		if line[i]=='':
			continue
		if '->' in line[i]:
    			exp=line[i].split('->')
    			#print exp
			if exp==['']:
				continue
    			if exp[0]>='A' and exp[0]<='Z' and len(exp[0])==1:
          			pass
    			else: 
          			print "invalid rhs production"
	  			exit(0)
    			txt=exp[1].split('#')
    			s=len(txt)
    			'''for j in range (0,s):
          			print txt[j]'''
    			for j in range (0,len(txt)):
          			if '^' in txt[j]:
                 			print "invalid null in production",i+j+1
		 			exit(0)
    			for j in range (0,s):
          			for k in range (1,len(txt[j])):
                 			if txt[j][k-1]>='A' and txt[j][k-1]<='Z' and txt[j][k]>='A' and txt[j][k]<='Z' :
                      				print "no two consecutive terminals allowed in production",i+j+1
		      				exit(0)
    			for j in range (0,s):
          			if len(txt[j])==2:
                 			if txt[j][0] not in operator.keys():
                      				if 'id' not in txt[j]:
                        	   			print "invalid production(2) (No recognisable operator)",i+j+1 
				   			exit(0)                     
          			if len(txt[j])==3:
                 			if txt[j][len(txt[j])-2] not in operator.keys():
                      				if 'id' not in txt[j]:
                        	   			print "invalid production(2) (No recognisable operator)",i+j+1
				   			exit(0)
          			if len(txt[j])==4:
                 			if txt[j][len(txt[j])-3]+txt[j][len(txt[j])-2] not in operator.keys():
						print txt[j][len(txt[j])-2]+txt[j][len(txt[j])-3]
                      				print "invalid production(3) (No recognisable operator)",i+j+1
		      				exit(0)
			temp=[]
				
			for j in range(0,s):
				production[txt[j]]=exp[0]
		elif '->' not in line[i]:
			print("invalid production in line:"+str(i))
			exit(0)
	print("valid grammar\n")
def genprectable():
	for i in range(0,count_preclines):
		precline[i]=precline[i].strip()
		if precline[i]=='':
			continue
		if precline[i][0]=='l' or precline[i][0]=='r':
			order=precline[i].split(" ")
			prec=order[1]
			if ',' in prec:
				prec=prec.split(',')
				for j in prec:
					tempprec=[]
					tempprec.append(i+1)
					tempprec.append(order[0])
					operator[j]=tempprec
			else:
				tempprec=[]
				tempprec.append(i+1)
				tempprec.append(order[0])
				operator[prec]=tempprec
	tempprec=[count_preclines+1,'']
	operator['id']=tempprec
	print(operator)
	lop=operator.keys()
	for i in range(len(lop)):
		precrelorder[lop[i]]=i
	for i in lop:
		tempprecrel=[]
		if i=='$':
			for j in lop:
				if operator[i][0]>operator[j][0]:
					tempprecrel.append('>')
				elif operator[i][0]<operator[j][0]:
					tempprecrel.append('<')
				else:
					tempprecrel.append("a")
			precrel.append(tempprecrel)

		elif i=='id':
			for j in lop:
				if operator[i][0]>operator[j][0]:
					tempprecrel.append('>')
				elif operator[i][0]<operator[j][0]:
					tempprecrel.append('<')
				else:
					tempprecrel.append("e")
			precrel.append(tempprecrel)
		else:
			for j in lop:
				if operator[i][0]>operator[j][0]:
					tempprecrel.append('>')
				elif operator[i][0]<operator[j][0]:
					tempprecrel.append('<')
				else:
					if operator[i][1]=='l':
						tempprecrel.append('>')
					elif operator[i][1]=='r':
						tempprecrel.append('<')
			precrel.append(tempprecrel)
	print "\t",
	for i in lop:
		print i+"\t",
	print('\n')
	for i in range(len(precrel)):
		print lop[i],"\t",
		for j in precrel[i]:
			print j,"\t",
		print('\n')
	#print(precrelorder)
def main():
	ips=input("enter the sentence you want to parse:")
	#ips=ips.split(" ")
	ip=[]
	print("generation of precedence table:\n")
	genprectable()
	print("checking whether grammar provided is operator grammar or not")
	checkopgram()
	
	for i in ips:
		if i.isalpha():
			ip.append('id')
		else:
			ip.append(i)
	ip.append('$')
	
	result=parse(ip)
	print(result)

main()
	
