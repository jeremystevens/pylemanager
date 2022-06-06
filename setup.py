from pathlib import Path
from setuptools import find_packages, setup

readme = Path(__file__).parent / 'README.md'

setup(name='pylemanager',
      version='1.0.0',
      description="A simple file manager",
      long_description=readme.read_text(),
      long_description_content_type='text/markdown',
      url='https://github.com/jeremystevens/pylemanager',
      doc_url='https://readthedocs.org/projects/pylemanager/',
      author='Jeremy Stevens',
      author_email='jeremiahstevens@gmail.com',
      maintainer='jeremystevens',
      license='MIT',
      license_file='LICENSE',
      packages=find_packages(),
      scripts=['run.py'],
      include_package_data=True,
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
      ],
      python_requires='>=3.7',
      install_requires=['simple_term_menu','art','tqdm','glob', 'shutil'],
      zip_safe=False)