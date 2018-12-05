"""
run the app at port 5001
debug is equal to true
"""
# run.py
#import app from app
from app import app

if __name__ == '__main__':
    app.run(port=5001, debug=True)
