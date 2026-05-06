# SpeedTester
A simple speed test logger using a modified version of [the SpeedTest++ library](https://github.com/taganaka/SpeedTest).
This program is designed to work with Linux systems. It has not been tested with Windows.

# Download
` git clone --recurse-submodules https://github.com/thumperfuzzy/SpeedTester.git`    
Make sure to use the --recurse-submodules flag when cloning. This ensures that you get the SpeedTest library when downloading.

# Usage
1. SpeedTest library
    
    Make sure you have the following:
* A modern C++ compiler
* cmake
* libcurl
* libssl
* libxml2

  Then you should be able to run `./makeExec.sh` to make the executable. If that doesn't work follow the instructions in the [README.md](https://github.com/thumperfuzzy/SpeedTest/blob/be39bfc37f69b40e244aef67ac0e57bdf5f4095a/README.md) for the SpeedTest library.

2. Logging Script

   a. Install the python requirements:
   
   If you have an older version of pip, you can simply use `pip install -r requirements.txt`

   If you have a newer version of pip, you will need to setup a virtual environment first:    
   ```
   python -m venv ./venv
   source ./venv/bin/activate
   pip install -r requirements.txt
   ```
  b. run `./makeenv.sh`    
  c. `python testSpeed.py`
