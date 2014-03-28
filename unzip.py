import zipfile
import glob


directory = glob.glob("C:\Users\ccantey\Desktop\DNR\*.zip")

for files in directory:
    print files
    zfile = zipfile.ZipFile(files)
    try:
        for zips in zfile.namelist():
          #print zips
          zfile.extract(zips)
    except:
        pass
