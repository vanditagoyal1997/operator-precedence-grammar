from stack import stack
#opening file
ff= open("input.txt", "r")
#reading line
line = ff.readlines()
#total number of lines
count_lines=len(line)
parsestack=stack()
production={}
operator={'+':8,'-':8,'*':9,'/':9,'&':5,'|':4,'>':7,'<':7,'!=':6,'==':6,'=':1,'&&':3,'||':2,'id':10,'$':0}

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
		a=operator[parsestack.st[top2]]
		b=operator[ip[i]]
		if parsestack.st[top2]==ip[i]:
			if parsestack.st[top2]=='$':
				return "accepted"
			elif parsestack.st[top2]=='id':
				return "error"
		if a==b:
			if ip[i]=='=':
				b=b+1
			else:
				a=a+1
			
		if a<b:
			#shift
			print("shift:"+ip[i])
			parsestack.push(ip[i])
			print(parsestack.st)
			print("\n")
			i+=1
		else: 
			#reduce
			print("reduce "+ip[i]+" "+parsestack.st[top2])
			temp=""
			while(temp not in production.keys()):
				d=parsestack.pop()
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
                        	   			print "invalid production(2)",i+j+1 
				   			exit(0)                     
          			if len(txt[j])==3:
                 			if txt[j][len(txt[j])-2] not in operator.keys():
                      				if 'id' not in txt[j]:
                        	   			print "invalid production(2)",i+j+1
				   			exit(0)
          			if len(txt[j])==4:
                 			if txt[j][len(txt[j])-2] not in operator and txt[j][len(txt[j])-3] not in operator.keys():
                      				print "invalid production(3)",i+j+1
		      				exit(0)
			temp=[]
				
			for j in range(0,s):
				production[txt[j]]=exp[0]
		elif '->' not in line[i]:
			print("invalid production in line:"+str(i))
			exit(0)
	print("valid grammar\n")
			
def main():
	ips=input("enter the sentence you want to parse:")
	ip=[]
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
	
