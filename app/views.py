from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
import pandas as pd 

start_row=18
end_row=110
stations=pd.read_csv('static\data_small\stations.txt',skiprows=range(start_row-1),nrows=end_row-start_row)
#print(stations)
stations=stations[["STAID","STANAME                                 "]]


def home(request):
  data=stations.to_html()
  d={"data":data}
  return render(request,'home.html',d)

def one_stat_one_date(request,station,date):
  filename="static\data_small\TG_STAID" + str(station).zfill(6) + '.txt'

  try:
    df=pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])

  except FileNotFoundError:
    return HttpResponse("Station does not exist")
  
  else:
    temp=df.loc[df["    DATE"]==date]["   TG"].squeeze()/10
    station,date=station,date
    if date in str(df["    DATE"]):
      return JsonResponse({"station":station,
            "temperature":temp,
            "date":date})
    else:
        return HttpResponse("Data for this date does not exist")


def one_stat_all_dates(request,station):
  filename="static\data_small\TG_STAID" + str(station).zfill(6) + ".txt"

  try:
    df=pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])

  except FileNotFoundError:
    return HttpResponse("Station doesnot exist")
  
  else:
    df['    DATE'] = df['    DATE'].astype(str)
    data = df.to_dict(orient="records")
    return JsonResponse(data,safe=False,json_dumps_params={'indent': 4})
    

def one_stat_one_year(request,station,year):
  filename="static\data_small\TG_STAID" + str(station).zfill(6) + '.txt'

  try:
    df=pd.read_csv(filename,skiprows=20)
    
  except FileNotFoundError:
    return HttpResponse("Station does not exist")
  
  else:
    df["    DATE"]=df["    DATE"].astype(str)
    result=df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    if result:
      return JsonResponse(result,safe=False,json_dumps_params={'indent': 4})
    else:
      return HttpResponse("Data for this year does not exists")
  
  

# Create your views here.
