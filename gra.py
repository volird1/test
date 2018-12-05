a = "plemię nadwodne"
b = "plemię ziemi"
c = "plemię górskie"

print("wpisz literę plemiona od a do c, aby zapoznać sie z opisem plemion")
wybor = input()

if wybor == "a":
 print('''Od teraz jesteś wojownikiem plemiona wody, twoje tereny leżą wzdłuż morza [nazwa morza]. 
 Twoje plemię żyje z rybołóstwa. 
 Jedną z zalet twojego plemiona jest posiadanie floty handlowej i wojennej. 
 Umiesz świetnie walczyć na morzu i radzisz sobie na lądzie.''')
 wybor = input()


if wybor == "b":
 
  print ('''Od teraz jestes wojownikiem ziemi, twoje tereny to ziemia[nazwa ziemi]. Twoim terenem są wszystkie lasy i  
  łaki. Utrzymujesz się z rolnictwa. W twój dorobek wchodzą rózne kopalnie i huty i warsztaty.''')
  wybor = input()


if wybor == "c":

  print ('''Twoje tereny są w górach [nazwa gór]. Twoimi zaletami jest budowanie warowni w trudno dostępnych miejscach wysoko w górach. Twoi wojownicy są wytrzymali na duży wysiłek fizyczny ''')
  
  

plemiona = input("podaj wybrane plemię a-plemię nadwodne b-plemię ziemi c-plemię górskie")
if plemiona == 'a':
  print("plemie nadwodne" )
if plemiona == 'b':
  print("plemie ziemi" )
if plemiona == 'c':
  print("plemie górskie" 
