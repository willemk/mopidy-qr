from pyzbar import pyzbar
import threading
import time
import logging
import pykka
from mopidy import core

logger = logging.getLogger(__name__)


class QRFrontend(pykka.ThreadingActor, core.CoreListener):

    def __init__(self, config, core):
        super().__init__()

        self.core = core
        self.config = config["qr"]

        logging.info("Initializing QR Frontend")

        self.QRReaderThread = QRReaderThread(self.config, self.core)

    def on_start(self):
        logging.info("Starting QR Frontend")

        self.QRReaderThread.start()

    def on_stop(self):
        logging.info("Stopping QR Frontend")
        self.QRReaderThread.stop()

class QRReaderThread:

    def __init__(self, config, core):
        self.parseConfig(config)
        self.core = core
        self._running = threading.Event()
        self._thread = None
        logging.debug("Initializing QRThread")

    def parseConfig(self, config):
        self.queue = config["queue"]

        logger.debug("Queue Setting: {}".format(self.queue))

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

        self.latestUrl = ""
        while self._running.is_set():
            # grab the frame from the threaded video stream and resize it to
            # have a maximum width of 400 pixels
            frame = vs.read()
            frame = imutils.resize(frame, width=400)

            # find the barcodes in the frame and decode each of the barcodes
            # List of supported barcodes 
            # https://github.com/NaturalHistoryMuseum/pyzbar/blob/443586145104fbdf52d4da47eaee833286435cc7/pyzbar/wrapper.py#L41
            barcodes = pyzbar.decode(frame, [pyzbar.ZBarSymbol.QRCODE])

            # loop over the detected barcodes
            for barcode in barcodes:

                data = barcode.data.decode("utf-8")

                logger.info("Found barcode {} ({})".format(data, barcode.type))

                # Ensure we only read once
                if self.latestUrl == data:
                    time.sleep(1)
                    continue
                self.latestUrl = data

                if self.queue:
                    self.core.tracklist.add(uris=[data])
                else:
                    self.core.tracklist.clear()
                    tracklist = self.core.tracklist.add(uris=[data]).get()
                    if len(tracklist) > 0:
                        self.core.playback.play(tracklist[0])

        vs.stream.release()
