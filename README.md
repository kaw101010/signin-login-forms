# Sign Up and Login Form 

## Table of Contents
* [Description](#description)
* [Setup](#setup)
* [Features](#features)


## Description
Sign Up and Login forms made with **HTML**, **CSS** and **JavaScript**. Implemented APIs in the back-end with **Flask** and use **jinja** for html templates.
Also used **SQL** to maintain a database of registered users.
Validated emails by sending OTPs using **SMTP** protocol.

## Setup
To run this project, clone this repository and navigate to the project directory.

Then run ```pip install -r requirements.txt``` to install the required Python dependencies.

Run this project by running ```python -m flask run``` in the project directory.

## Features
* You can register on the website using your email and a password
* Password Validation is also done to ensure that the password strength is high.
* An email containing an OTP will be sent to your email address to authenticate your email address.
* You cannot re-register on the website with the same email address.
