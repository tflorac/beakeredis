def test_import():
    try:
        import beakeredis
    except ImportError:
        assert False
