from distutils.core import setup, Extension

core_ext = Extension(
    name                = 'core',
    sources             = ['lib/python/core.cpp'],
    include_dirs        = ['include/cpp'],
    library_dirs        = ['lib'],
    extra_compile_args  = ["-O3", "-Wall"],
    language            = 'c++'
)

graphics_ext = Extension(
    name                = 'graphics',
    sources             = ['lib/python/graphics.cpp'],
    include_dirs        = ['include/cpp'],
    library_dirs        = ['lib/cpp'],
    extra_compile_args  = ["-O3", "-Wall"],
    language            = 'c++'
)

setup(
    name                = 'app',
    version             = '0.0.1',
    author              = 'Christoph Pader-Barosch',
    author_email        = 'chrispad2k@gmail.com',
    ext_modules         = [core_ext, graphics_ext],
)
