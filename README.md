# Jupyter Notebook Library and webservice test

## Goal
  We want to be able to call an integration from inside of the Jupyter notebook since 
  developers will be prototyping there. Jupyter needs to be able to call a function 
  (e.g. `addTwoNums(2,3)`) and receive the result `5` without any additional setup of the webservices. 

 ## Setup
 1. Clone git repo
 1. Start web service
    ```
    # Build the container image (from inside this dir)
    docker build -t flask_app .
    
    # Run the container
    docker run --name flask_app -d -p 8080:8080 flask_app
    ```
 1. Kick off Jupyter Notebook and open .ipynb
    ```bash
    jupyter notebook
    # Via the Jupyter GUI, open the file wrapper_example.ipynb
    ```
 
## Pieces
### webServiceWrapper library
  1. will be wrapping an HTTP call to the deployed webservice
  1. The library will need to handle basic HTTP responses and exceptions
  1. Initial design of function can look like `addTwoNumbers(a, b)`
    
### Web Service for API requests
  1. Basic Flask setup for `/addTwoNums?num1=5&num2=4` as well as JSON payloads `{"num1": 1, "num2": 4}` 
  1. Docker container for webservice

### Importing library into jupyter notebook:
  See `wrapper_example.ipynb`
  
  References: https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/

## Stretch Goals
1. Given the framework, how would we target addTwoNums() A deployment versus addTwoNums() B deployment from the notebook? 
Think about how the web service is advertised, discovered, 
and accessed so that a production release would be able to hav A/B testing of the webservice function.
    1. Talk slides explaining multiple service discovery options: https://ep2017.europython.eu/media/conference/slides/service-discovery-for-dynamic-python-applications.pdf 
1. ~~Dockerize webservice~~
