# Backoffice

Backoffice functions, such as analytics: teachable &amp; AR scripts

Use:
```python checkprovisioning.py```
which gives files in stdout and dir reports, e.g. ```missing_from_ac.csv```.

## Developer workflow

Clone the repo in a folder, and set up a Python virtual environment. In VSCode this is "Python: Create Environment", which will also pip install the requirements.

Fill `.env` with a valid TEACHABLE_API_KEY.

Dont run in decontainer, run in venv.

Run in debugger, or `python teachableapi.py`.

Run tests with `pytest` ?
