from flask import Blueprint,render_template,request
import requests
from requests.exceptions import MissingSchema
from bs4 import BeautifulSoup
import websiteprojesi.ol,math
from collections import Counter

auth = Blueprint('auth',__name__)

@auth.route('/asama1',methods=['GET','POST'])
def asama1():
      url=request.form.get('url') 
      if url != None:

        print(url)
        text=websiteprojesi.ol.get_text(url)
        soup=websiteprojesi.ol.clean_data(text)
        words=websiteprojesi.ol.count_function(soup)
        
        return render_template("asama1.html",words=words)
      else:
        return render_template("asama1.html")
    
@auth.route('/asama2',methods=['GET','POST'])
def asama2():
  url=request.form.get('url')
  if url!=None:
    text=websiteprojesi.ol.get_text(url)
    keyword,rakepointarray=websiteprojesi.ol.find_keywords(text)
    print(keyword)

    
    
    return render_template("asama2.html",keyword=keyword)
  else:
    return render_template("asama2.html")
            

@auth.route('/asama3',methods=['GET','POST'])
def asama3():
  url1=request.form.get('url1')
  url2=request.form.get('url2')
  if url1!=None:
    
    text=websiteprojesi.ol.get_text(url1)
    text2=websiteprojesi.ol.get_text(url2) 
    keyword1,rakepointarray1=websiteprojesi.ol.find_keywords(text)
    keyword2,rakepointarray2=websiteprojesi.ol.find_keywords(text2)
    x=0
    kok_x=0
    kok_y=0
    for i in range(len(keyword1)):
      for j in range(len(keyword2)):
        if(keyword1[i]==keyword2[j]):
         x+=rakepointarray1[i]*rakepointarray2[j]             
         kok_x+=rakepointarray1[i]*rakepointarray1[i]           
         kok_y+=rakepointarray2[j]*rakepointarray2[j]

    koky=math.sqrt(kok_y)
    kokx=math.sqrt(kok_x)
    value=100*(x/(koky*kokx))



    return render_template("asama3.html",value=value)
  else:
    return render_template("asama3.html")
    

