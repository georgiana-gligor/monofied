# Create a monorepo

# Setup

Create a virtualenv:
```bash
$ virtualenv py27

New python executable in /Users/g/Sites/tekkie/monorepo/py27/bin/python2.7
Also creating executable in /Users/g/Sites/tekkie/monorepo/py27/bin/python
Installing setuptools, pip, wheel...done.
```

Activate it:
```bash
$ . py27/bin/activate
```

Install dependencies:
```bash
$ pip install --editable .

Obtaining file:///Users/g/Sites/tekkie/monorepo
Collecting Click (from monorepo==0.1)
  Using cached click-6.7-py2.py3-none-any.whl
Installing collected packages: Click, monorepo
  Running setup.py develop for monorepo
Successfully installed Click-6.7 monorepo
```

## Usage

```bash
(py27) $ monorepo
```
