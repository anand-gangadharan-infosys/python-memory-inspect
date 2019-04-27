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
This is a pure Python tool for analysing Python object Model.https://mg.pov.lt/objgraph/ . It can be installed using pip

```python
pip install objgraph
```


## Python Native
