from subprocess import Popen
import os

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    os.chdir('Generic_LSTM_Model_Builder')
    Popen(["streamlit", "run", "app.py", "--browser.serverAddress=0.0.0.0", "--browser.gatherUsageStats=False", "--server.enableCORS=False"])
