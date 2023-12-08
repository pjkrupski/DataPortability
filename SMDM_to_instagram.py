import json
from common_definitions import smdm_comments, instagram_comments

f = open('smdm_data/smdm_comments.json')

data = json.load(f)



#Transform SMDM comments to Instagram comments
lst = instagram_comments
for c in data["comments"]:
    #Defines new instagram comment
    instagram_comment = {
    "media_list_data": c["media"],
  "string_map_data": {
    "Comment": {
      "value": c["comment_text"]
    },
    "Media Owner": {
      "value": c["media_owner"]
    },
    "Time": {
      "timestamp": c["timestamp"]
    }
  }    
}
    lst["comments"].append(instagram_comment)

print(lst["comments"][0])

#Export instagram formatted version
with open('instagram_data/instagram_comments.json', 'w') as f:
    json.dump(lst, f)    
    f.close()
    #f.write(json.dumps(smdm_comments))

