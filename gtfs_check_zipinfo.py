import io
import urllib.request, urllib.error
import zipfile
import csv
import time
from datetime import datetime, timedelta, timezone
import pytz
import pprint

def checkURL(url):
  try:
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
      headers = res.info()
      #print(headers)
      if 'Last-Modified' in headers:
        gmt_str = datetime.strptime(headers['Last-Modified'], "%a, %d %b %Y %H:%M:%S %Z").replace(tzinfo=pytz.utc)
        gmt = gmt_str.timestamp()
        tz = timezone(timedelta(hours=+9), 'JST')
        timestamp = str(datetime.fromtimestamp(gmt, tz))[:-9]
        #print(url, gmt, gmt_str, timestamp)
      else:
        timestamp = ''

      # zipファイル本体読込
      buff = res.read()
      with zipfile.ZipFile(io.BytesIO(buff), 'r') as zip_data:
      # with zipfile.ZipFile(url, 'r') as zip_data:
        flg = 0
        filepath = ''
        for name in zip_data.namelist():
          if 'feed_info.txt' in name:
            filepath = name
            flg = 1
            break

        if flg == 1:
          with zip_data.open(filepath, 'r') as bin_txt:
            buff_txt = bin_txt.read()
            txt_file = buff_txt.decode('utf-8_sig')
            
            with io.StringIO() as f:
              f.write(txt_file)
              f.seek(0)
              csv_reader = csv.DictReader(f)
              line = [row for row in csv_reader]
              # pprint.pprint(line)
      
      return timestamp, line
  except urllib.error.HTTPError as err:
    print("HTTPError: ", err.code, url)
    return None, []
  except urllib.error.URLError as err:
    print("URLError: ",err.reason, url)
    return None, []
  except Exception as err:
    print("Error: ",err,url)
    return None, []

if __name__ == '__main__':
  with open('GTFS_fixedURL.csv',encoding='utf-8_sig') as rf:
    reader = csv.DictReader(rf)
    listline = [row for row in reader]
    # print(listline)
    
    with open('GTFS_fixedURL_LastModified.csv', 'w', newline='', encoding='utf-8') as wf:
      writer = csv.writer(wf)
      writer.writerow(['label', 'Last-Modified-JST', 'url', 'license_name', 'feed_publisher_name', 'feed_start_date', 'feed_end_date', 'feed_version'])
      
      for row in listline:
        url = row['fixed_current_url']
        print(url)
        result = checkURL(url)
        # print(result[0], result[1])
        if result[0] is not None:
          label = row['label']
          stmp = result[0]
          license = row['license_name']

          fpname = result[1][0].get('feed_publisher_name')
          start = result[1][0].get('feed_start_date')
          end = result[1][0].get('feed_end_date')
          ver = result[1][0].get('feed_version')
        else:
          label = ''
          stmp = ''
          license = ''
          fpname = ''
          start = ''
          end = ''
          ver = ''
        writer.writerow([label, stmp, url, license, fpname, start, end, ver])
        time.sleep(1)
  
  print("Finished.")
