date = input('Enter Date of Birth(dd/mm/yyyy) : ')
date= list(map(int,date.split('/')))

date_dict = {'date':d[0] , 'month':d[1] , 'year':d[2]}

month_list = {1:1, 2:4, 3:4,4:0,5:2, 6: 5, 7:0, 8:3, 9:6, 10:1, 11:4, 12:6} 
year_list = {17:4, 18:2, 19:0, 20:6}
week_day = {1:'Sunday',2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 0:'Saturday'}

day = date_dict['date']
month = date_dict['month']
year = date_dict['year']
son = year%100

key = year
key//=4
key += date
key += month_list[month]
key += year_list[year//100]

if son%4==0:
	key -= 1

key += son
key%=7
print ('You were born on',weak_day[key])
