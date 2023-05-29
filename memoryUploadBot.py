import asyncio
import os
import requests
from dotenv import load_dotenv
import extractMetadata
import datetime
import zipfile

load_dotenv()

# Define the function to upload a Document
def upload_document(bot_token, chat_id, folder_path,caption) :     
    print("Uploading "+caption)
    try:
        parent_dir = os.path.dirname(folder_path)
        os.makedirs(parent_dir+"/upload", exist_ok=True)          
        url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
        files = {'document': open(folder_path+"/"+caption, 'rb')}
        data = {'chat_id': chat_id, 'caption':caption}
        response = requests.post(url, files=files, data=data)
        uploadFile= open(f"{parent_dir}/upload/{caption}_uploadStatus.json", "w")
        uploadFile.write(f"{response.json()}")
        # print(response.json())    
        print("uploaded Successfully")
    except Exception as error:
        print("Uploading Error: ",error)

# def create_zip(folder_path):
#     # Get the path to the folder that you want to zip.
#     parent=os.path.dirname(folder_path)
#     print("parent: ",parent)
#     # Create a zip file object.
#     zip_file = zipfile.ZipFile(f"{parent}.zip", "w")
#     # Iterate over the files in the folder.
#     for file in os.listdir(folder_path):
#         # Get the full path to the file.
#         file_path = os.path.join(folder_path, file)
#         # Add the file to the zip file.
#         zip_file.write(file_path)
#     # Close the zip file object.
#     zip_file.close()


async def main(): 
    print("-----------------main called-----------------")
    bot_token=os.getenv('bot_token')
    chat_id=os.getenv('chat_id')
    folder_path = os.getenv('folder_path')
    files=[]
    for file in os.listdir(folder_path):
        filePath= os.path.join(folder_path,file)  
        extractMetadata.extractMetaData(folder_path,file)
        file_creation_date = datetime.datetime.fromtimestamp(os.path.getmtime(filePath))
        files.append((file,file_creation_date))
    # # Sort the list of tuples by the file creation date.
    # files.sort(key=lambda x: x[-1])
    files.sort()
    metadata_file = open(f"fileSort.txt", "w")
    for file, file_creation_date in files:
        metadata_file.write(f"{file}----{file_creation_date}\n")
        upload_document(bot_token= bot_token,chat_id= chat_id,folder_path= folder_path,caption= file)        
    metadata_file.close()


asyncio.run(main())
