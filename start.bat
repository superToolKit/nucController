C:
CD "C:\nucController"
if exist venv\Scripts\ (
    rem do nothing
) else (
    py -m venv venv
)
call .\venv\Scripts\activate && pip3 install -r requirements.txt
.\dist\scheduledRestart.exe
call python nucController.py
