#################################################
#                                               #
#         Created by Cao Le Cong Minh           #
#                                               #
#################################################
#   Gmail:  caolecongminh1997@gmail.com         #
#	Github: https://github.com/Minh-CaoLeCong   #
#################################################


# USAGE:
# python RenameMultipleFile.py --path inpuFolderPath

# Import the necessary packages
import os
import argparse

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", type=str, required=True,
	help="input directory path of all files want to rename")
args = vars(ap.parse_args())

# grab all files name in input folder
List_File_Name = os.listdir(args["path"])

# loop over the image path
for (i, Str_FileName) in enumerate(List_File_Name):

    # Extract the file extension
    print("[INFO] processing image {}/{}".format(i + 1, len(List_File_Name)))
    Tuple_File_Extension = os.path.splitext(Str_FileName)

    Str_Current_File_Name = args["path"] + "\\" + Str_FileName
    Str_New_File_Name = args["path"] + "\\" + str(i).zfill(8) + Tuple_File_Extension[-1]

    # rename
    os.rename(Str_Current_File_Name, Str_New_File_Name)

print ('\n----------------------DONE---------------------------\n')

#################################################
#                                               #
#         Created by Cao Le Cong Minh           #
#                                               #
#################################################
#   Gmail:  caolecongminh1997@gmail.com         #
#	Github: https://github.com/Minh-CaoLeCong   #
#################################################