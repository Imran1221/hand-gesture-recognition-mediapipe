from requests import post

url = "http://192.168.178.118:8123/api/services/media_player/play_media"
headers = {"Authorization": "Bearer <TOKEN>"}
data = {"entity_id": "media_player.imrans_echo_dot", "media_content_id": "Stop", "media_content_type": "custom"}
response = post(url, headers=headers, json=data)
print(response.text)

