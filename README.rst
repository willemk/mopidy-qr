****************************
Mopidy-QR
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-QR
    :target: https://pypi.org/project/Mopidy-QR/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/circleci/build/gh/willemk/mopidy-qr
    :target: https://circleci.com/gh/willemk/mopidy-qr
    :alt: CircleCI build status

.. image:: https://img.shields.io/codecov/c/gh/willemk/mopidy-qr
    :target: https://codecov.io/gh/willemk/mopidy-qr
    :alt: Test coverage

Mopid extension for adding tracks via a QR code


Installation
============

Install by running::

    python3 -m pip install Mopidy-QR

See https://mopidy.com/ext/qr/ for alternative installation methods.


Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-QR to your Mopidy configuration file::

    [qr]
    # TODO: Add example of extension config

And run the following to add the proper user permissions:
```
sudo usermod -a -G video mopidy
```


Project resources
=================

- `Source code <https://github.com/willemk/mopidy-qr>`_
- `Issue tracker <https://github.com/willemk/mopidy-qr/issues>`_
- `Changelog <https://github.com/willemk/mopidy-qr/blob/master/CHANGELOG.rst>`_


Credits
=======

- Original author: `Willem Kappers <https://github.com/willemk>`__
- Current maintainer: `Willem Kappers <https://github.com/willemk>`__
- `Contributors <https://github.com/willemk/mopidy-qr/graphs/contributors>`_
