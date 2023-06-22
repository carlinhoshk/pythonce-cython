import os
from os.path import join
from setuptools import setup, Extension
from Cython.Build import cythonize


directory_path = os.path.dirname(
    os.path.abspath(__file__)
    )

ext_data = {
    'pythonce.ola.wrap_ola': {
        'sources': [
            join(directory_path, 'pythonce', 'ola', 'wrap_ola.pyx'),
            join(directory_path, 'pythonce', 'ola', 'ola.c')]
    },
    'pythonce.calculator.cal': {
        'sources': [
            join(directory_path, 'pythonce', 'calculator', 'cal.pyx')]}
}

extensions = []

for name, data in ext_data.items():

    sources = data['sources']
    include = data.get('include', [])

    obj = Extension(
        name,
        sources=sources,
        include_dirs=include
    )
    
    extensions.append(obj)


# Use cythonize on the extension object.
setup(
    name='pythonce',
    author='Carlinhoshk',
    #package_dir={'pythonce': ''},
    ext_modules=cythonize(extensions)
    )