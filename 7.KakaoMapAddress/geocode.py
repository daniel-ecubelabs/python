import json
import sys
import pandas as pd
import requests
from datetime import *

#전역변수
tracker_data = 'sample.csv'
location_data = 'location.csv'
APP_KEY = '개인키입력'
URL = 'https://dapi,kakao.com/v2/local/geo/coord2regioncode.json'

df_all = pd.read_csv(tracker_data, encoding='euc-kr')
df = df_all[['idx','lon','lat']]

def json_request(url='', encoding='utf-8', success=None, error=lambda e:print('%s : %s' %(e, datetime.now()), file=sys.stderr)):
    headers = {'Authorization' : 'KakaoAK{}'.format(APP_KEY)}
    resp = requests.get(url, headers=headers)
    print('%s : success for request [%s]' % (datetime.now(), url))
    return resp.text

    
def reverse_geocode(longitude, latitude):
    url = '%s?x=%s&y=%s' %(URL, longitude, latitude)
    #json request
    try:
        json_req = json_request(url=url)
        json_data = json_loads(json_req)
        json_doc = json_data.get('documents')[0]
        json_name = json_doc.get('address_name')
        #json_name = json_doc.get('region_3depth_name')
    except:
        json_name = 'NaN'

    return json_name


def get_address(x, y):
    address = []
    json_name = reverse_geocode(x,y)
    address.append(json_name)
    return address


def main():
    #파일 읽기
    data = pd.read_csv(tracker_data, encoding='euc-kr')
    location = pd.read_csv(location_data, encoding='euc-kr')

    address = get_address(data)
    data = preprocess(data, address, location)

    #최종 파일 저장
    data.to_csv('%s_final.csv' %(tracker_data[:-4]), spe=',', encoding='euc-kr')

if __name__ == '__main__':
    main()


    for i in range(len(df)):
        x_crd = float(df.loc[i,['lat']])
        print('x=%f' %(x_crd))
        y_crd = float(df.loc[i,['lon']])
        print('y=%f' %(y_crd))
        address = get_address(x_crd, y_crd)
        print('addr=%s' %(address))
        df.loc[i,['addr']] = address
        
    #location = pd.read_csv(location_data, encoding='euc-kr')

    
