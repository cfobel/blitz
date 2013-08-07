blitz
=====

This package wraps the [Blitz++][1] C++ library in a Python package to make it
easy to install.

# Usage #

From the command-line, the `include` or `lib` paths for the installed Blitz++
package can be obtained by running:

    python -c "import blitz; print blitz.get_include()"

or:

    python -c "import blitz; print blitz.get_lib()"

# Cython bindings #

There are also Cython definitions with limited support for Blitz++ `Array` and
`TinyVector` types in the file `cython_include/blitz.pxd`.  The path to
`cython_include` can be obtained by running:

    python -c "import blitz; print blitz.get_cython_include()"

[1]: https://github.com/syntheticpp/blitz
