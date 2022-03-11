import requests
from requests.exceptions import MissingSchema
from bs4 import BeautifulSoup
from collections import Counter
import operator
import re
from operator import itemgetter
from rake_nltk import Rake
from nltk.corpus import stopwords 
import nltk
def get_text(url):
    try:
      data=requests.get(url).text 
      text=BeautifulSoup(data,'html.parser').text
    except MissingSchema:
      print('URL is not complete')
    return text  
def clean_data(soup):
    try:
      soup=soup.lower()
      soup = soup.encode('ascii', 'ignore').decode()
      print(soup)
      print("*****************************************************************************************")
      soup=re.split('[{ }\n;.,!?():=<>/&\t:" "''""\r-]',soup)
      t=0
      result = []
      for item in soup:
        if len(item)!=0:
          result.append(item)
      soup = result

    except MissingSchema:
      print('URL is not complete')
    return soup
    
def count_function(soup):
    try:
      print(soup)
      words=Counter(soup)
      print("-------------------------")
      print(words)
      sortword=sorted(words.items(), key=lambda words: words[1], reverse = True)
    except MissingSchema:
      print('URL is not complete')
    return sortword

def find_keywords(text):
  nltk.download("stopwords")
  stop_words = set(stopwords.words("english"))
  text= text.encode('ascii', 'ignore').decode()
  words=clean_data(text)
  clean_array=[]
  clean_array_freq=[]
  degree_array=[]
  word_array=[]
  degree_str=""
  letter_str=""
  hold_str=""
  point_str=""
  hold=0
  t=0
  booleanarray=True 
  deg_array=[]
  ol_array=[]
  imp_array=[]
  rake_array=[]
  num=0
  number=0
  degree_num=0
  degree_point=0
  rakepoint_array=[]
  z=0
  for word in words:
    for stopword in stop_words:
      if word!=stopword:
         hold=hold+1
      else:
        hold=0
        for x in clean_array:
          degree_str+=x+" "  
        degree_array.append(degree_str)
        degree_str=""                                     
        clean_array=[]             
        break                           
   
    if(hold==len(stop_words)):
      clean_array.append(word)
      clean_array_freq.append(word)
      hold=0
  print("-------------------------------")
  print(degree_array)
  for words in degree_array:
    for letter in words:
     
     
      if letter!=" ":
         letter_str+=letter
      else:
        word_array.append(letter_str)
        letter_str=""
    
    
    if len(word_array)!=0:
        for i in word_array:
         for j in word_array:
           if i==j:
            num+=1
        
        if num<=len(word_array):
          imp_array.append(word_array)
        num=0

    word_array=[]  
  print("*******")  
  print(imp_array)
  
  count_dict=count_function(clean_array_freq)
  for words in imp_array:
    for word in words:
      for i in range(len(count_dict)):
        if count_dict[i][0]==word:
           degree_num+=count_dict[i][1]
    degree_point=degree_num/len(words)
    words.append(degree_point)
    rake_array.append(words)
    

     
    degree_num=0
    
  print(len(imp_array))
  for i in range(len(rake_array)):                             
      for j in range(i+1,len(rake_array)):
        if(rake_array[i][len(rake_array[i])-1]<rake_array[j][len(rake_array[j])-1]):
          temp=rake_array[i][len(rake_array[i])-1]
          rake_array[i][len(rake_array[i])-1]=rake_array[j][len(rake_array[j])-1]
          rake_array[j][len(rake_array[j])-1]=temp

  print(rake_array)
  keyword_len=int((len(imp_array)-(len(imp_array)%10))/10)
  keyword_txt=""
  keyword_array=[]
  for i in range(keyword_len):
    for word in rake_array[i]:
      print(word)
      if word!=rake_array[i][len(rake_array[i])-1]:
        keyword_txt+=word+" "
      else:
        rakepoint_array.append(word)
      
    for i in range(len(keyword_array)):
      for j in range(i+1,len(keyword_array)):
          if keyword_array[i]==keyword_array[j]:
            keyword_array.pop(i)
            rakepoint_array.pop(i)

    keyword_array.append(keyword_txt)
    keyword_txt=""
      
  print(keyword_array)
  

  
  return keyword_array,rakepoint_array

  