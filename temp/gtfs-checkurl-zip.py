#-*- using:utf-8 -*-
import urllib.request, urllib.error
import csv
import time
from datetime import datetime, timedelta, timezone
import pytz

def checkURL(url):
  try:
    with urllib.request.urlopen(url) as res:
      headers = res.info()
      #print(headers)
      if 'Last-Modified' in headers:
        gmt_str = datetime.strptime(headers['Last-Modified'], "%a, %d %b %Y %H:%M:%S %Z").replace(tzinfo=pytz.utc)
        gmt = gmt_str.timestamp()
        tz = timezone(timedelta(hours=+9), 'JST')
        timestamp = str(datetime.fromtimestamp(gmt, tz))[:-9]
        #print(url, gmt, gmt_str, timestamp)
      else:
        timestamp = ""
      return timestamp
  except urllib.error.HTTPError as err:
    print("HTTPError: ", err.code, url)
    return None
  except urllib.error.URLError as err:
    print("URLError: ",err.reason, url)
    return None
  except Exception as err:
    print("Error: ",err,url)
    return None

if __name__ == '__main__':
  with open('GTFS_fixedURL.csv',encoding='utf-8_sig') as rf:
    reader = csv.DictReader(rf)
    line = [row for row in reader]
    
    with open('GTFS_fixedURL_LastModified.csv', 'w', newline='', encoding='utf-8') as wf:
      writer = csv.writer(wf)
      writer.writerow(['label', 'Last-Modified-JST', 'url', 'license_name'])
      for row in line:
        url = row['fixed_current_url']
        stmp = checkURL(url)
        #print(stmp)
        #if res is not None:
        label = row['label']
        license = row['license_name']
        writer.writerow([label, stmp, url, license])
        time.sleep(1)
  
  print("Finished.")

# cf. https://qiita.com/seigot/items/534ca3089d217200a1d6
# cf. https://qiita.com/sqrtxx/items/49beaa3795925e7de666
