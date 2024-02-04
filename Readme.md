# How to Run
1. install python on your computer ([how to](https://www.python.org/downloads/release/python-3121/))
2. confirm python installation by running `python --version` or `python3 --version` on your computer's terminal/CMD
    - if it shows `Python 3.12.1` then you're ok
3. install git on your computer ([how to](https://git-scm.com/download/win))
4. confirm git installation by running `git --version`
    - if it shows `git version ......` then you're ok
5. open terminal:
    - enter `C:\Users\user\Desktop`, and then enter `git clone <this repo>`
    - enter `cd coshztock_app`
    - enter `python -m venv venv` or `python3 -m venv venv`
    - enter `venv\Scripts\activate`
    - enter `pip install -r requirements.txt`
    - enter `streamlit run streamlit_app.py`, and the app should be running locally!