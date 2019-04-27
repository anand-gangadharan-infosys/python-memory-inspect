# python-memory-inspect

## Python Memory Profiler
Memory Profiler can be installed from source. The module include C code. see https://pypi.org/project/memory-profiler/

```python
sudo python setup.py install 
```
Above command compiles native code and .so gets installed in /Library/Python/2.7/site-packages in mac. Find out how this work for broadcom tool chain and where in Android Linux File system site-package exist.

Once python has access to memory profiler, the code can be annotated with 

```python

from memory_profiler import profile
..
...

@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a
```

Profiling can be started by launching the app with a switch. Find a way to do that for our launcher.


```python
python -m memory_profiler example.py
```
Time based memory reporting is also possible

```python
mprof run <executable>
mprof plot
```      


## Python Object Graph
This is a pure Python tool for analysing Python object Model.https://pypi.org/project/objgraph/. It has a dependency on graphviz but both seems to be pure python modules.

Download the source and

```python
sudo python setup.py install 
```
The egg files should appear in the site-packages. Thats enough for it to work on Mac.



## Python Native

Check the c folder for a helloworld module which exposes a helloworld c api to Python. Read https://www.tutorialspoint.com/python/python_further_extensions.htm

Memory profiling does not include any memory usage in C layer. Need to find a way to co-relate this memory usage so that optimization effort is spent in the right spot.
