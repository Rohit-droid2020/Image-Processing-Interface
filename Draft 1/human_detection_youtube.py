import cv2
import imutils
from functions import youtube_import
import pafy

url = youtube_import()
vPafy = pafy.new(url)
play = vPafy.getbest(preftype="mp4")

cap = cv2.VideoCapture(play.url)

# Initializing the HOG person
# detector


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#cap = cv2.VideoCapture('Pexels_Videos.mp4')
print("Video Captured")
while cap.isOpened():
    # Reading the video stream
    ret, image = cap.read()
    print("Stream started")
    if ret:
        print("Human found")
        image = imutils.resize(image,width=min(400, image.shape[1]))

        # Detecting all the regions
        # in the Image that has a
        # pedestrians inside it
        (regions, _) = hog.detectMultiScale(image,
                                            winStride=(8, 8),
                                            padding=(4, 4),
                                            scale=1.05)

        # Drawing the regions in the
        # Image
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y),
                          (x + w, y + h),
                          (0, 0, 255), 2)

        # Showing the output Image
        cv2.imshow("Image", image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()