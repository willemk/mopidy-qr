from mopidy_qr import Extension


def test_get_default_config():
    ext = Extension()

    config = ext.get_default_config()

    assert "[qr]" in config
    assert "enabled = true" in config
    assert "queue = true" in config


def test_get_config_schema():
    ext = Extension()

    schema = ext.get_config_schema()

    assert "enabled" in schema
    assert "queue" in schema
