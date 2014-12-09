def test_import():
    try:
        import beakeredis
    except ImportError as e:
        assert False
