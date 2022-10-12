# RoombaTestSuite

This test suite works with Python, Pytest and Allure. Python use requests library to make the API calls, then Pytest helps with the console reporting and asserts and then generates an HTML report of the results with Allure.


## Installation

Install python 
```bash
sudo apt update
sudo apt install python3
apt-get update
```
Install pip
```bash
sudo apt-get update
sudo apt-get install python-pip
```
Install allure
```bash
curl -o allure-2.13.8.tgz -OLs https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz
sudo tar -zxvf allure-2.13.8.tgz -C /opt/
sudo ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure
allure --version
```
Source: https://askubuntu.com/questions/1322255/failing-to-install-allure-2-13-8-on-ubuntu-20-04-2-lts-manually

Install JAVA
```bash
sudo apt install default-jdk
sudo apt install default-jre
```
Java is necessary to run the allure service  

Install virtualenv
```bash
sudo pip3 install virtualenv 
```
Create and activate virtual environment
```bash
virtualenv venv 
source venv/bin/activate
```
Install requirements
```bash
sudo pip3 install requirements 
```
Install requets
```bash
sudo pip3 install requests 
```
Install pytest
```bash
sudo pip3 install pytest
```
Install allure
```bash
sudo pip3 install allure
```
Install Git
```bash
sudo pip3 install git
```
Clone repository

## Usage

Inside the repository  

To run the test cases:
```bash
pytest RoombaTest.py --alluredir=allure-report
```
To generate allure report:
```bash
allure serve allure-report
```
