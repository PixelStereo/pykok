# pykok

=====

**pykok** can be defined as a framework for creating inventory applications

It offers a way to organise your inventory with many levels such as location, suppliers, users, rental etc…
Every part of the application inherit from a Base Class.

For the moment, **pykok** is capable of:
-  Creating location (Create a Location Class)
-  ~~Creating item (Create an Item Class)~~
-  Move an item between different location (create a Movement Class)
-  Export reports to PDF files
-  Export inventory to csv format for opening with Libre Office
-  Create a group of x same items (same attributes)


####Documentation
---
Documentation is available online [on this page](http://pixelstereo.github.io/pykok)    

If you need/want to build the documentation from the repo, here are the steps : 

    pip install sphinx
    cd docs/source
    make html

####QuickStart
---
The tests.py contains a nice exemple to understand what you can do with pykok package.

####Development
---
Development is made on OSX with python 2.7.12    
Continious integration is made on linux for python 2 and 3.
