def get_date():
	date = input('Enter Date of Birth(dd/mm/yyyy) : ')
	date= list(map(int,date.split('/')))
	date_dict = {'date':date[0] , 'month':date[1] , 'year':date[2]}
	return date_dict

def get_key(date_dict, month_list, year_list):
	day = date_dict['date']
	month = date_dict['month']
	year = date_dict['year']
	son = year%100

	key = son
	key//=4
	key += day
	key += month_list[month]
	key += year_list[year//100]

	if son%4==0 and (month==1 or month==2):
		key -= 1

	key += son
	key%=7
	return key

if __name__=='__main__':
	
	date_dict = get_date()

	month_list = {1:1, 2:4, 3:4,4:0,5:2, 6: 5, 7:0, 8:3, 9:6, 10:1, 11:4, 12:6}
	year_list = {17:4, 18:2, 19:0, 20:6}
	weak_day = {1:'Sunday',2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 0:'Saturday'}
	
	key = get_key(date_dict, month_list, year_list)
	print ('You were born on',weak_day[key])
