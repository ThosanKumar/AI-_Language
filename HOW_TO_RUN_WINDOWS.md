# Language Tutor AI - How to run on Windows

## 1. Prerequisites
- Python 3.12 or 3.13 (https://www.python.org/downloads/windows/)
  During install, tick **"Add python.exe to PATH"**.
- A Google AI Studio API key (https://aistudio.google.com/) - needed for the AI pages.

Check in Command Prompt (CMD):

    python --version
    pip --version

## 2. Unzip
Right-click `Language_Tutor_AI.zip` -> **Extract All...** (e.g. to the Desktop).

## 3. Add your API key
Inside the extracted folder:
1. Open `.streamlit` folder.
2. Copy `secrets.toml.example` and rename the copy to `secrets.toml`.
3. Open it in Notepad and replace the placeholder:

       GOOGLE_API_KEY = "paste_your_real_key_here"

Never share this file or commit it to GitHub (it is already in `.gitignore`).

## 4a. Easiest way
Double-click **setup_and_run.bat**. It creates a virtual environment, installs
requirements and starts the app. The browser opens at http://localhost:8501.

## 4b. Manual way (CMD)
Open the extracted folder, click the address bar, type `cmd`, press Enter:

    python -m venv .venv
    .venv\Scripts\activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    python -m streamlit run app.py

Press **Ctrl+C** in the terminal to stop. To run again later:

    .venv\Scripts\activate
    python -m streamlit run app.py

(If `python` is not recognised, use `py` instead.)

## 5. Optional demos
    python -m streamlit run widgets_demo.py
    python -m streamlit run state_demo.py
    python -m streamlit run streamlit_fundamentals_demo.py

## Troubleshooting
| Problem | Fix |
|---|---|
| `python` not recognised / opens Microsoft Store | Reinstall Python with "Add to PATH", or use `py`; disable python.exe app alias in Windows Settings |
| `No module named streamlit` | Activate the venv and run `python -m pip install -r requirements.txt` |
| pip cannot find a pinned version | Edit `requirements.txt`, remove the `==x.y.z` part of that line, reinstall |
| `Google API key not found` | Create `.streamlit\secrets.toml` as in step 3 |
| Model not found / 404 error | Open `services\ai_service.py` and `services\speech_service.py`, change `MODEL_NAME` to a Gemini model available to your key (e.g. `gemini-2.5-flash`) |
| Quota / 429 error | Wait a while or check your quota in Google AI Studio |
| Microphone not working | Allow microphone permission for localhost in the browser |
| Port 8501 busy | `python -m streamlit run app.py --server.port 8502` |

## Deploy
Push to your own GitHub repo (without secrets.toml), then create the app at
https://share.streamlit.io/ with entry point `app.py` and add `GOOGLE_API_KEY`
under App secrets.
