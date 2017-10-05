# omnic-demo

Demo server configuration

## Setting up a dev environment

NOTE: Will not have system dependencies installed with this methodology, natch

1. Install Python 3, including `pip` and `venv`:

   -  On Debian-based distros:

      -  `sudo apt-get install python3 python3-env python3-pip`

   -  On macOS, use something like `brew`

2. Create a virtualenv. For example:

   -  `mkdir -p ~/.venvs/`
   -  `python3 -m venv ~/.venvs/omnic-demo`

3. Activate virtualenv:

   -  `source ~/.venvs/omnic/bin/activate`
   -  You will need to do this any time you want to work

4. Install dependencies:

   -  `pip install -r requirements.txt`

5. Start the server:

   -  `omnic runserver`
