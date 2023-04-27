import requests
import json
import datetime
import csv


TOKEN = 'NWMyYmZlOTItZTkxOS00OGJiLThmOTQtMWE1ZjdiNjg5Mzc5'  # M3O access token


def days_until(dt_str):
    dt = datetime.date.fromisoformat(dt_str)
    delt = dt - datetime.date.today()
    return delt.days


def get_country_codes():
    codes = {}  # country -> code
    url = 'https://api.m3o.com/v1/holidays/Countries'
    headers = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + TOKEN }  
    parameters = {}
    response = requests.get(url, params=parameters, headers=headers)
    data = json.loads(response.text)
    for country in data['countries']:
        code = country ['code']
        name = country ['name']
        codes[name] = code

    
    return codes


def get_holidays(country_code, horizon=None):
    holiday_tups = []  # [ (date1, holiday1), (date2, holiday2), ... ]
    url = 'https://api.m3o.com/v1/holidays/List'
    headers =  { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + TOKEN }
    parameters ={'country_code': country_code, 'year': 2022} 
    response = requests.get(url,params=parameters, headers=headers)
    data = json.loads(response.text)

    for country in data['holidays']:
        if ((days_until(country['date'])>0) and (days_until(country['date'])< horizon)):
            holiday_tups.append((country['date'],country['local_name']))
    
    return holiday_tups


def get_forecasts(loc):
    url = 'https://api.m3o.com/v1/weather/Forecast' 
    headers =  { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + TOKEN }
    parameters ={'days' : 10, 'location' : loc} 
    response = requests.get(url,params=parameters, headers=headers)
    data = json.loads(response.text)
    forecasts = {}  # date -> forecast
    
    if("forecast" not in data):
        return forecasts
    for country in data['forecast']:
        forecasts[country['date']] = country['condition']
    

    return forecasts
    


def write_upcoming_holidays(holiday_dict, filepath):
    write_count = 0
    
    f = open(filepath,encoding='utf-8', mode="w")
    f.write("country, date, holiday, forecast\n")
    for each in holiday_dict:
        data = holiday_dict[each]
        
        for holiday in data:
            print(each)
            print(data)
            text = each + "," + holiday[0] + ","+ holiday[1] + "," + holiday[2] + "\n"
            f.write(text)
            write_count+=1

    
    f.close()
    
    return write_count


##########################

if __name__ == '__main__':
    # Get all the available countries
    country_codes = get_country_codes()  # country -> code 
    # For each one, grab their upcoming holidays and weather forecasts
    country_holidays = {}  # country -> [ (dt1, hol1, for1), (dt2, hol2, for2), ... ]
    for country, cc in country_codes.items():
        print("checking holidays and weather for", country, "(" + cc + ")")
        holiday_tups = get_holidays(cc, 10)  # list: [ (date1, holiday1), (date2, holiday2), ... ]
        forecasts = get_forecasts(country)  # dict: date -> forecast
        
        if holiday_tups:
            print("\tfound", len(holiday_tups), "holidays")
            country_holidays[country] = []
            for dt, name in holiday_tups:
                country_holidays[country].append((dt, name, forecasts[dt]))

    # Write out the results to a file

    write_upcoming_holidays(country_holidays, "upcoming_holidays.csv")
