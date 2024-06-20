from requests import post
import time 
from jsandha import to_do_list
from pynput.keyboard import Key, Listener


ha_variablen = to_do_list
print("finale to do liste: ", ha_variablen)


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

# für s4 und folgende, media playen 
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

# beim achten Mal Leeertaste
def s8(mode_s8: str, content_s8: str):
        time.sleep(31)
        sync_state_hue(mode_s8)
        play_media(content_s8)
        time.sleep(60)
        turn_tv_off()
        turn_all_lights_off()
        
def diffuser(diff: str, option: str):
        url = "http://192.168.68.57:8123/api/services/select/select_option"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"entity_id": diff,
                "option": option}
        response = post(url, headers=headers, json=data)
        print("success")

def diffuser_light_turn_on(diff_dev_id: str, rgb: list):
        url = "http://192.168.68.57:8123/api/services/light/turn_on"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"device_id": diff_dev_id,
                "rgb_color": rgb,
                "brightness": 255}
        response = post(url, headers=headers, json=data)
        print("success")

def diffuser_light_turn_off(diff_dev_id: str):
        url = "http://192.168.68.57:8123/api/services/light/turn_off"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"device_id": diff_dev_id}
        response = post(url, headers=headers, json=data)
        print("success")
        
# entity ids duft
#lemongras select.smart_humidifier_2306278478273164110148e1e9cb8cdb_spray
#lavendel select.smart_humidifier_2306274491270164110148e1e9cb8f24_spray
#pfefferminz select.diffuser_3_spray

#für s9



#beim neunten Mal Leertaste
# als Variablen nur Diffuser Device ID, RGB List und Entity ID durchgeben
def s9(diff_s9: str):
        diffuser(diff_s9, "on")

def s10(diff_s9_2: str, rgb_set: list, diff_s9_dev: str):
        diffuser_light_turn_on(diff_s9_dev,rgb_set)
        time.sleep(45)
        diffuser(diff_s9_2, "off")
        diffuser_light_turn_off(diff_s9_dev)


        
#s9("select.smart_humidifier_2306274491270164110148e1e9cb8f24_spray", [140,8,122],"838bd2e21f0bc6e752fc66f00e897a32")

def activate_scene(scene: str):
        url = "http://192.168.68.57:8123/api/services/scene/turn_on"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"entity_id": scene}
        response = post(url, headers=headers, json=data)
        print("success")

def s11(scene_s10: str):
        time.sleep(16)
        activate_scene(scene_s10)

#s11("scene.esszimmer_strahlend")

def s16(scene_s11_ess: str, scene_s11_bur: str, scene_s11_wohn: str):
        time.sleep(15)
        activate_scene(scene_s11_ess)
        activate_scene(scene_s11_bur)
        activate_scene(scene_s11_wohn)

#s16("scene.esszimmer_strahlend", "scene.buro_strahlend", "scene.wohnzimmer_strahlend")

def s18(movie: str):
        sync_state_hue("video")
        turn_tv_on()
        turn_apple_tv_on()
        play_media(movie)
        
#s18("youtube://www.youtube.com/watch?v=DhiQlnBzk3U")   

def roborock_cleaning():
        url = "http://192.168.68.57:8123/api/services/vacuum/start"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"entity_id": "vacuum.roborock_s8_pro_ultra"}
        response = post(url, headers=headers, json=data)
        print("Success")

def roborock_docking():
        url = "http://192.168.68.57:8123/api/services/vacuum/return_to_base"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"entity_id": "vacuum.roborock_s8_pro_ultra"}
        response = post(url, headers=headers, json=data)
        print("Success")

def luftreiniger_led_on():
        url = "http://192.168.68.57:8123/api/services/light/turn_on"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"entity_id": "light.luftreiniger_led",
                "rgb_color": [255,180,63]}
        response = post(url, headers=headers, json=data)
        print("success")

def luftreiniger_led_off():
        url = "http://192.168.68.57:8123/api/services/light/turn_off"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"entity_id": "light.luftreiniger_led"}
        response = post(url, headers=headers, json=data)
        print("success")

def luftreiniger_turn_on():
        url = "http://192.168.68.57:8123/api/services/fan/turn_on"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"device_id": "476ae2c0f67ace9a51769d82d4154efa"}
        response = post(url, headers=headers, json=data)
        print("success")

def luftreiniger_turn_off():
        url = "http://192.168.68.57:8123/api/services/fan/turn_off"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzFjZTZhYTU5ZDI0NWNlOGZhNmU3OTg1ZmNjNWQzZSIsImlhdCI6MTcxNzA3MzA5NSwiZXhwIjoyMDMyNDMzMDk1fQ.8bHc3y6dhWrD9JS49ioam6j7rUyqJ7FBjQkwzJk7CGU" }
        data = {"device_id": "476ae2c0f67ace9a51769d82d4154efa"}
        response = post(url, headers=headers, json=data)
        print("success")


        

def s19():
        turn_tv_off()
        turn_all_lights_off()
        time.sleep(45)
        roborock_cleaning()
        luftreiniger_led_on()
        luftreiniger_turn_on()
        time.sleep(45)
        roborock_docking()
        luftreiniger_turn_off()
        luftreiniger_led_off()
        time.sleep(5)
        roborock_docking()

#s19()

count=0

diffuser_s9 = str
rgb_set_s9 = list
diffuser_s9_device = str

if ha_variablen[3] == "lemongras":
        diffuser_s9 = "select.smart_humidifier_2306278478273164110148e1e9cb8cdb_spray"
        rgb_set_s9 = [78,207,23]
        diffuser_s9_device = "7db5ea279b69b2923eb7b1786024a865"
elif ha_variablen[3] == "pfefferminz":
        diffuser_s9 = "select.diffuser_3_spray"
        rgb_set_s9 = [0,179,255]
        diffuser_s9_device = "86816fdc160eb20107b9c7edc2f2b4dc"
elif ha_variablen[3] == "lavendel":
        diffuser_s9 = "select.smart_humidifier_2306274491270164110148e1e9cb8f24_spray"
        rgb_set_s9 = [140,8,122]
        diffuser_s9_device = "838bd2e21f0bc6e752fc66f00e897a32"
        

wohnzimmer_scene = str
esszimmer_scene = str
buro_scene = str
if ha_variablen[2] == "bernsteinblüte": 
        wohnzimmer_scene = "scene.wohnzimmer_bernsteinblute"
        esszimmer_scene = "scene.esszimmer_bernsteinblute"
        buro_scene = "scene.buro_bernsteinblute"
elif ha_variablen[2] == "blüte": 
        wohnzimmer_scene = "scene.wohnzimmer_blute"
        esszimmer_scene = "scene.esszimmer_blute"
        buro_scene = "scene.buro_blute"
elif ha_variablen[2] == "strahlend": 
        wohnzimmer_scene = "scene.wohnzimmer_strahlend"
        esszimmer_scene = "scene.esszimmer_strahlend"
        buro_scene = "scene.buro_strahlend"
elif ha_variablen[2] == "nordlichter": 
        wohnzimmer_scene = "scene.wohnzimmer_nordlichter"
        esszimmer_scene = "scene.esszimmer_nordlichter"
        buro_scene = "scene.buro_nordlichter"
elif ha_variablen[2] == "galaxie": 
        wohnzimmer_scene = "scene.wohnzimmer_galaxie"
        esszimmer_scene = "scene.esszimmer_galaxie"
        buro_scene = "scene.buro_galaxie"
elif ha_variablen[2] == "smaragd-insel": 
        wohnzimmer_scene = "scene.wohnzimmer_smaragd_insel"
        esszimmer_scene = "scene.esszimmer_smaragd_insel"
        buro_scene = "scene.buro_smaragd_insel"
elif ha_variablen[2] == "memento": 
        wohnzimmer_scene = "scene.wohnzimmer_memento"
        esszimmer_scene = "scene.esszimmer_memento"
        buro_scene = "scene.buro_memento"
elif ha_variablen[2] == "scharlachroter traum": 
        wohnzimmer_scene = "scene.wohnzimmer_scharlachroter_traum"
        esszimmer_scene = "scene.esszimmer_scharlachroter_traum"
        buro_scene = "scene.buro_scharlachroter_traum"
elif ha_variablen[2] == "hal": 
        wohnzimmer_scene = "scene.wohnzimmer_hal"
        esszimmer_scene = "scene.esszimmer_hal"
        buro_scene = "scene.buro_hal"
elif ha_variablen[2] == "bergbrise": 
        wohnzimmer_scene = "scene.wohnzimmer_bergbrise"
        esszimmer_scene = "scene.esszimmer_bergbrise"
        buro_scene = "scene.buro_bergbrise"

#Key.space
def on_press(key):
    global count
    if key == Key.space: 
        count +=1
        print(count)
        if count == 2:
                s2()
        elif count == 3:
                s3("video")
        elif count == 4:
                s4(ha_variablen[0])
        elif count == 8: 
                s8("music", ha_variablen[1])
        elif count == 9: 
                s9(diffuser_s9)
        elif count == 10: 
                s10(diffuser_s9, rgb_set_s9, diffuser_s9_device)
        elif count == 11: 
                s11(esszimmer_scene)
        elif count == 16: 
                s16(esszimmer_scene, buro_scene, wohnzimmer_scene)
        elif count == 18: 
                s18(ha_variablen[4])
        elif count == 19: 
                s19()
        
        


def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
        

        
        
        

##DIFFUSER

# 78,207,23 lemongras diffuser
# lemongras diffuser 7db5ea279b69b2923eb7b1786024a865

# 140,8,122 lavendel
# lavendel diffuser 838bd2e21f0bc6e752fc66f00e897a32
# 0,179,255 pfefferminuz 
# pfefferminz diffuser 86816fdc160eb20107b9c7edc2f2b4dc


        
        
        

        
        





