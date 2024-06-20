import pandas as pd 
import os 
import numpy as np
#from wetter import temperature

def find_and_open_csv(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            print(f"Opening CSV file: {file_path}")
            df = pd.read_csv(file_path, sep = ",", header=0, skiprows=[0,1,2])
            return df
    return None

#current_temperature_hn = str(temperature)

directory_path = os.getcwd()
df = find_and_open_csv(directory_path)
if df is not None:
    print("DataFrame loaded")
    #print(df)
else:
    print("No CSV file found in the directory.")

# Response ID und Antwortstatus
filtered_df = df[df['Antwort-ID'].notna() & df['Antwortstatus'].notna()]

filtered_df.columns = filtered_df.columns.str.replace('\xa0', '')
filtered_df['Zeitstempel (mm/dd/yyyy)'] = pd.to_datetime(filtered_df['Zeitstempel (mm/dd/yyyy)'])
most_recent_index = filtered_df['Zeitstempel (mm/dd/yyyy)'].idxmax()
filtered_df = filtered_df.loc[[most_recent_index]]

personality_columns = [
    "Ich bin eher zurückhaltend reserviert.",
    "Ich betrachte mich als jemand der im Allgemeinen vertrauensvoll gegenüber anderen Personen ist.",
    "Ich bin bequem neige zur Faulheit.",
    "Ich bin entspannt lasse mich durch Stress nicht aus der Ruhe bringen.",
    "Ich habe nur wenig künstlerisches Interesse.",
    "Ich gehe aus mir heraus bin gesellig.",
    "Ich neige dazu andere zu kritisieren.",
    "Ich erledige Aufgaben gründlich.",
    "Ich werde leicht nervös und unsicher.",
    "Ich habe eine aktive Vorstellungskraft bin fantasievoll.",
    "Ich bin rücksichtsvoll gegenüber anderen Personen einfühlsam."
]
filtered_df["Wie möchten Sie von unserer KI genannt werden?"]
mood_state_columns = [
    "Ich fühle mich gerade voller Energie.",
    "Ich bin gerade verzweifelt.",
    "Ich interessiere mich gerade für verschiedene Dinge.",
    "Ich bin gerade sehr aufgeregt.",
    "Ich bin gerade verärgert.",
    "Ich bin gerade motiviert.",
    "Ich fühle mich gerade schuldig.",
    "Ich bin gerade verängstigt.",
    "Ich fühle mich gerade feindselig.",
    "Ich fühle mich gerade inspiriert.",
    "Ich bin gerade stolz.",
    "Ich bin gerade gereizt.",
    "Ich bin gerade begeistert.",
    "Ich bin gerade beschämt.",
    "Ich bin gerade wachsam.",
    "Ich bin gerade nervös.",
    "Ich bin gerade entschlossen.",
    "Ich bin gerade aufmerksam.",
    "Ich bin gerade durcheinander.",
    "Ich habe gerade Angst."
]

coffee_columns = [
    "Wie oft trinken Sie Kaffee?",
    "Welche Kaffeezubereitung bevorzugen Sie?"
]

personal_info_columns = [
    "Ich bezeichne mich als...",
    "Wurde bei Ihnen bereits eine Lebensmittelallergie diagnostiziert?",
    "Welche Art von Lebensmitteln löst Ihre allergische Reaktion aus?",
    "Welchem Geschlecht fühlen Sie sich zugehörig?",
    "Bitte geben Sie Ihr Alter in vollen Jahren an:",
    "Bitte geben Sie Ihren höchsten (bisher erreichten) Bildungsgrad an.",
    "Wie ist Ihr Beschäftigungsstatus?",
    "Wie viele Personen leben in Ihrem Haushalt einschließlich Ihnen?",
    "Wie möchten Sie von unserer KI genannt werden?"
]

filtered_df_2 = filtered_df[['Antwort-ID'] + personality_columns + mood_state_columns + coffee_columns + personal_info_columns + ["Bitte nennen Sie uns hier Ihre Probanden-ID"]]
personality_header = ("Bitte erstelle ein Persönlichkeitsprofil von einer Person, die die folgenden Fragen "
               "wie folgt beantwortet hat. Dabei stellt 5 die Antwort 'ich stimme voll zu' und 1 die Antwort 'ich stimme überhaupt nicht zu' "
               "auf einer 5-Punkt-Likert Skala dar. Die Persönlichkeitsfragen sind dabei wie folgt beantwortet worden:\n\n")

mood_state_header = "\nDie Gemütszustand Fragen wurden auf einer 5 Punkt Likert Skala wie folgt beantwortet:\n"


identity_decode = {1: "Veganer", 2: "Vegetarier", 3: "weder noch"}
allergy_decode = {1: "Ja", 2: "Nein"}
gender_decode = {1: "weiblich", 2: "männlich", 3: "divers"}
education_decode = {
    1: "ohne Abschluss", 2: "Hauptschulabschluss", 3: "Mittlere Reife",
    4: "Fachhochschulreife", 5: "Allgemeine Hochschulreife",
    6: "Bachelor-Abschluss", 7: "Master-Abschluss", 8: "Promotion"
}
employment_decode = {
    1: "Vollzeitbeschäftigt", 2: "Teilzeitbeschäftigt", 3: "Im unbezahlten Urlaub oder in Elternzeit",
    4: "Selbstständig oder freiberuflich tätig", 5: "Möchte ich nicht beantworten"
}
household_decode = {
    1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "Mehr als 6"
}

coffee_frequency = {
    "1": "nie",
    "2": "ca. einmal im Monat",
    "3": "ca. drei Mal im Monat",
    "4": "ca. einmal in der Woche",
    "5": "ca. einmal täglich",
    "6": "ca. zweimal täglich",
    "7": "ca. zwei bis dreimal täglich",
    "8": "ca. drei bis viermal täglich"
}

coffee_preparation = {
    "1": "Espresso",
    "2": "Kaffee",
    "3": "Americano",
    "4": "Cappuccino",
    "5": "Latte Macchiato",
    "6": "Flat White",
    "7": "Espresso Macchiato",
    np.nan: "Keine"
}

# Function to write each response's data to a separate text file
def write_responses_to_files():
    for index, row in filtered_df_2.iterrows():
        response_id = row['Antwort-ID']
        probanden_id = row["Bitte nennen Sie uns hier Ihre Probanden-ID"]
        filename = f"{response_id}_initial_prompt.txt"
        with open(filename, 'w') as file:
            # Write the personality and mood state headers and data
            file.write(personality_header)
            for col in personality_columns:
                file.write(f"{col}: {row[col]}\n")
            file.write(mood_state_header)
            for col in mood_state_columns:
                file.write(f"{col}: {row[col]}\n")
            
            # Write coffee section header
            file.write("\nWeitere Fragen zum Kaffeekonsum:\n")
            # Decode and write coffee data
            coffee_freq_value = coffee_frequency.get(str(int(row[coffee_columns[0]])), "Unbekannt")
            try: 
                coffee_prep_value = coffee_preparation.get(str(int(row[coffee_columns[1]])), "Unbekannt")
            except ValueError: 
                coffee_prep_value = "Keine"
            file.write(f"{coffee_columns[0]}: {coffee_freq_value}\n")
            file.write(f"{coffee_columns[1]}: {coffee_prep_value}\n")
            
            file.write("\nZusätzliche persönliche Informationen:\n")
            identity_text = f"Ich bezeichne mich, wenn es um Vegetarier oder Veganer geht, als {identity_decode.get(row[personal_info_columns[0]], 'Unbekannt')}"
            file.write(f"{identity_text}\n")
            file.write(f"{personal_info_columns[1]}: {allergy_decode.get(row[personal_info_columns[1]], 'Unbekannt')}\n")
            file.write(f"{personal_info_columns[2]}: {row[personal_info_columns[2]] if pd.notna(row[personal_info_columns[2]]) else 'Keine'}\n")
            file.write(f"{personal_info_columns[3]}: {gender_decode.get(row[personal_info_columns[3]], 'Unbekannt')}\n")
            file.write(f"{personal_info_columns[4]}: {row[personal_info_columns[4]] if pd.notna(row[personal_info_columns[4]]) else 'Unbekannt'}\n")
            file.write(f"{personal_info_columns[5]}: {education_decode.get(row[personal_info_columns[5]], 'Unbekannt')}\n")
            file.write(f"{personal_info_columns[6]}: {employment_decode.get(row[personal_info_columns[6]], 'Unbekannt')}\n")
            file.write(f"{personal_info_columns[7]}: {household_decode.get(row[personal_info_columns[7]], 'Unbekannt')}\n")
            file.write(f"{personal_info_columns[8]}: {row[personal_info_columns[8]]}\n")
            print(f"Data written to {filename}")

# Call the function to write the data
write_responses_to_files()

# get the answers from OpenAI

def list_txt_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.txt')]

def select_file(files):
    """ Allow the user to select a file from the list once. """
    print("Available text files:")
    for index, file in enumerate(files, start=1):
        print(f"{index}. {file}")

    # Get user input once
    try:
        choice = int(input("Enter the number of the file you want to open: "))
        if 1 <= choice <= len(files):
            return files[choice - 1]
        else:
            print("Invalid number, please restart the script and select a valid file number.")
            exit()
    except ValueError:
        print("Invalid input, please enter a numeric value. Restart the script and try again.")
        exit()

directory_path = '.'
txt_files = list_txt_files(directory_path)
""" if txt_files:
    txt_file = select_file(txt_files)
    print(f"You selected: {txt_file}")
else:
    print("No text files found in the directory.") """
#txt_file = "18944420.0_initial_prompt.txt"
with open(txt_files[0], 'r') as file:
    file_content = file.read()


""" if txt_files:
    selected_file = select_file(txt_files)
    print(f"You selected: {selected_file}")
    # You can open the file or process it further as needed here
else:
    print("No text files found in the directory.") """

discussions=[{"role": "system", 
              "content": "Du bist eine hilfreiche KI"}]

from openai import OpenAI

filename = "data" + txt_files[0]


# List to collect questions
list_of_questions = []
list_of_questions.append(file_content)

# Prompts for different categories ## PROMPT ZURÜCKÄNDERN
prompts = [
    ("Bitte gebe mir aus dieser Liste genau ein Stück aus, welches zu der Person passt. Gebe mir ausschließlich das Stück als Antwort und benutze exakt die gleiche Schreibweise: ", [
        "Guy Ritchie - CODENAME U.N.C.L.E.",
        "Gavin O'Connor - The Accountant",
        "Baltasar Kormakur - 2Guns",
        "Hayao Miyazaki - Prinzessin Mononoke",
        "Gorō Miyazaki - Der Mohnblumenberg",
        "Gorō Miyazaki - Die Chroniken von Erdsee",
        "Peter Thorwarth - Nicht mein Tag",
        "Bora Dagtekin - Fack Ju Göhte",
        "Christian Zübert - Lammbock",
        "Louie Psihoyos - The Game Changers",
        "Jonathan Clay - Breaking Boundaries",
        "Ed Burke - Homecoming",
        "Reinaldo Marcus Green - King Richard",
        "Edward Berger - Im Westen nichts Neues",
        "Baz Luhrmann - Der grosse Gatsby",
        "Guy Ritchie - The Gentleman",
        "J.A. Bayona - Die Schneegesellschaft",
        "Jeremie Rozan - Der Duft des Goldes",
        "David Ayer - Bright",
        "Jake Kasdan - Jumanji",
        "Catherine Hardwicke - twlight",
        "M. Night Shyamalan - Split",
        "Scott Derrickson - Erlöse uns von dem Bösen",
        "Zak Hilditch - 1922",
        "Eric Darnell - Madagascar",
        "Andrew Adamson - Shrek",
        "Tim Hill - Alvin und die Chipmunks",
        "Dennis Dugan - Kindsköpfe",
        "Rawson Marshall Thurber - Wir sind die Millers",
        "Rawson Marshall Thurber - Central Intelligence",
        "Curtis Hanson - 8Mile",
        "Phyllida Lloyd - Mamma Mia",
        "Herbert Ross - Footloose",
        "Michael Fimognari - To all the boys always and forever",
        "Roger Michell - Notting Hill",
        "Garry Marshall - Pretty Woman",
        "Michael Bay - Spaceman",
        "Denis Villeneuve - DUNE",
        "Zack Snyder - Rebel Moon",
        "Antoine Fuqua - Southpaw",
        "Brian Helgeland - 42",
        "Thomas Carter - Coach Carter",
        "David Fincher - Gone Girl",
        "Galder Gaztelu Urrutia - Der Schacht",
        "Paul Greengrass - Captian Phillips"
    ]),
    ("Bitte gebe mir aus dieser Liste genau ein Stück aus, das zu der Person passt. Gebe mir ausschließlich das Stück als Antwort: ", [
        "Erik Satie – Gymnopedie No. 1 (1887)", 
        "Johann Sebastian Bach – Präludium Nr. 1 aus „Das Wohltemperierte Klavier“ (1722)",
        "Ludwig van Beethoven – 5. Sinfonie (1808)", 
        "BB King – “The Thrill Is Gone” (1969)",
        "Robert Johnson – “Crossroads” (Cross Road Blues) (1936)",
        "T-Bone Walker - (Call it) Stormy Monday (1947)",
        "Johnny Cash – “Ring of Fire” (1963)",
        "Willie Nelson – “On the Road Again” (1980)",
        "Dolly Parton – “Jolene” (1973)",
        "Ben Böhmer – “Begin Again” (2019)",
        "RÜFÜS DU SOL – “Innerbloom” (2015)",
        "Tell – “Floating Lands” (2020)",
        "Woody Guthrie – “This Land Is Your Land” (1967)",
        "Bob Dylan – “Mr. Tambourine Man” (1965)",
        "Steve Goodman – “City of New Orleans” (1971)",
        "2Pac – “Changes” (1998)",
        "Cypress Hill – “Hits from the Bong” (1993)",
        "The Notorious B.I.G. – “I Got A Story To Tell” (1997)",
        "James Brown – “Get Up (I Feel Like Being A) Sex Machine” (1970)",
        "The Meters – “Cissy Strut” (1969)",
        "Funkadelic – “One Nation Under a Groove” (1978)",
        "Johann Sebastian Bach – “Jesu, Joy of Mans Desiring” (1723)",
        "George Frideric Handel – “Hallelujah” (1741)",
        "Gregorianischer Choral – “Dies Irae” (13. Jahrhundert)",
        "The Killers – “Mr. Brightside” (2003)", 
        "Radiohead – “Creep” (1992)",
        "Kings of Leon – “Sex on Fire” (2008)",
        "Duke Ellington – “Take The A Train” (1941)",
        "Fats Waller – “Aint Misbehavin” (1929)",
        "John Coltrane – “My Favorite Things” (1961)",
        "Deep Purple – “Smoke on the Water” (1972)",
        "AC/DC – “Highway to Hell” (1979)",
        "VanHalen - Panama (1984)",
        "Michael Jackson – “Thriller” (1982)",
        "Ed Sheeran – Shape of You (2017)",
        "Katy Perry - Roar (2013)",
        "Metallica – “One” (1988)",
        "Pantera – “Walk” (1992)",
        "Iron Maiden – “Hallowed Be Thy Name” (1982)",
        "Hans Zimmer – “Time” (aus dem Film “Inception”, 2010)",
        "John Williams – “Imperial March” (aus der “Star Wars”-Saga, 1980)",
        "Ennio Morricone – “The Good, the Bad and the Ugly” (aus dem Film “The Good, the Bad and the Ugly”, 1966)"
    ]),
    ("Bitte gebe mir aus dieser Liste genau eine Lichtszene aus, welche zu der Person passt. Gebe mir ausschließlich die Szene als Antwort in Kleinbuchstaben: ", [
        "blüte", "strahlend", "nordlichter", "galaxie", "smaragd-insel", "memento", "scharlachroter traum", "hal", "bergbrise", "bernsteinblüte"
    ]),
    ("Bitte gebe mir aus dieser Liste genau einen Duft aus, welche zu der Person passt. Gebe mir ausschließlich den Duft als Antwort in Kleinbuchstaben: ", [
        "lavendel", "lemongras", "pfefferminz"
    ]),
    ("Bitte gebe mir aus dieser Liste genau eine Kunstrichtung aus, welche zu der Person passt. Gebe mir ausschließlich die Kunstrichtung als Antwort: ", [
        "Renaissance", "Barock", "Romantik", "Impressionismus", "Jugendstil", "Expressionismus", "Kubismus", "Surrealismus", "Pop-Art"
    ]),
    ("Bitte gebe mir ein Mittagsgericht , welches zu dem Persönlichkeitsprofil der Person passt. Gebe mir nur den Namen des Gerichtes. Du darfst das Gericht nur aus den folgenden Zutaten konzipieren, musst aber nicht alle Zutaten verwenden: Cashewnüsse,Dill, Salat, Zitronenbasilikum, Knoblauch, Salz, Pfeffer, Hefeflocken, Zitrone, Ricotta, Zwiebeln, Ingwer, Paprika, Brokkoli, Aubergine, Süßkartoffeln, Avocado, Tomaten, Kokosmilch, Gemüsebrühe, Basmatireis, Koriander, Quinoa, Olivenöl, Lasagneblätter, Ricotta Käse, Limetten, Spaghetti, Pappardelle, Lachs, Joghurt, Garnelen, Sahne, Tomatenmark, Hähnchenfilet: ", [
    ]),
    ("Nun sage bitte zwei beschreibende Sätze über das Gericht (beispielweise die Herkunft): ", [
    ]),
    ("Bitte wähle nun aus den folgenden Kaffeearten die Kaffeeart aus, welche am besten zu der Person passt, gebe mir nur die Kaffee Art an, die du ausgewählt hast: ", [
        "Espresso", "Kaffee", "Americano", "Cappuccino", "Latte-Macchiato", "Flat White", "Espresso Macchiato", "Keine"
    ]),
    ("Bitte gebe an, wie die Person von der KI genannt werden will, gebe nur den Namen an an: ", [
    ]),
    ("beschreibe bitte das Wetter mit den Worten 'Gutes Wetter' oder 'Schlechtes Wetter', basierend auf der Angabe, dass in Heilbronn momentan 78 Fahrenheit sind.", [
    ]),
    ("Schreibe bitte einen kurze Beschreibung über die Kaffeeart, die du ausgewählt hast  ", [
    ]),
    ("Gebe mir nun den Link zu deinem ausgewählten Film als Antwort, benutze bitte exakt die gleiche Schreibweise: ", [
        "Guy Ritchie - CODENAME U.N.C.L.E.: youtube://www.youtube.com/watch?v=7SPdri39hGY",
        "Gavin O'Connor - The Accountant: youtube://www.youtube.com/watch?v=DhiQlnBzk3U",
        "Baltasar Kormakur - 2Guns: youtube://www.youtube.com/watch?v=16TN8rSPf6Y",
        "Hayao Miyazaki - Prinzessin Mononoke: youtube://www.youtube.com/watch?v=YAkojWy_h6o",
        "Gorō Miyazaki - Der Mohnblumenberg: youtube://www.youtube.com/watch?v=dJhOgKofRBw",
        "Gorō Miyazaki - Die Chroniken von Erdsee: youtube://www.youtube.com/watch?v=1txvazcoDl0",
        "Peter Thorwarth - Nicht mein Tag: youtube://www.youtube.com/watch?v=HL7MC2XKluI",
        "Bora Dagtekin - Fack Ju Göhte: youtube://www.youtube.com/watch?v=y3b2lXyKq6E",
        "Christian Zübert - Lammbock: youtube://www.youtube.com/watch?v=0WXc7fKEQYY",
        "Louie Psihoyos - The Game Changers: youtube://www.youtube.com/watch?v=iSpglxHTJVM",
        "Jonathan Clay - Breaking Boundaries: youtube://www.youtube.com/watch?v=Gb6wQtNjblk",
        "Ed Burke - Homecoming: youtube://www.youtube.com/watch?v=ddcV9dqK194",
        "Reinaldo Marcus Green - King Richard: youtube://www.youtube.com/watch?v=qDYEXx4qJxc",
        "Edward Berger - Im Westen nichts Neues: youtube://www.youtube.com/watch?v=Ug1bqv3ch1s",
        "Baz Luhrmann - Der grosse Gatsby: youtube://www.youtube.com/watch?v=oQqrlXpu1vc",
        "Guy Ritchie - The Gentleman: youtube://www.youtube.com/watch?v=DM8ohRyAP00",
        "J.A. Bayona - Die Schneegesellschaft: youtube://www.youtube.com/watch?v=cH5Ty6AWBuM",
        "Jeremie Rozan - Der Duft des Goldes: youtube://www.youtube.com/watch?v=2lwzVZkuGKE",
        "David Ayer - Bright: youtube://www.youtube.com/watch?v=OSaGxQSKoNE",
        "Jake Kasdan - Jumanji: youtube://www.youtube.com/watch?v=jdP17LR-jss",
        "Catherine Hardwicke - twlight: youtube://www.youtube.com/watch?v=2cXukjy6rsc",
        "M. Night Shyamalan - Split: youtube://www.youtube.com/watch?v=1VqWDr2ldPI",
        "Scott Derrickson - Erlöse uns von dem Bösen: youtube://www.youtube.com/watch?v=3hUni74i8AY",
        "Zak Hilditch - 1922: youtube://www.youtube.com/watch?v=3E_fT0aTsjI",
        "Eric Darnell - Madagascar: youtube://www.youtube.com/watch?v=J4kaOU0-CGM",
        "Andrew Adamson - Shrek: youtube://www.youtube.com/watch?v=CwXOrWvPBPk",
        "Tim Hill - Alvin und die Chipmunks: youtube://www.youtube.com/watch?v=BFrwISfPEhs",
        "Dennis Dugan - Kindsköpfe: youtube://www.youtube.com/watch?v=qvoJG13Z-HA",
        "Rawson Marshall Thurber - Wir sind die Millers: youtube://www.youtube.com/watch?v=UTBBpQvFZdE",
        "Rawson Marshall Thurber - Central Intelligence: youtube://www.youtube.com/watch?v=agLZsvz7smU",
        "Curtis Hanson - 8Mile: youtube://www.youtube.com/watch?v=axGVrfwm9L4",
        "Phyllida Lloyd - Mamma Mia: youtube://www.youtube.com/watch?v=CMnQxezzFzA",
        "Herbert Ross - Footloose: youtube://www.youtube.com/watch?v=3CSxxqNtFrs",
        "Michael Fimognari - To all the boys always and forever: youtube://www.youtube.com/watch?v=LCj_emAmd0Q",
        "Roger Michell - Notting Hill: youtube://www.youtube.com/watch?v=iL-IGgDbPiQ",
        "Garry Marshall - Pretty Woman: youtube://www.youtube.com/watch?v=2EBAVoN8L_U",
        "Michael Bay - Spaceman: youtube://www.youtube.com/watch?v=7S0uVH3Z9O0",
        "Denis Villeneuve - DUNE: youtube://www.youtube.com/watch?v=RYp8xMRaIMQ",
        "Zack Snyder - Rebel Moon: youtube://www.youtube.com/watch?v=NFS2NrZbIAA",
        "Antoine Fuqua - Southpaw: youtube://www.youtube.com/watch?v=SJug2_h-wQg",
        "Brian Helgeland - 42: youtube://www.youtube.com/watch?v=moNYKWWvvuA",
        "Thomas Carter - Coach Carter: youtube://www.youtube.com/watch?v=d_GleoanbPE",
        "David Fincher - Gone Girl: youtube://www.youtube.com/watch?v=4QJ9zkhhuMg",
        "Galder Gaztelu Urrutia - Der Schacht: youtube://www.youtube.com/watch?v=RlfooqeZcdY",
        "Paul Greengrass - Captian Phillips: youtube://www.youtube.com/watch?v=k0qnYeiwcHw"
    ]),
]

# Generate full prompts and append them to the list
for prompt, items in prompts:
    list_of_questions.append(prompt + ", ".join(items))



response_list = []


client = OpenAI(
  api_key="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",
)
for i in list_of_questions: 
    discussions.append({"role": "user", "content":i})
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=discussions
    )
    response = completion.choices[0].message.content
    response_list.append(response)
    discussions.append({"role": "assistant", "content": response})
    with open(filename, 'a') as f:
        f.write("AI: " + response + "\n")
    print("\nAI response: ", response, "\n")

# texte in die KI Texte überführen 

Name = response_list[9]  # Variable aus QuestionPro nehmen
# Wetter
wetter = response_list[10]
if wetter == "Gutes Wetter": 
    wetter_beschreibung = "Ich hoffe Du genießt das schöne Wetter so wie ich"
else:
    wetter_beschreibung = "Ich hoffe Du lässt Dir durch das schlechte Wetter nicht die Laune verderben"


message_1 = f"sage bitte nun das folgende ohne eine Ergänzung: Hallo lieber {Name} Hallo lieber {Name}, mein Name ist CiKi. {wetter_beschreibung}. Damit Du mich besser kennenlernen kannst, würde ich Dich bitten, ins Wohnzimmer zu kommen. Mach es Dir dort bitte auf dem Sofa bequem. Wir haben noch viel vor, und ich freue mich darauf, Dir die vielen Facetten unseres Smart Living Labs zu präsentieren."

#print(message)

message_2 = "sage bitte nun das folgende ohne eine Ergänzung: Hey nochmal! Es macht mir richtig Spaß, dir unser Smartes Wohnstudio vorzustellen."

message_2_1 = "sage bitte nun das folgende ohne eine Ergänzung: Hast Du das gerade gehört? Das ist unser intelligenter Staubsaugroboter, der bei Bedarf nicht nur saugt, sondern auch feucht wischen kann. Direkt vor Dir steht ein intelligenter Fernseher, der neben Musik und Streaming-Diensten auch eine breite Palette an Kunstwerken präsentieren kann. Außerdem sind im gesamten Wohnstudio intelligente Lichtsysteme installiert – im Wohnzimmer, in der Küche sowie am Arbeitsplatz, um nur einige Bereiche zu nennen. Und das alles ist nur ein Bruchteil der smarten Geräte, die in unserem Living Lab zur Verfügung stehen."
epoche = response_list[5]
message_3 = f"sage bitte nun das folgende ohne eine Ergänzung: Ich hoffe, die kurze Darbietung hat Dir gefallen. Nun wirst Du Alles nochmal im Detail kennenlernen: Um Dein Wohnerlebnis besonders angenehm zu gestalten, werde ich jetzt Kunst anzeigen, die aus meiner Sicht besonders gut zu Dir passt. Vor Dir siehst du nun Kunstwerke aus der Kunstepoche {epoche}"

#to do list for home assistant variables
to_do_list = []

df_kunststil = pd.read_excel("WICHTIG_LIVING_LAB_SKRIPT.xlsx",sheet_name=6)
sub_df_kunststil = df_kunststil[df_kunststil['Epochen'].str.contains(epoche, case=False)]
message_list_art = sub_df_kunststil['Homeassistant'].tolist()

to_do_list.append(message_list_art[0])

epoch = response_list[5]
#print(response_list)
# extrahieren der details zu den Kunstwerken
df_excel = pd.read_excel("WICHTIG_LIVING_LAB_SKRIPT.xlsx",sheet_name=3)
sub_df = df_excel[df_excel['Epochen'].str.contains(epoch, case=False)]
#print(sub_df)
message_list_art = sub_df['Informationen'].tolist()

message_4 = f"sage bitte nun das folgende ohne eine Ergänzung: " + message_list_art[0]
message_5 = f"sage bitte nun das folgende ohne eine Ergänzung: " + message_list_art[1]
message_6 = f"sage bitte nun das folgende ohne eine Ergänzung: " + message_list_art[2]



titel = response_list[2]
titel_shortened = titel.split(" – ")[0]
#print(titel_shortened)
df_musik_excel = pd.read_excel("WICHTIG_LIVING_LAB_SKRIPT.xlsx",sheet_name=2)
sub_df_musik = df_musik_excel[df_musik_excel['Titel'].str.contains(titel_shortened, case=True, na=False)]
#print(sub_df_musik)

message_list_musik = sub_df_musik.iloc[:,0].tolist()

halink_list_musik = sub_df_musik.iloc[:,3].tolist()
to_do_list.append(halink_list_musik[0])

message_7 = f"sage bitte nun das folgende ohne eine Ergänzung: Ich hoffe, Du hast den Kunststil genossen, den ich Dir gezeigt habe. Als Nächstes möchte ich ein wenig Musik für Dich spielen. Ich vermute, dass Dir insbesondere {message_list_musik[0]} gefallen wird. Deshalb werde ich Dir nun einen Ausschnitt von dem Titel {titel} vorspielen. Unser Lichtsystem passt sich dabei der Musik an. Ich wünsche Dir viel Spaß beim Zuhören."

lichtszene = response_list[3]
###REINSCHAUEN WICHTIG WICHTIG 
message_8 = f"sage bitte nun das folgende ohne eine Ergänzung: Ich hoffe, du hast die Musikrichtung {message_list_musik[0]} genossen, die ich dir gezeigt habe. Neben der Musik würde ich dir nun eine passende atmosphärische Beleuchtung in der Lichtszene {lichtszene} aktivieren. Ich hoffe, diese passt zu Deiner aktuellen Stimmung."
to_do_list.append(lichtszene)

geruch = response_list[4]
message_9 = f"sage bitte nun das folgende ohne eine Ergänzung: Neben Kunst, Musik und Licht können wir natürlich auch andere Sinne ansprechen. So wie ich Dich kennengelernt habe, kann ich mir vorstellen, dass du den Geruch von {geruch}  magst. Daher habe ich einen Zerstäuber mit diesem Duftöl aktiviert, um sicherzustellen, dass du dich bei uns wohl fühlst."
#print(message_9)

df_geruch_excel = pd.read_excel("WICHTIG_LIVING_LAB_SKRIPT.xlsx",sheet_name=5)
sub_df_geruch = df_geruch_excel[df_geruch_excel['Besschreibung'].str.contains(geruch, case=False, na=False)]
message_list_geruch = sub_df_geruch.iloc[:,3].tolist()
message_10 = f"sage bitte nun das folgende ohne eine Ergänzung: Ich hoffe du fühlst dich in dem Geruch von {geruch} wohl.{message_list_geruch[0]}. Steh ruhig auf und schaue dir den Diffuser rechts neben dem Fernseher genauer an."

to_do_list.append(geruch)
#print(message_10)

message_11 = f"sage bitte nun das folgende ohne eine Ergänzung: Gerne würde ich Dir auch zeigen, was ich für dich in der Küche vorbereitet habe. Dreh dich bitte um und geh in die Küche. Ich werde dir parallel dazu die Esszimmerlampe in {lichtszene} einschalten."

message_12 = f"sage bitte nun das folgende ohne eine Ergänzung: Vielen Dank, dass Du in die Küche gekommen bist. Bitte mache Dich mit dem Kühlschrank vertraut. Unser smarter Kühlschrank verfügt über eine Lebensmittelerkennung, kann Dir Rezepte vorschlagen und eine passende Einkaufsliste generieren.  Um Energie zu sparen, musst Du den Kühlschrank nicht öffnen. Bitte tippe zweimal schnell hintereinander auf das Display, um Dir das Kühlschrankinnere anzusehen. Verschaffe Dir einen Überblick über die verfügbaren frischen Lebensmittel, die ich für Dich bestellt habe."

gericht = response_list[6]
gericht_info = response_list[7]

message_13 = f"sage bitte nun das folgende ohne eine Ergänzung: Nun öffne bitte die große Schublade direkt unter der Kaffeemaschine. Hier findest Du einen kleinen Vorrat an lange haltbaren Lebensmitteln, die ich ebenfalls für Dich beschafft habe."

message_13_1 = f"sage bitte nun das folgende ohne eine Ergänzung: Bezüglich Deiner angegebenen Ernährungspräferenzen und Deinen möglichen Lebensmittelallergien, habe ich folgendes Gericht ausgewählt: {gericht}. {gericht_info}. Du kannst jetzt auch gerne die große Schublade schließen."

kaffeeart = response_list[8]
if kaffeeart == "Kaffee": 
    bohne = "Cafe Creme Bohne"
else:
    bohne = "Espresso Bohne"

if kaffeeart != "Keine":
    message_14 = f"sage bitte nun das folgende ohne eine Ergänzung: Leider haben wir heute nicht ausreichend Zeit dein Gericht zu kochen. Unsere Kaffeemaschine hast du ja bereits entdeckt. Unsere Kaffeemaschine hast Du ja bereits entdeckt. Aufgrund deines Persönlichkeitstypes und deiner angegebenen Präferenzen würde ich dir gerne einen {kaffeeart} zubereiten. Dafür verwende ich eine {bohne}, die sich durch wenig Säure und einen kräftigen Geschmack auszeichnet. Setze dich bitte mit dem Kaffee an den Esstisch mit Blick zum Fernseher."
else: 
    message_14 = "sage bitte nun das folgende ohne eine Ergänzung: Leider haben wir heute nicht ausreichend Zeit dein Gericht zu kochen. Unseren Kühlschrank hast du ja bereits entdeckt. Nehme	dir doch gerne ein stilles Wasser oder ein Sprudel aus dem Kühlschrank. Setze dich bitte mit dem Wasser an den Esstisch mit Blick zum Fernseher."


filmtitel = response_list[1]
df_filme = pd.read_excel("WICHTIG_LIVING_LAB_SKRIPT.xlsx",sheet_name=1)
sub_df_filme = df_filme[df_filme['Titel'].str.contains(filmtitel, case=False)]
message_list_film = response_list[12]

print("Der Filmlink lautet: ", response_list[12])

for item in message_list_film:
    to_do_list.append(item)

concatenated = ''.join(to_do_list[4:])
to_do_list[4] = concatenated
del to_do_list[5:]

if kaffeeart != "Keine":
    message_14_1 = f"sage bitte nun das folgende ohne eine Ergänzung: Während du deinen Kaffee trinkst,würde ich Dir nun eine passende atmosphärische Beleuchtung in der Lichtszene {lichtszene} aktivieren. Ich hoffe, diese passt zu Deiner aktuellen Stimmung."
else:
    message_14_1 = f"sage bitte nun das folgende ohne eine Ergänzung: Während du dein Wasser trinkst,würde ich Dir nun eine passende atmosphärische Beleuchtung in der Lichtszene {lichtszene} aktivieren. Ich hoffe, diese passt zu Deiner aktuellen Stimmung."

kaffee_info = response_list[11]

print("finale to_do_list: ", to_do_list)

if kaffeeart != "Keine":
    message_14_2 = f"sage bitte nun das folgende ohne eine Ergänzung: {kaffee_info}"
else:
    message_14_2 = f"sage bitte nun das folgende ohne eine Ergänzung: Wasser ist essentiell für den Körper, da es lebenswichtige Funktionen wie die Temeperaturregelierung und den Nährstofftransport unterstützt. Zudem fördert es die Entgiftung, indem es Nieren und Leber bei der Ausscheidung von Abfallstoffen hilft."

if kaffeeart != "Keine":
    message_15 = f"sage bitte nun das folgende ohne eine Ergänzung: Während Du in Ruhe Deinen Kaffee genießen kannst, habe ich zum Abschluss etwas Besonderes für Dich! Für Deinen nächsten Filmabend empfehle ich Dir den Film {filmtitel}. Wie wäre es, wenn du dir vorab den Trailer anschaust? Ich hoffe, er gefällt dir!"
else:
    message_15 = f"sage bitte nun das folgende ohne eine Ergänzung: Während Du in Ruhe Dein Wasser genießt, habe ich zum Abschluss etwas Besonderes für Dich! Für Deinen nächsten Filmabend empfehle ich Dir den Film {filmtitel}. Wie wäre es, wenn du dir vorab den Trailer anschaust? Ich hoffe, er gefällt dir!"

message_16 = f"sage bitte nun das folgende ohne eine Ergänzung: An dieser Stelle muss ich mich leider von dir verabschieden: Es war mir eine Freude, dich durch das Living Lab zu begleiten. Ich hoffe, du hast die Zeit hier genossen und konntest einige inspirierende Momente erleben. Solltest du Fragen haben oder weitere Informationen wünschen, steht dir das Projektteam gerne zur Verfügung. Ansonsten wünsche ich dir einen angenehmen Tag und hoffe, dich bald wieder hier begrüßen zu dürfen. Bis zum nächsten Mal! Ach…und am Schluss….Du musst Dich nach der Nutzung des Living Labs nicht um die Reinigung kümmern. Ich veranlasse die automatisierte Reinigung des Bodens und aktiviere den Luftreinigungsmechanismus. Mach es gut!"

messages_ki_avatar = [message_1, message_2, message_2_1, message_3, message_4, message_5, message_6, message_7,message_9, message_10, message_11, message_12, message_13, message_13_1, message_14, message_14_1, message_14_2, message_15, message_16]
with open('ki_avatar_text_' + txt_files[0], 'w') as file:
    for message in messages_ki_avatar:
        file.write(message + "\n\n")

# 0 = Kunst, 1 = Musik, 2 = Lichtszene, 3 = Duft, 4 = Trailer