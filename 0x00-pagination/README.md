# 0x00. Pagination
Back-end

+ By Emmanuel Turlay, Staff Software Engineer at Cruise
### Concepts
For this project, we expect you to look at this concept:

+ [Back-end concepts](https://github.com/geeflows44/alx-backend/tree/master/0x00-pagination)
  
## Resources
### Read or watch:

+ [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)
+ [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google:**

+ How to paginate a dataset with simple page and page_size parameters
+ How to paginate a dataset with hypermedia metadata
+ How to paginate in a deletion-resilient manner

## Requirements
+ All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
+ All your files should end with a new line
+ The first line of all your files should be exactly `#!/usr/bin/env python3`
+ A `README.md` file, at the root of the folder of the project, is mandatory
+ Your code should use the  `pycodestyle` style (version 2.5.*)
+ The length of your files will be tested using `wc`
+ All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
+ All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
+ A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of 
  it will be verified)
+ All your functions and coroutines must be type-annotated.
## Setup: `Popular_Baby_Names.csv`
[use this data file](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230722%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230722T152254Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=184f5f42940425d6233aa8a3d9969f339e9840a47ccd2bfc1cf77f7399e2a584) for your project
