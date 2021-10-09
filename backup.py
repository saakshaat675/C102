import os
import shutil

source=input("pls put source folder name")

source=source+"\\"


destination=input("pls put destination place")

destination=destination+"\\"


listfile=os.listdir(source)


for file in listfile:
    shutil.copy((source+file),destination)



    