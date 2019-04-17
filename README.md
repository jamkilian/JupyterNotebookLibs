# Jupyter Notebook Library and webservice test

## Goal
  We want to be able to call an integration from inside of the Jupyter notebook since 
  developers will be prototyping there. Jupyter needs to be able to call a function 
  (e.g. `addTwoNums(2,3)`) and receive the result `5` without any additional setup of the webservices. 

 ## Setup
 ```
 # Install requirements for pip packages
 pip install -r requirements.txt
 # Start flask app
 python BasicWebService.py

 ```
 
## Pieces
### webServiceWrapper library
  1. will be wrapping an HTTP call to the deployed webservice
  1. The library will need to handle basic HTTP responses and exceptions
  1. Initial design of function can look like `addTwoNumbers(int a, int b)`
    
### Web Service for API requests
  1. Basic Flask setup for `/addTwoNums?num1=5&num2=4`
  1. Docker container for webservice

### Importing library into jupyter notebook:
  1. https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/

## Stretch Goals
1. Given the framework, how would we target addTwoNums() A deployment versus addTwoNums() B deployment from the notebook? 
Think about how the web service is advertised, discovered, 
and accessed so that a production release would be able to hav A/B testing of the webservice function.
 