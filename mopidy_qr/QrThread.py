from pyzbar import pyzbar
import logging
import threading
import time

from mopidy import core

logger = logging.getLogger(__name__)

class QRThread:
    def __init__(self, config, core):
        self.config = config
        self.core = core
        self._running = threading.Event()
        self._thread = None
        logging.debug("Initializing QRThread")


    def start(self):
        if self._thread is not None:
            return
        logging.debug("Starting QRThread")
        
        self._running = threading.Event()
        self._running.set()
        self._thread = threading.Thread(target=self._loop)
        self._thread.start()

    def stop(self):
        logging.debug("Stopping QRThread")
        
        self._running.clear()
        self._thread.join()
        self._thread = None

    def _loop(self):
        logging.debug("Starting QR Reader")
       
        import imutils.video 

        logger.debug("Import conpleted")

        vs = imutils.video.VideoStream(usePiCamera=True).start()
        
        time.sleep(5.0)
        
        logger.debug("Initialization conpleted")

        while self._running.is_set():
            # grab the frame from the threaded video stream and resize it to
            # have a maximum width of 400 pixels
            frame = vs.read()
            frame = imutils.resize(frame, width=400)
            # find the barcodes in the frame and decode each of the barcodes
            barcodes = pyzbar.decode(frame)

            if len(barcodes) == 0:
                logger.debug("No barcodes found")

            # loop over the detected barcodes
            for barcode in barcodes:
                # extract the bounding box location of the barcode and draw
                # the bounding box surrounding the barcode on the image

                # the barcode data is a bytes object so if we want to draw it
                # on our output image we need to convert it to a string first
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type
                # draw the barcode data and barcode type on the image
                logger.info("[INFO] found barcode {} ({})".format(barcodeData, barcodeType))
                
                self.core.tracklist.clear()
                tracklist = self.core.tracklist.add(uris=[barcodeData]).get()

                self.core.playback.play(tracklist[0])
