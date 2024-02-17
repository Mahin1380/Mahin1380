import os
import shutil
# source = r"C\Users\Username\folder" + "\\"
# target = r"the\path\to\your\destination" + "\\" 
source = r"" +"\\"
target_1 = r"" +"\\"
target_2 = r"" + "\\"
target_3 = r"" + "\\"
for folder , subfolder , filenames in os.walk(source):
    for filename in filenames:
        if filename.endswith(".mp3"): 
            source_file = os.path.join(folder,filename)
            target_file = os.path.join(target_2,filename)
        elif filename.endswith(".py"):
            source_file = os.path.join(folder,filename)
            target_file = os.path.join(target_1,filename)
        elif filename.endswith("."):
            source_file = os.path.join(folder,filename)
            target_file = os.path.join(target_3,filename)
        
        try:
            print(f"Moving {filename} files to target folder")
            shutil.move(source_file,target_file)
        except Exception as e:
                print ("Error occured while moving the files ",e)


