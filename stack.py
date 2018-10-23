class stack():
	def __init__(self):
		self.st=[]
		self.top=-1
	def push(self,a):
		self.st.append(a)
		self.top+=1
	def pop(self):
		if self.top==-1:
			return("empty")
		else:
			b=self.st.pop()
			self.top-=1
			return(b)
