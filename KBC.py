question=[
		"1.capital of india?",
		"2.economic city of india?",
		"3.HQ of international solar alliances?",
		"4.winner of IPL-2018?",
		"5.runner up of IPL-2018?",
		"6.Peanut plant is?",
		"7.Which one of the following spices is a flower bud?",
		"8.Who is a father of indian congress party?",
		"9.The diamond appears lustrous because of?",
		"10.Raman effect deals with the light rays passing through?",
		"11.On which date GST is applied?",
		"12.who was the fast runner in the world?",
		"13.whole number are start from ?",
		"14.88/44=...?",
		"15.Who is the IT manager of Navgurukul is....?"
		]
first_option=[
			 "0.Delhi","0.Mumbai","0.Nagpur","0.Mumbai indians","0.Chennai super king","0.Herb","0.Cumin",
			 "0.M.K Gandhi","0.Interfernce of light","0.Only fluids","0. 1st june","0.Usion Bolt","0.2","0.44","0.shivnath"
			 ]
second_option=[
			  "1.Mumbai","1.Delhi","1.Gurgaon","1.Chennai super king","1.Sunrisers hydrabad","1.Flower",
			  "1.Clove","1.A.O. Hume","1.Dispersion","1.Only prisms","1. 1st july","1.Milkha Singh","1.0","1.88","1.naresh"
			  ]
third_option=[
			 "2.Bangloar","2.Chennai","2.Delhi","2.Kolkata kight rider","2.Rajstan royals","2.Bush","2.Pepper","2.Lokmany Tilk",
  			 "2.Total internal reflection","2.Only diamond","2. 1st august","2.Dhaynchan Mandela","2.2","2.2","2.sanjay"
  			 ]
fourth_option=[
			  "3.Kolkata","3.Pune","3.Chennai","3,Rajstan royals","3.Kolkata kight rider","3.None of these","3.Turmeric",
			  "3.javahrlal Nehru","3.Scattering","3.All transparanr medium","3. 1st jan","3.Sumit Jain","3.4","3.132","3.sunil"
			  ]
all_option=["first_option","second_option","third_option","fourth_option"]
ans_key=[0,0,1,1,1,0,1,1,2,3,1,0,1,2,2]
price=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,1000000,1500000,3000000,5000000,10000000]
length=len(question)
i=0
total=0
while i<length:
	print question[i] 
	print first_option[i]
	print second_option[i]
	print third_option[i]
	print fourth_option[i]
	x=int(raw_input("Enter your answer "))
	if x==ans_key[i]:
		print "Congrats! your answer is right" 
		print "You win the {} rupees".format(price[i])
		if price[i] == price[4]:
			print "Congrats! Your first level is completed"
		if price[i] == price[9]:
			print "Congrats! Your second level is completed"
		if price[i] == price[14]:
			print "Congrats! Your third level is completed... Now you are a bilinear"
		total = total + price[i]
		print "Total wining price is:-",total,"Rs."

	else:
		print "Sadly your answer is wrong that's why You have lost KBC game \nYou have win total {} Rs, Thank you.".format(total)
		break
	i=i+1

		

		
		