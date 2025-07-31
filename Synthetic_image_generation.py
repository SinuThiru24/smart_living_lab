from openai import OpenAI
import base64
import pandas as pd

client = OpenAI(api_key="")


df = pd.read_excel("prompts_per_product_black_countertop.xlsx", sheet_name="Sheet1")

def search_product(product_name):
    return df[df["Product"] == product_name]

 # Function to create a file with the Files API
def create_file(file_path):
  with open(file_path, "rb") as file_content:
    result = client.files.create(
        file=file_content,
        purpose="vision",
    )
    return result.id

list_of_items = ["Hähnchenfilet"]

for i in list_of_items: 

    df_cashew = search_product(i)

    prompt_list = df_cashew["Prompt"].to_list()
    print(prompt_list)


    # Getting the file ID
    file_id = create_file(i + ".jpg")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text", "text": "please load the attached image into your knowledge base"},
                {
                    "type": "input_image",
                    "file_id": file_id,
                },
            ],
        }],
    )

    counter = 0
    for i in prompt_list:
        response_2 = client.responses.create(
            model="gpt-4.1-mini",
            previous_response_id=response.id,
            input=i,
            tools=[{"type": "image_generation"}],
        )

        image_data_fwup = [
            output.result
            for output in response_2.output
            if output.type == "image_generation_call"
        ]

        if image_data_fwup:
            image_base64 = image_data_fwup[0]
            with open(i + f"{counter}.png", "wb") as f:
                f.write(base64.b64decode(image_base64)) 
        counter += 1
        print(f"Image {counter} created and image saved")