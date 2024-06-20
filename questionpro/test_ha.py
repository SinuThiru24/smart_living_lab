from requests import post
import time 



# step 1 scenario 

bearer = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU"

# beim zweiten Mal Leertaste 
def s2(): 
        time.sleep(9)
        url = "http://192.168.68.57:8123/api/services/vacuum/locate"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"entity_id": "vacuum.roborock_s8_pro_ultra"}
        response = post(url, headers=headers, json=data)
        print("Success")

# für s3 
def turn_tv_on():
        url = "http://192.168.68.57:8123/api/services/media_player/turn_on"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"entity_id": "media_player.samsung_the_frame_75_2"}
        response = post(url, headers=headers, json=data)
        print("success")

def turn_tv_off():
        url = "http://192.168.68.57:8123/api/services/media_player/turn_off"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"entity_id": "media_player.samsung_the_frame_75_2"}
        response = post(url, headers=headers, json=data)
        print("success")

def turn_apple_tv_on():
        url = "http://192.168.68.57:8123/api/services/media_player/turn_on"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"entity_id": "media_player.wohnzimmer_2"}
        response = post(url, headers=headers, json=data)
        print("success")

def turn_all_lights_on():
        url = "http://192.168.68.57:8123/api/services/light/turn_on"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"entity_id": ["light.avatar_led", "light.begrussungsbildschirm_led","light.buro_led",
                              "light.esszimmer_hangelampe_oben","light.esszimmer_hangelampe_unten",
                              "light.hue_gradient_lightstrip_3", "light.hue_play_links", "light.hue_play_rechts",
                              "light.kuche_led", "light.luftreiniger_led", "light.schreibtischlampe", "light.stehlampe_links",
                              "light.stehlampe_rechts", "light.tv_led","light.wohnzimmer_hangelampe", "light.wohnzimmer_lampe"],
        "color_name": "mediumseagreen"}
        response = post(url, headers=headers, json=data)
        print("success")

def turn_all_lights_off():
        url = "http://192.168.68.57:8123/api/services/light/turn_off"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"entity_id": ["light.avatar_led", "light.begrussungsbildschirm_led","light.buro_led",
                              "light.esszimmer_hangelampe_oben","light.esszimmer_hangelampe_unten",
                              "light.hue_gradient_lightstrip_3", "light.hue_play_links", "light.hue_play_rechts",
                              "light.kuche_led", "light.luftreiniger_led", "light.schreibtischlampe", "light.stehlampe_links",
                              "light.stehlampe_rechts", "light.tv_led","light.wohnzimmer_hangelampe", "light.wohnzimmer_lampe"]}
        response = post(url, headers=headers, json=data)
        print("success")

def sync_state_hue(mode: str):
        url = "http://192.168.68.57:8123/api/services/huesyncbox/set_sync_state"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"device_id": "42501425aaaad9ecbe9a6353b40b621d",
                "brightness": 99,
                "intensity": "high",
                "mode": mode,
                "input": "input4",
                "power": "true",
                "sync": "true"}
        response = post(url, headers=headers, json=data)
        print("success")
        
#beim dritten Mal Leertaste
def s3(mode_s3: str):
        time.sleep(20)
        turn_tv_on()
        time.sleep(1)
        turn_tv_on()
        time.sleep(7)
        turn_all_lights_on()
        time.sleep(6)
        turn_all_lights_off()
        sync_state_hue(mode_s3)
        turn_apple_tv_on()

def play_media(content: str):
        url = "http://192.168.68.57:8123/api/services/media_player/play_media"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"entity_id": "media_player.wohnzimmer_2",
                "media_content_id": content,
                "media_content_type": "url"}
        response = post(url, headers=headers, json=data)
        print("success")

# beim vierten Mal Leertaste
def s4(content_id: str):
        time.sleep(21)
        play_media(content_id)

def s8(mode_s8: str, content_s8: str):
        time.sleep(31)
        sync_state_hue(mode_s8)
        play_media(content_s8)
        time.sleep(60)
        turn_tv_off()
        turn_all_lights_off()

s2()
s3("video")
s4("youtube://www.youtube.com/watch?v=TXX4Px197ug")
s8("music", "youtube://www.youtube.com/watch?v=gRlj5vjp3Ko")
