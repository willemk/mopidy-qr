import logging

import pykka
from mopidy import core

logger = logging.getLogger(__name__)


class QR1Frontend(pykka.ThreadingActor, core.CoreListener):

    def __init__(self, config, core):
        super().__init__()
  
        self.core = core
        self.config = config["qr"]

        logging.info("Initializing QR Frontend")

        from .QrThread import QRThread
        self.QrThread = QRThread(self.config, self.core)

    def on_start(self):
        logging.info("Starting QR Frontend")

        self.QrThread.start()


    def on_stop(self):
        logging.info("Stopping QR Frontend")
        self.QrThread.stop()

      



  
