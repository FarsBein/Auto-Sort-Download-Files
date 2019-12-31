import os 
import shutil
# Images , Document, video, Zip, Audio,

# Images = '/Users/User/Downloads/Images' 
# Documents = '/Users/User/Downloads/Documents' 
# videos = '/Users/User/Downloads/videos' 
# Zip = '/Users/User/Downloads/Zip' 
# Audio = '/Users/User/Downloads/Audio' 
# Executable = '/Users/User/Downloads/Executable'
# programming = '/Users/User/Downloads/programming'
# Other = '/Users/User/Downloads/Other'

folderNames=[
            '/Users/User/Downloads/Images',
            '/Users/User/Downloads/Documents',
            '/Users/User/Downloads/videos',
            '/Users/User/Downloads/Zip',
            '/Users/User/Downloads/Audio',
            '/Users/User/Downloads/Executable',
            '/Users/User/Downloads/programming',
            '/Users/User/Downloads/Other'
             ]

for folderName in folderNames:
    if not os.path.exists(folderName):
        os.makedirs(folderName)



os.chdir('/Users/User/Downloads')
 
for i in os.listdir():
    try:
        fileExt = os.path.splitext(i)[1].strip()
        if fileExt in [".aif",".cda",".mid",".mp3",".mpa"]:
            shutil.move(f"/Users/User/Downloads/{i}",f"/Users/User/Downloads/Audio/{i}")
        if fileExt in [".7z",".arj",".zip",".z",".rpm",".pkg",".rar",".tar.gz"]:
            shutil.move(f"/Users/User/Downloads/{i}",f"/Users/User/Downloads/Zip/{i}")
        if fileExt in [".ai",".bmp",".gif",".ico",".jpeg",".jpg",".png",".ps",".psd",".tif",".svg",".tiff",".ico"]:
            shutil.move(f"/Users/User/Downloads/{i}",f"/Users/User/Downloads/Images/{i}")
        if fileExt in [".csv",".dat",".db",".log",".mdb",".sav",".sql",".tar",".xml",".pptx",".ppt",".pps",".odp",".key",".doc",".docx",".odt",".pdf",".rtf",".txt"]:
            shutil.move(f"/Users/User/Downloads/{i}",f"/Users/User/Downloads/Documents/{i}")
        if fileExt in [".mp4",".mov",".mpeg",".swf",".vob",".mkv",".m4v",".h264",".flv",".avi",".3gp",".iso"]:
            shutil.move(f"/Users/User/Downloads/{i}",f"/Users/User/Downloads/videos/{i}")
        if fileExt in [".vb",".swift",".sh",".java",".h",".cs",".cpp",".class",".c",".html"]:
            shutil.move(f"/Users/User/Downloads/{i}",f"/Users/User/Downloads/programming/{i}")
        if fileExt in [".jar",".wsf",".gadget",".exe",".com",".cgi",".bin",".bat",".pl",".msi",".sys"]:
            shutil.move(f"/Users/User/Downloads/{i}",f"/Users/User/Downloads/Executable/{i}")
    except:
        print("Error: ",i,"----",os.path.splitext(i)[1].strip())
for i in os.listdir():
    fileExt = os.path.splitext(i)[1].strip()
    try:
        if fileExt not in ["", " "]:
            shutil.move(f"/Users/User/Downloads/{i}",f"/Users/User/Downloads/other/{i}")
    except:
        print("Error: ",i,"----",os.path.splitext(i)[1].strip())

        
print('DONE!!')