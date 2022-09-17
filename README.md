# alda-python
Python client for Alda (https://alda.io/).

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