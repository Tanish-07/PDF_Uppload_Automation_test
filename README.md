**📂 PDF Upload Automation Test**
=================================

This project automates the testing of file upload functionality using **Selenium WebDriver** and **Pytest**. It validates whether a PDF file can be successfully uploaded to the demo site [The Internet – File Upload](https://the-internet.herokuapp.com/upload).

**🚀 Features**
---------------

*   Automates file upload functionality.
    
*   Uses the **Page Object Model (POM)** for a better test structure.
    
*   Implements **Pytest** as the testing framework.
    
*   Uses **webdriver-manager** to automatically handle browser drivers.
    
*   Includes sample **test data** (valid\_document.pdf and invalid\_file.txt).
    

**📂 Project Structure**
------------------------

```
QACondaTest/
│
├── test_data/
│   ├── valid_document.pdf       # Valid file for testing
│   └── invalid_file.txt         # Example invalid file
│
├── test_main_flow.py            # Main automation test script
└── requirements.txt             # Project dependencies
```
**🛠️ Setup Instructions**
--------------------------

### **1\. Clone the repository**
```
git clone [https://github.com/your-username/PDF_Upload_Automation_test.git](https://github.com/your-username/PDF_Upload_Automation_test.git)
cd PDF_Upload_Automation_test
```
### **2\. Install dependencies**

Since you are not using a virtual environment right now, you can install the required packages directly:
```
pip install -r requirements.txt
```
This will install:

*   Selenium
    
*   Pytest
    
*   webdriver-manager
    

**▶️ Running the Tests**
------------------------

To execute the tests, run the following command in your terminal:
```
pytest -v
```
Pytest will perform the following actions:

1.  Launch the Chrome browser.
    
2.  Open the file upload page.
    
3.  Upload the test\_data/valid\_document.pdf file.
    
4.  Validate that the success message "File Uploaded!" appears.
    

✅ If the upload is successful, the test will pass.

**📘 Dependencies**
-------------------

All required dependencies are listed in requirements.txt:
```
selenium
pytest
webdriver-manager
```
**✅ Example Test Case**
-----------------------

**Test Name:** test\_successful\_upload

**Steps:**

1.  Navigate to the upload page.
    
2.  Select valid\_document.pdf from the test\_data directory.
    
3.  Click the submit button.
    
4.  Verify that the "File Uploaded!" message is displayed.
    

**Expected Result:** The file upload is successful.
