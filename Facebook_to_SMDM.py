import json
from common_definitions import smdm_comments


#Code for transfering comments
fb_comments = json.load(open("facebook_data/comments.json"))

for c in fb_comments["comments_v2"]:
    # Overwrite temp to new blank comment before appending to comment list
    temp = {
    "media": [],
    "comment_text": "",
    "author": "",
    "media_owner": "",
    "timestamp": ""
    }
    temp["timestamp"] = c["timestamp"]
    temp["comment_text"] = c["data"][0]["comment"]["comment"]
    temp["author"] = c["data"][0]["comment"]["author"]
    lst = c["data"]
    
    #If media if it exists
    if("attachments" in c.keys()):
        for attachment in c["attachments"]:
            for data in attachment["data"]:
                temp["media"].append(data["media"])
                
    #Parse title string to extract media owner
    title = []
    title.append(c["title"])
    title = title[0].split()
    #Parse out 's from names   
    title[len(title)-2] = title[len(title)-2][:-2]
    #Detect "comment on" or "replied to" with key words "on" and "to"
    if("on" in title):
        temp["media_owner"] = title[title.index("on")+1: len(title)-1]     
    elif("to" in title):
        temp["media_owner"] = title[title.index("to")+1: len(title)-1]
 
    smdm_comments["comments"].append(temp)
    #smdm_comments["comment"].append(json.dumps(temp, indent=4)) 
    
#print(smdm_comments)


#Export smdm formatted version
with open('smdm_data/smdm_comments.json', 'w') as f:
    json.dump(smdm_comments, f)    
    f.close()
    #f.write(json.dumps(smdm_comments))

#Received_freind_requests
fb_requests = json.load(open("facebook_data/received_friend_requests.json"))
smdm_requests = {"requests": []}

for r in fb_requests["received_requests_v2"]:
    smdm_requests["requests"].append({
     "name": r["name"],
     "timestamp": r["timestamp"],
     "href": ""
      })

print(smdm_requests)



#Sent_friend_requests
fb_requests = json.load(open("facebook_data/comments.json"))



