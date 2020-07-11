from unittest import mock

import pykka
from mopidy import core
import time

from mopidy_qr import Extension
from mopidy_qr import frontend as frontend_lib

from . import dummy_audio, dummy_backend, dummy_mixer

dummy_config = {"qr": {"queue": ("true")}}
"""
with patch("pyzbar.decode") as decodefunction:
    decodefunction.return_value = [{"data": "dummy_data", "type": "dummy_type"}]


@mock.patch(
    "pyzbar.decode", return_value=[{"data": "dummy_data", "type": "dummy_type"}]
)
"""


@mock.patch("pyzbar.pyzbar")
class PyZBarTest:
    def decode(self, frame, qrcodes):
        return [{"data": "dummy_data", "type": "dummy_type"}]


@mock.patch("imutils.video.VideoStream")
class VideoStreamTest:
    def start(self):
        return self

    def read(self):
        return "dummyImage"


@mock.patch("imutils.video")
class VideoTest:
    def resize(self, frame, dimensions):
        return "dummyImage"


def stop_mopidy_core():
    pykka.ActorRegistry.stop_all()


def dummy_mopidy_core():
    mixer = dummy_mixer.create_proxy()
    audio = dummy_audio.create_proxy()
    backend = dummy_backend.create_proxy(audio=audio)
    return core.Core.start(audio=audio, mixer=mixer, backends=[backend]).proxy()


def test_setup():
    registry = mock.Mock()

    ext = Extension()
    ext.setup(registry)
    calls = [mock.call("frontend", frontend_lib.QRFrontend)]
    registry.add.assert_has_calls(calls, any_order=True)

    stop_mopidy_core()


def test_frontend_dummy_image():
    time.sleep(3)
    stop_mopidy_core()
