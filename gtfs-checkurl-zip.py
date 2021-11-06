#-*- using:utf-8 -*-
import urllib.request, urllib.error
import csv
import datetime
import time

def checkURL(url):
  try:
    with urllib.request.urlopen(url) as res:
      #print ("OK: " + url )
      fdate = res.info()['Last-Modified']
      timestamp = datetime.datetime.strptime(fdate, "%a, %d %b %Y %H:%M:%S GMT")
      print(url, fdate, timestamp)
      return timestamp
  except urllib.error.HTTPError as err:
    print("HTTPError: ", err.code)
    return None
  except urllib.error.URLError as err:
    print("URLError: ",err.reason)
    return None
  except:
    return None

if __name__ == '__main__':
  with open('GTFS_fixedURL.csv',encoding='utf-8_sig') as rf:
    reader = csv.DictReader(rf)
    line = [row for row in reader]
    
    with open('GTFS_fixedURL_LastModified.csv', 'w', newline='', encoding='utf-8') as wf:
      writer = csv.writer(wf)
      writer.writerow(['label', 'Last-Modified-GMT', 'url'])
      for row in line:
        url = row['fixed_current_url']
        stmp = checkURL(url)
        print(stmp)
        #if res is not None:
        label = row['label']
        writer.writerow([label, stmp, url])
        time.sleep(1)
  
  print("Finished.")

# cf. https://qiita.com/seigot/items/534ca3089d217200a1d6
# cf. https://qiita.com/sqrtxx/items/49beaa3795925e7de666
