from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension(
        "nw_ec_alignx",
        ["nw_ec_alignx.pyx"],
        include_dirs=[numpy.get_include()],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        extra_compile_args=['-Wno-unreachable-code', '-Wno-unreachable-code-fallthrough']
    )
]

setup(
    name="nw_ec_alignx",
    ext_modules=cythonize(
        extensions,
        compiler_directives={
            'language_level': "3",
            'boundscheck': False,
            'wraparound': False
        }
    )
)
