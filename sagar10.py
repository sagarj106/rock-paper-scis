import random
l=["r","p","s"]
d={'r':'rock','p':'paper','s':'scissor'}
cs=0                             
us=0
while True:
	#take input from user
	u=input("enter your choice,press n to discontinue: ")
	if u in d:
		print("user chooses: ",d[u])
		#to exit
	if u=='n':
		print("game over")
		print("user score: ",us)
		print("comp score: ",cs)
		exit()
	#input the user and computer choice
	c=random.choice(l)
	print("computer choose: ",d[c])
	if u==c:
		print("tie")
	elif u=="r" and c=="p":
		cs=cs+1
		print("comp wins",cs)
	elif u=='r' and c=='s':
		us=us+1
		print("user wins",us)
	elif u=='p' and c=='r':
		us=us+1
		print("user wins",us)
	elif u=='p' and c=='s':
		cs=cs+1
		print("comp wins",cs)
	elif u=='s' and c=='p':
		us=us+1
		print("user wins",us)
	elif u=='s' and c=='r':
		cs=cs+1
		print("comp wins",cs) 