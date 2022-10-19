## How to do ultraviolence

##### OS: Ubuntu 22.04.1 LTS 64 bit
##### Python 3.11 and 3.10

1. Create two virtual enviroments with Python 3.10 and Python 3.11 as base interpreters.
As a total noob, I have just used PyCharm. 
a) create a new project with _ultraviolence.py_.
b) in Interpreter Settings (Ctrl+Alt+S) push "Add interpreter" -> "Add Local Interpreter".
c) create a new **Venv** enviroment with Python 3.10. It will be useful to name Venv folder as "**venv10**".
d) In the same manner create **Venv** enviroment with Python 3.11 in folder "**venv11**".

2. For greater convinience, divide _requirements.txt_ in two separate .txt files with different packages. 
_I done it for you, _requirements10.txt_ and _requirements11.txt_ are properly divided _requirements.txt_.
In _requirements10.txt_ there are only packages which can't be installed in enviroment with Python 3.11, and a specific version of _pandas_.

3. In command line activate Venv with Python 3.10.
Simplest way is to run terminal from _/bin_ folder in _venv10_ and run `source activate`.

4. Run `pip install -r requirements10.txt`.

5. Do the same two steps for enviroment with Python 3.11 and _requirements11.txt_.

6. Copy all the files from _~/.../venv10/lib/Python3.10_ to _~/.../venv11/lib/Python3.11_ *WITHOUT OVERWRITING*.

7. Go to the _~/.../venv11/lib/Python3.11/site-packages/pandas/core_ and delete _frame.py_.

8. Copy  _~/.../venv10/lib/Python3.10/site-packages/pandas/core/frame.py_ into _~/.../venv11/lib/Python3.11/site-packages/pandas/core_

9. Run _ultraviolence.py_ with Python 3.11


Ultraviolence is done.
