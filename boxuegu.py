import json
with open("django-天天新鲜项目.txt",encoding="utf-8") as file1:
    target_video_str = file1.readlines()
    
target_video_json = json.loads(''.join(target_video_str))
target_video_format_list = []
for x in target_video_json['result']['sectionItems']:
    items = {}
    items['sectionId'] = x['sectionId']
    items['dirnames'] = x['sectionName']
    items['video_info'] = []
    for x1 in x['pointItems']:
        video_items = {}
        video_items['file_name'] =  x1['pointName']
        video_items['urls'] = x1['ccVideoId']
        items['video_info'].append(video_items)
        
    target_video_format_list.append(items)    
    
   
   target_video_format_list_copy = target_video_format_list[10:]

##采用切片的方式割开数据

request_url_head = "https://p.bokecc.com/servlet/app/playinfo?dt=iPhone&hlssupport=1&mediatype=&osversion=11.4&sh=667&sn=C343459A-C62A-4E4F-AC59-FA5D240B698B&sw=375&userid=78665FEF083498AB&version=20140214&videoid="
request_url_end = "&time=1532068860629&hash=3A1F5ED0D92D8FA4E1134E80994608CE"

for x in target_video_format_list_copy:
    print(x['dirnames'])
    for x1 in x['video_info']:
        print(x1['file_name'],x1['urls'])
    print()
    
  
