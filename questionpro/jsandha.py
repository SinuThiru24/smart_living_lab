from auswertung_test import messages_ki_avatar, to_do_list
import re
from openai import OpenAI
import os 
import shutil
from datetime import datetime



js_data = messages_ki_avatar

#### App js vom Desktop in App.txt

src_file = "/Users/citai-livinglab/Desktop/App.js"

destination_folder = os.path.join(os.getcwd(), "App (copy).js")

dest = shutil.copy2(src_file, destination_folder)

os.rename(destination_folder, os.path.join(os.getcwd(),"App.txt"))



with open("App.txt", "r") as file:
    data = file.read()

client = OpenAI(
  api_key="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",
)

discussions=[{"role": "system", 
              "content": "Du bist eine hilfreiche KI"}]

list_of_questions = []
list_of_questions.append("Schaue dir bitte den folgenden Code an, veraendere aber nichts: " + data)
list_of_questions.append("Ersetze bitte den Text bei case 0 durch den folgenden Text: " + js_data[0]+ " Ersetze bitte den Text bei case 1 durch den folgenden " + 
                         "Text: " + js_data[1] + " Ersetze bitte den Text bei case 2 durch den folgenden Text: " + js_data[2] + 
                         " Ersetze bitte den Text bei case 3 durch den folgenden Text: " + js_data[3] + " Ersetze bitte den Text bei case 4 durch den folgenden Text: " + js_data[4] +
                         " Ersetze bitte den Text bei case 5 durch den folgenden Text: " + js_data[5] + " Ersetze bitte den Text bei case 6 durch den folgenden Text: " + js_data[6] +
                         " Ersetze bitte den Text bei case 7 durch den folgenden Text: " + js_data[7] + " Ersetze bitte den Text bei case 8 durch den folgenden Text: " + js_data[8] + 
                         " Ersetze bitte den Text bei case 9 durch den folgenden Text: " + js_data[9] + " Ersetze bitte den Text bei case 10 durch den folgenden Text: " + js_data[10] + 
                         " Ersetze bitte den Text bei case 11 durch den folgenden Text: " + js_data[11] + " Ersetze bitte den Text bei case 12 durch den folgenden Text: " + js_data[12] +
                         " Ersetze bitte den Text bei case 13 durch den folgenden Text: " + js_data[13] + " Ersetze bitte den Text bei case 14 durch den folgenden Text: " + js_data[14] +  
                         " Ersetze bitte den Text bei case 15 durch den folgenden Text: " + js_data[15] + " Ersetze bitte den Text bei case 16 durch den folgenden Text: " + js_data[16] +
                         " Ersetze bitte den Text bei case 17 durch den folgenden Text: " + js_data[17] + " Ersetze bitte den Text bei case 18 durch den folgenden Text: " + js_data[18] +
                         " Gebe mir bitte ausschließlich den vollstaendigen neuen Code zurueck ohne irgendwelchen weiteren Text und schreibe den gesamten Code NICHT in einem Kommentar")

response_js_list = []
for i in list_of_questions:
    discussions.append({"role": "user", "content":i})
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=discussions
        )
    response = completion.choices[0].message.content
    response_js_list.append(response)
    discussions.append({"role": "assistant", "content": response})
    
response_js_list.pop(0)

def clean_string(element):
    if element.startswith("```javascript") and element.endswith("```"):
        return element[len("```javascript"):].rstrip("```")
    return element

clean_list = [clean_string(element) for element in response_js_list]

with open("App.txt", 'w') as file:
    for item in clean_list:
        file.write(item)


### PATH HAS TO BE EXCHANGED
destination_path = "/Users/citai-livinglab/Desktop/Convai/Convai-JS-SDK-Alpha-master/demo/talking-avatar/src"
def rename_and_move_file(src_path, dst_folder, new_filename):
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    
    dst_path = os.path.join(dst_folder, new_filename)
    
    shutil.move(src_path, dst_path)
    print(f"File moved to {dst_path}")


src_file = 'App.txt'
destination_folder = 'some/other/folder'  
new_name = 'App.js'



##LETZTER STEP
rename_and_move_file(src_file, destination_path, new_name)

def move_txt_files_to_new_folder(source_folder):
    current_datetime = datetime.now()
    
    folder_name = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    
    new_folder_path = os.path.join(source_folder, folder_name)
    os.makedirs(new_folder_path)
    
    for file in os.listdir(source_folder):
        if file.endswith(".txt"):
            file_path = os.path.join(source_folder, file)
            shutil.move(file_path, new_folder_path)
            print(f"Moved {file} to {new_folder_path}")

source_folder = "/Users/citai-livinglab/Desktop/QuestionPro Dateien für Auswertung/" 

move_txt_files_to_new_folder(source_folder)