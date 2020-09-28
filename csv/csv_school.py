import csv

with open('한국교원대학교_초중고등학교위치_20200320.csv', 'r') as f:
    cells = csv.DictReader(f)
    new_cells = "학교명,소재지도로명주소,위도,경도\n"

    for k in cells:
        if '경상남도 창원' in k['소재지도로명주소']:
            new_cells += "%s,%s,%s,%s\n" % (k['학교명'], k['소재지도로명주소'], k['위도'], k['경도'])

with open('한국교원대학교_초중고등학교위치_창원시_20200320.csv', 'w', newline='') as f:
    f.write(new_cells)

    
