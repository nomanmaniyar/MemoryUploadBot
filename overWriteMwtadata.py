import exiftool


def stringToJson(file_path):
    # Open the file in read mode
    file = open(file_path, "r")
    
    # Read all of the lines from the file into a list
    
    lines = file.readlines()
    # Close the file
    file.close()

    jsonData={}
    # Print the lines
    for line in lines:
        key= line.split(" ")[0]
        value= line.removeprefix(key).removesuffix('\n').strip()
        print(key+value)
        jsonData[key.removesuffix(":")]=value   
    return jsonData 

    

# Set the metadata to overwrite
metadata =stringToJson("C:/Users/Noman Maniyar/Downloads/Telegram Desktop/recorded-3641344878509.MP4_metadata.txt")
                        # E:Fatima/test/recorded-3641344878509.MP4_metadata.txt")
exiftool = exiftool.ExifTool()
exiftool.terminate()
exiftool.run()
print(metadata)
# Overwrite the metadata
exiftool.execute(str(metadata), "C:/Users/Noman Maniyar/Downloads/Telegram Desktop/recorded-3641344878509.MP4")

