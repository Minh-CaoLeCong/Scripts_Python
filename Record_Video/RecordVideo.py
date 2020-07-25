#################################################
#                                               #
#         Created by Cao Le Cong Minh           #
#                                               #
#################################################
#   Gmail:  caolecongminh1997@gmail.com         #
#	Github: https://github.com/Minh-CaoLeCong   #
#################################################

# USAGE
# python RecordVideo.py

# import the necessary packages
from imutils.video import VideoStream
import argparse
import cv2
import time
from datetime import datetime

def RecordVideo():
    print("----------------------------------------------")
    # init configuration
    writer = None                   # check to save video.
    record = 0                      # record video or not. 0 is no record and 1 is recording video.
    videoPath = "./output/video/"   # output video directory 
    imagePath = "./output/image/"   # output image directory
    videoNameExtension = ".avi"
    imageNameExtension = ".jpg"
    displayTime = 1                 # display current time onto the frame. 1 is "yes" and 0 is "no"
    fps = 50                        # frame per second
    resolutionWidth = 640           # Width of frame
    resolutionHeight = 480          # Height of frame
    cameraDevice = 0                # select camera device
    check1 = False
    check2 = False

    cameraDevice = int(input("[INFOR]: Choose camera device: "))

    # Create a VideoCapture object
    cap = cv2.VideoCapture(cameraDevice)
    # Check if camera opened successfully
    if (cap.isOpened() == False): 
        print("[ERROR]: Unable to read camera feed")

    # try:
    #     # Create a VideoCapture object
    #     cap = cv2.VideoCapture(cameraDevice)
    #     break
    # except:
    #     # Check if camera opened successfully
    #     if (cap.isOpened() == False): 
    #         print("[ERROR]: Unable to read camera feed")
    #     print("[ERROR]: Cannot ")
    #     keyCameraDevice = input("[INFOR]: Change another camera? y/n?: ")
    #     if keyCameraDevice == "y":
    #         cameraDevice = input("[INFOR]: Camera device: ")

    # init resolution
    cap.set(3, resolutionWidth)
    cap.set(4, resolutionHeight)
    # wait to warming up
    time.sleep(1.0)
    # print init configuration
    print("[INFOR]: Output video path: " + videoPath)                # output video directory
    print("[INFOR]: Output image path: " + imagePath)                # output image directory
    print("[INFOR]: Video name extension: " + videoNameExtension)
    print("[INFOR]: Image name extension: " + imageNameExtension)
    if displayTime:
        print("[INFOR]: Display time: Yes")
    else:
        print("[INFOR]: Display time: No")
    print("[INFOR]: Frame per second of video record: " + str(fps))
    print("[INFOR]: Width: " + str(resolutionWidth))                 # Width of frame
    print("[INFOR]: Height: " + str(resolutionHeight))               # Height of frame
    print("[INFOR]: Camera device: " + str(cameraDevice))                  # camera decive

    print("----------------------------------------------")
    print("[GUIDE]: Press 'q' key to quit")
    print("[GUIDE]: Press 'r' key to start record video")
    print("[GUIDE]: Press 's' key to stop record video")
    print("[GUIDE]: Press 't' key to display current time onto the frame or not")
    print("[GUIDE]: Press 'i' key to take a photo")
    print("[GUIDE]: Press 'c' key to write the command")
    print("----------------------------------------------")

    # Wait to press 'Enter' to continue
    input("[GUIDE]: Press enter to starting video stream...")
    print("----------------------------------------------")

    # loop over frames from the video file stream
    while True:
        # grab the frame from the threaded video stream
        ret_frame, frame = cap.read()

        if ret_frame == True:
            # check to display current time on the frame or not
            if displayTime == 1:
                # get the date time current
                currentDateTime = datetime.now()
                # converting to format string
                currentDateTime_string = currentDateTime.strftime("%d/%m/%Y %H:%M:%S")
                # put date time text on frame
                cv2.putText(frame, currentDateTime_string, (10, frame.shape[0]-10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 1)

            # If the video writer is None *AND* we are supposed to write
            # the output video to disk initialize the writer
            if (writer is None) and (record != 0):
                writer = cv2.VideoWriter(videoPath + videoName + videoNameExtension,\
                    cv2.VideoWriter_fourcc(*"MJPG"), fps, (frame.shape[1], frame.shape[0]), True)
            
            # if the writer is not None, write the frame to odisk
            if writer is not None:
                cv2.putText(frame, "REC", (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                writer.write(frame)

            # display the frame onto the screen
            cv2.imshow("Frame", frame)

            # get input key
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):         # if the `q` key was pressed, break from the loop
                break
            elif key == ord("r"):       # starting record video
                if writer is None:
                    print("[INFOR]: Recording...")
                    videoName = currentDateTime.strftime("%d_%m_%Y_%H_%M_%S") # Video name
                    print("Video name: " + str(videoName) + str(videoNameExtension))
                    record = 1
            elif key == ord("s"):       # stop record video
                if writer is not None:
                    print("[INFOR]: Stop record!")
                    writer.release()
                    writer = None
                    record = 0
            elif key == ord("t"):       # display current time onto the frame or not
                displayTime = displayTime ^ 1 # XOR
                # another way:
                # displayTime = 1 - displayTime
                if displayTime:
                    print("[INFOR]: Display time: Yes")
                else:
                    print("[INFOR]: Display time: No")
            elif key == ord("i"):       # take the photo
                imageName = currentDateTime.strftime("%d_%m_%Y_%H_%M_%S") # Image name
                print("[INFOR]: Captured the image: " + str(imageName + imageNameExtension))
                cv2.imwrite(imagePath + imageName + imageNameExtension, frame)

            elif key == ord("c"):
                print("----------------------------------------------")
                print("[GUIDE]: Enter 'fps' to modify frame per second of the frame")
                print("[GUIDE]: Enter 'resol' to modify resolution")
                print("[GUIDE]: Enter 'came' to select camera device")
                print("----------------------------------------------")
                check1 = False

                keyCommand = input("Command?: ")
                if keyCommand == "fps":         # modify frame per second
                    fps = int(input("fps: "))
                elif keyCommand == "resol":       # modify resolution
                    resolutionWidth = int(input("Width: "))
                    resolutionHeight = int(input("Height: "))
                    cv2.destroyAllWindows()
                    cap.release()
                    print("[INFOR]: Wait a second to re-initialize...")
                    # Create a VideoCapture object
                    cap = cv2.VideoCapture(0)
                    # Check if camera opened successfully
                    if (cap.isOpened() == False): 
                        print("[ERROR]: Unable to read camera feed")
                    cap.set(3, resolutionWidth)
                    cap.set(4, resolutionHeight)
                    time.sleep(1.0)
                elif keyCommand == "cam": # select camera device
                    cameraDevice = int(input("Select camera: "))
                    cv2.destroyAllWindows()
                    cap.release()
                    print("[INFOR]: Wait a second to re-initialize...")
                    # Create a VideoCapture object
                    cap = cv2.VideoCapture(0)
                    # Check if camera opened successfully
                    if (cap.isOpened() == False): 
                        print("[ERROR]: Unable to read camera feed")
                    cap.set(3, resolutionWidth)
                    cap.set(4, resolutionHeight)
                    time.sleep(1.0)
                elif key == ord("q"):         # if the `q` key was pressed, break from the loop
                    break
        else:
            break

    # Cleanup
    cv2.destroyAllWindows()
    if writer is not None:
        writer.release()
    cap.release()

if __name__ == "__main__":
    RecordVideo()

#################################################
#                                               #
#         Created by Cao Le Cong Minh           #
#                                               #
#################################################
#   Gmail:  caolecongminh1997@gmail.com         #
#	Github: https://github.com/Minh-CaoLeCong   #
#################################################