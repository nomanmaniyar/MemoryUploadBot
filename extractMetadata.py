import exiftool
import os

def extractMetaData(folderPath,file):
  print("-----------------extractMetaData called-----------------")
  parent_dir = os.path.dirname(folderPath)
  os.makedirs(parent_dir+"/metadata", exist_ok=True) 
  
  with exiftool.ExifToolHelper() as et: 
    try:      
      metadata_file = open(f"{parent_dir}/metadata/{file}_metadata.txt", "w")
      metadata =  et.get_metadata(f"{folderPath}/{file}")
      for listItem in metadata:
        for key, value in  listItem.items():
          metadata_file.write(f"{key}: {value}\n")
      metadata_file.close()
    except Exception as error:
      print(f"Can't extract data fot fileError: {folderPath}/{file}\n Error: {error}")

