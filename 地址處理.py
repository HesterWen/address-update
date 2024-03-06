import csv

with open('地址資料.csv', encoding='utf-8') as infile:
    data = list(csv.DictReader(infile))
    for e in data:
        print('原始資料:', e['姓名'], e['縣市'], e['住址'])
        if e['縣市'][0] == '台':
            e['縣市'] = '臺' + e['縣市'][1:]
        if 'F' in e['住址']:
            e['住址'] = e['住址'].replace('F', '樓')
        if e['縣市'] == '臺中市' and '中港路' in e['住址']:
            e['住址'] = e['住址'].replace('中港路', '臺灣大道')
        
        print('    更新資料:', e['姓名'], e['縣市'], e['住址'])

with open('新地址資料.csv', 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames = data[0].keys())
    writer.writeheader()
    for e in data:
        writer.writerow(e)            



