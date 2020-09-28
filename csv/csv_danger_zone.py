import csv
from pyproj import Proj, transform


# UTM-K
proj_UTMK = Proj(init='epsg:5178') # UTM-K(Bassel) 도로명주소 지도 사용 중

# WGS1984
proj_WGS84 = Proj(init='epsg:4326') # Wgs84 경도/위도, GPS사용 전지구 좌표

with open('링크기반 사고위험지역.csv', 'r') as f:
    cells = csv.DictReader(f)
    new_cells = "시도명,폴리곤,경도,위도\n"

    for k in cells:
        x, y = transform(proj_UTMK, proj_WGS84, k['중심점UTMK X좌표'], k['중심점UTMK Y좌표'])
        new_cells += "%s,%s,%s,%s\n" % (k['시도명'], k['폴리곤'].replace(',', '/'), x, y)

with open('링크기반_사고위험지역_창원시.csv', 'w', newline='') as f:
    f.write(new_cells)

    
