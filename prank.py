import os
fileList=os.listdir('/Users/viditgupta/Downloads/prank')
os.chdir('/Users/viditgupta/Downloads/prank')
for filename  in fileList:
    oldname=filename
    newname=filename.lstrip("0123456789")

    print("oldname - "+ oldname)
    print("newname - "+ newname)

    os.rename(oldname,newname)
