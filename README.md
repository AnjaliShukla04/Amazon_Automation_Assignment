# Amazon_Automation_Assignment

**🛒 Amazon Product Automation Script**
This Python script automates the process of searching for products on Amazon India using Selenium WebDriver. It demonstrates the following actions:

1)Searching for a random product and verifying no results are found.
2)Searching for a valid product (Laptop), selecting the first result, adding it to the cart.
3)Changing the quantity of the product in the cart and then removing it.


**✨ Key Features**
1)Automated Search: Search for any product on Amazon and handle "no results found."
2)Product Interaction: Select a product, navigate through pages, and perform cart operations.
3)Dynamic Element Handling: Waits for elements to load and clicks dynamically on product listings.
4)Cart Manipulation: Adds items to the cart, updates the quantity, and removes them efficiently.


**🛠️ Prerequisites**
Make sure you have the following installed before running the script:

1)Python 3.x 🐍
2)Selenium WebDriver 📦
3)Google Chrome 🌐 (or any other compatible browser)
4)ChromeDriver executable matching your Chrome version

You can install Selenium using pip: 
        pip install selenium

**🖥️ Installation**
1)Clone the repository or download the Python script:
        git clone https://github.com/yourusername/amazon-automation.git
2)Download the appropriate version of ChromeDriver and place it in a known directory.
3)Update the Service path in the script to point to the location of your ChromeDriver:
        service=Service(r'C:\path\to\your\chromedriver.exe')
4)Install the necessary Python dependencies using:
        pip install -r requirements.txt


**🚀 Usage**
1)Open the terminal and navigate to the directory containing the script.
2)Run the script using Python:
        python amazon_automation.py
3)The script will:
~Search for a product called "Flibbertygibbet 3000" and verify the absence of results.
~Search for "Laptop", select the first product, add it to the cart.
~Change the quantity to 2, and finally remove the item from the cart.

**🛑 Notes**
1)Ensure that your ChromeDriver version matches your Chrome browser version.
2)The script is built specifically for Amazon India (www.amazon.in), and XPaths might differ for other Amazon domains.
3)The script waits for up to 10 seconds for elements to load; you can adjust this based on your internet speed.

**📂 Project Structure**
📦 amazon-automation
 ┣ 📜 amazon_automation.py      # Main script
 ┗ 📜 README.md                 # Documentation

 **👨‍💻 Contributing**
Feel free to fork this repository, create a new branch, and submit a pull request. All contributions are welcome! 🎉

**📧 Contact**
For any issues, feel free to contact me at anjalishukla0409@gmail.com.
