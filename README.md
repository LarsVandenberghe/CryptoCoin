CryptoCoin
=======

This is a python widget displaying the latest values of crypto currencies.
This version only works in python 3 with pyqt4.

Download links: python + dependency:
-------------

  Download python3.5
  https://www.python.org/ftp/python/3.5.4/python-3.5.4-amd64.exe
  
  
  Download PyQt4 64-bit:
  http://www.silx.org/pub/wheelhouse/PyQt4-4.11.4-cp35-none-win_amd64.whl
  
  Download PyQt4 32-bit:
  http://www.silx.org/pub/wheelhouse/PyQt4-4.11.4-cp35-none-win32.whl
  
  
You don't have python 3.5 instaled:
-------------
  
  Once downloaded, start installing python. For the sake of making it easy, check "Add Python 3.5 to PATH" 
  and click on "Install Now". (If you don't want to add python to the path, please remember where you installed python.exe and use "C:\Users\PATH\TO\python.exe" instead of "python" in Command Shell.)
  
Installing PyQt4:
-------------

  Open cmd (Command Shell) and type 'python --version'. Make sure you have Python 3.5.
  Now navigate to the directory where you downloaded PyQt4. Use: 'cd "C:\Users\SOME\DIRECTORY"'.
  If you are in the directory where the .whl file is stored, type: 'python -m pip install <name of the .whl>'.
  Once the wheel is installed, you can delete the python installer and the .whl file.
  
  * summary:
     - python --version
     - cd "C:\Users\DIRECTORY\WHERE\WHL\IS\STORED"
     - python -m pip install <name of the .whl>
  
  * example:
     - python --version
     - cd "C:\Users\MYUSERNAME\Downloads"
     - python -m pip install PyQt4-4.11.4-cp35-none-win_amd64.whl
  
Running the App:
-------------

  * Download the Zip and extract the files. Place the folder on a location you like. To run the app, I advise you to make a new shortcut. To do this you need to go to the python installation directory. If you clicked on "Install Now" it will be something like this: "C:\Users\MYUSERNAME\AppData\Local\Programs\Python\Python35".
  In that directory there should be a file called: "pythonw.exe". That makes the following path: "C:\Users\MYUSERNAME\AppData\Local\Programs\Python\Python35\pythonw.exe".
  
  * Right click the "CryptoCoin.py" file and create a shortcut. Now rightclick the shortcut and edit the propperties. Add the pythonw.exe path infront of the Target line. It should look something like this: <br>
  
  "C:\Users\MYUSERNAME\AppData\Local\Programs\Python\Python35\pythonw.exe" "C:\Users\MYUSERNAME\Projects\CryptoCoin Widget\CryptoCoin.py"
   
Start the App with your computer:
-------------

Copy the shortcut and place it in your startup folder.
"C:\Users\MYUSERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
