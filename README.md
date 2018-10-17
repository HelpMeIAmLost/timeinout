# TimeInOut
## Description
A set of Python scripts to automate time in and time out for the e-PayStamp system.

## Requirements
Aside from the libraries listed in the requirements.txt file, I used the following:
*  [Python 3.7](https://www.python.org/downloads/release/python-370/)
*  [Google Chrome 69.0.3497.100](https://www.google.com/chrome/)
*  [ChromeDriver 2.42](https://chromedriver.storage.googleapis.com/index.html?path=2.42/)

### What's in `requirements.txt`?
*  Selenium 3.14.1

## Usage
Update the first 3 lines of the `info.txt` file with the following information (should be in the same order):
*  企業コード (Company Code)
*  社員番号 (Employee Number)
*  パスワード (Password)
The `timein.py` script opens up a Google Chrome browser, loads the e-PayStamp log-in page, logs in automatically using the information in the `info.txt` file and clicks the 出勤 button to clock-in the user's time in.
The `timeout.py` does the same thing except that it clicks the 退勤 button instead to clock-in the user's time out.