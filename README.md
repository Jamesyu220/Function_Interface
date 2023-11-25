# Describe Function  

## Table of contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Getting Started](#getting-started)
* [Demos and Examples](#demos-and-examples)
* [License](#license)
* [Reference](#reference)
* [Contributors](#contributors)
<!-- * [Evaluation and Results](#evaluation-and-results) -->

## Introduction
The function DescribeFunction takes another function as input, and the output is the input parameters and return type of that function, helping users figure out the input and output of a function and know how to use it.

## Technologies
Project is created with:
* Python 3.8
* Jupyter Notebook 6.4.12
* Python libraries (see /requirements.txt)
* VSCode

## Getting Started
To run this project, 
1. Clone the repo:
   ```sh
   git clone https://github.com/Jamesyu220/describe_function.git
   ```
2. Install [packages](#technologies)

3. Install EvaDB
    Please refer to the website of EvaDB to setup the environment.  
    https://evadb.readthedocs.io/en/stable/source/overview/getting-started.html

4. Install python libraries
   ```sh
   pip install -r requirements.txt
   ```
5. Run describe-function.ipynb:  

6. Modify the value of ```module_name``` and ```function_name``` to get the information about the function you want.  

## Demos and Examples
Input:  
Module: replicate  
Function: run  

Output:  
Function Parameters:  
ref: <class 'str'>  
input: typing.Optional[typing.Dict[str, typing.Any]]  
params: typing_extensions.Unpack[ForwardRef('Predictions.CreatePredictionParams')]  

Return Type:  
typing.Union[typing.Any, typing.Iterator[typing.Any]]  

## License
Distributed under the Apache License. See LICENSE for more information.  

## Reference 
[1] EvaDB: https://evadb.readthedocs.io/en/stable/source/overview/getting-started.html  
[2] Describe Function:  https://spark.apache.org/docs/3.0.0-preview/sql-ref-syntax-aux-describe-function.html  
[3] Snowpark function interface: https://docs.snowflake.com/en/developer-guide/snowpark/python/creating-udfs  

## Contributors
* [James Yu](https://github.com/Jamesyu220)  
---