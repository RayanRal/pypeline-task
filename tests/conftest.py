import subprocess
import time
import pytest
import requests
import os
import signal

@pytest.fixture(scope="session", autouse=True)
def run_mock_server():
    # Start the mock server
    server_path = os.path.join(os.path.dirname(__file__), "../mock_server/server.py")
    process = subprocess.Popen(["python3", server_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Wait for the server to be ready
    retries = 10
    while retries > 0:
        try:
            response = requests.get("http://127.0.0.1:5001/employees?page=1")
            if response.status_code == 200:
                break
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)
        retries -= 1
    
    if retries == 0:
        process.terminate()
        pytest.fail("Mock server failed to start")
        
    yield
    
    # Stop the mock server
    process.terminate()
    process.wait()
