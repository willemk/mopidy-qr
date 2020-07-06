# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2

# construct the argument parser and parse the arguments 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, default="",
                help="path to output CSV file containing barcodes")
args = vars(ap.parse_args())

# open the output CSV file for writing and initialize the set of
# barcodes found thus far
if args["input"] != "":
	print("[INFO] using static image {}".format(args["input"]))

	image = cv2.imread(args["input"])
	barcodes = pyzbar.decode(image)

	if len(barcodes) == 0:
		print("[INFO] No barcodes found")

	# loop over the detected barcodes
	for barcode in barcodes:
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type
		print("[INFO] found barcode {} ({})".format(barcodeData, barcodeType))
else:
	
	# initialize the video stream and allow the camera sensor to warm up
	print("[INFO] starting video stream...")

	# vs = VideoStream(src=0).start()
	vs = VideoStream(usePiCamera=True).start()
	time.sleep(5.0)
	# loop over the frames from the video stream
	while True:
		# grab the frame from the threaded video stream and resize it to
		# have a maximum width of 400 pixels
		frame = vs.read()
		frame = imutils.resize(frame, width=400)
		# find the barcodes in the frame and decode each of the barcodes
		barcodes = pyzbar.decode(frame)

		if len(barcodes) == 0:
			print("[INFO] No barcodes found")

		# loop over the detected barcodes
		for barcode in barcodes:
			# extract the bounding box location of the barcode and draw
			# the bounding box surrounding the barcode on the image

			# the barcode data is a bytes object so if we want to draw it
			# on our output image we need to convert it to a string first
			barcodeData = barcode.data.decode("utf-8")
			barcodeType = barcode.type
			# draw the barcode data and barcode type on the image
			print("[INFO] found barcode {} ({})".format(barcodeData, barcodeType))

# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")


# From # https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/
# sudo apt-get install libzbar0
# pip3 install pyzbar
# pip3 install imutils

 from imutils.video import VideoStream
 from pyzbar import pyzbar
 import imutils
 import time

 vs = VideoStream(usePiCamera=True).start()
  time.sleep(5.0)

   while True:
        # grab the frame from the threaded video stream and resize it to
        # have a maximum width of 400 pixels
        frame = vs.read()
         frame = imutils.resize(frame, width=400)
          # find the barcodes in the frame and decode each of the barcodes
          barcodes = pyzbar.decode(frame)

           if len(barcodes) == 0:
                logging.log(logging.INFO, "No barcodes found")

            # loop over the detected barcodes
            for barcode in barcodes:
                # extract the bounding box location of the barcode and draw
                # the bounding box surrounding the barcode on the image

                # the barcode data is a bytes object so if we want to draw it
                # on our output image we need to convert it to a string first
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type
                # draw the barcode data and barcode type on the image
                logging.log(logging.DEBUG, "Found barcode {}({})".format(
                    barcodeData, barcodeType))

                #core.tracklist.add()
