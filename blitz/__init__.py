import os


def get_include():
    import blitz
    """
    Return the directory that contains the Blitz++ reshape \\*.hpp header
    files.

    Extension modules that need to compile against Blitz++ reshape should use
    this function to locate the appropriate include directory.

    Notes
    -----
    When using ``distutils``, for example in ``setup.py``.
    ::

        import blitz
        ...
        Extension('extension_name', ...
                include_dirs=[blitz.get_include()])
        ...

    """
    d = os.path.join(os.path.dirname(blitz.__file__), 'include')
    return d


def get_cython_include():
    import blitz
    d = os.path.join(os.path.dirname(blitz.__file__), 'cython_include')
    return d


def get_lib():
    import blitz
    d = os.path.join(os.path.dirname(blitz.__file__), 'lib')
    return d
