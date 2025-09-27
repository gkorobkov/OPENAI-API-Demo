@ECHO OFF
rem https://www.geeksforgeeks.org/python/dependency-tree-of-a-python-module/
rem pipdeptree | grep -P '^\w+'
rem pipdeptree -f --warn silence | grep -P '^[\w0-9\-=.]+'
@ECHO ON
pipdeptree | findstr /i "=="  
pipdeptree | findstr /i "=="  > reqtree.txt