print("WELCOME TO KBC GAME")
name=input("enter your name")
questions_list=["1.who discovered python","2.how many datatypes in python","3.how many cases in python","4.in which year python discovered"]
options_list=[["1.rajitha","2.gangothri","3.akshitha","4.guidovan russum"],["1.six","2.four","3.two","4.seven"],["1.two","2.one","3.five","4.three"],["1.1980","2.1989","3.1991","4.1990"]]
solutions_list=[4,2,3,3]
fifty_options=[["1.rajitha,2.guidovan russum"],["1.four","2.six"],["1.three","2.five"],["1.1991","2.1980"]]
fifty_solutions=[2,1,2,1]
price=["CONGRATULATIONS!ITS RIGHT ANSWER,YOU WON 1000 RUPEES","GREAT ANSWER","FANSTASTIC","YOU WON THIS GAME"]
eliminate=["SORRY!WRONG ANSWER","BETTER LUCK NEXT TIME","YOU LOSS THIS GAME"]
i=0
index=0
count=0
while i<len(questions_list):
