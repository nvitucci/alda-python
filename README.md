# alda-python
Python client for Alda (https://alda.io/).

[![Package version](https://img.shields.io/pypi/v/alda-python)](https://pypi.org/project/alda-python/)
[![Package status](https://img.shields.io/pypi/status/alda-python?color=blue)](https://pypi.org/project/alda-python/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

## Usage

1. Download and install Alda per the [Install instructions](https://alda.io/install/)
2. Run the Alda REPL as a server using port 12345:
   ```
   $ alda repl --server --port 12345
   ```
3. In a different terminal, run an interactive Python session (e.g. IPython)
4. Install `alda-python`
   ```
   !pip install --user alda-python
   ```
5. Import and initialize the Alda Python client:
   ```
   from alda import Client
   
   client = Client()
   ```
6. Create some Alda code, for example:
   ```
   code = """ 
       (tempo! 90) 
       piano:  
           o3 c1/e/g/b | f2/a/>c/e ~ <e2/g/b/>d 
       violin: 
           o2 c1 ~ | f2 ~ g2 
       percussion: 
           o2 [c8 r8 c8 r8 e8 c8 r8 c8] * 2 
   """
   ```
7. Play the code:
   ```
   client.play(code)
   ```