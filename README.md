This code has a simple echo server with some memory leaks. The server uses some memory intensive native libs too. Using the below tools we should be able detect and fix them
# python-memory-inspect

## Python Memory Profiler
Memory Profiler can be installed from source. The module include C code. see https://pypi.org/project/memory-profiler/

```python
sudo python setup.py install 
```
Above command compiles native code and .so gets installed in /Library/Python/2.7/site-packages in mac. Find out how this work for broadcom tool chain and where in Android Linux File system site-package exist.
```shell
export CC=your-platform-triple-gcc
export LDSHARED="your-platform-triple-ld -shared"
python setup.py build
```


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


## Python Debugger
Python Object graph has to be used along with pdb especially when working with external targets. If the tool is not available pdb can be invoked as a module. This should be available along with standard python distribution, so that you can invoke your app as follows.

```python
python -m pdb your_script.py
```
PDB should be used after setting breakpoints in the code. This can be done by adding the following into your code.

```python
import pdb
..
..

pdb.set_trace()

```
There are several commands to continue or abort the further execution, here are some:

c continue execution
n step to the next line within the same function
s step to the next line in this function or a called function
q quit the debugger/execution

This can be done during debug time too, if you know the code.

```python
pdb> b(reak) [[filename:]lineno | function[, condition]]
```

## Python Object Graph
This is a pure Python tool for analysing Python object Model.https://pypi.org/project/objgraph/. It has a dependency on graphviz but both seems to be pure python modules.

Download the source and

```python
sudo python setup.py install 
```
The egg files should appear in the site-packages. Thats enough for it to work on Mac.

### Usage

Now getting to use objgraph Refer https://mg.pov.lt/objgraph/

Assume that now you have found an area around which you seem to have a high memory usage. Our objective is to identify newly created objects, and if we think they are uncessary check why they are not garbage collected.

What we need to do is

* Identify analysis start point, set break point.
* Initiate GC and mark all previous memory growth
* Run function in doubt
* Break at the end of it, gc and analyse the memory growth.

```python
..
..
Break point start
pdb> import gc
pdb> import objgraph

pdb> gc.collect()
pdb> objgraph.show_growth(limit=3)
pdb>c
..
..
Breakpoint end
pdb> gc.collect()
pdb> objgraph.show_growth(limit=3)

pdb>objgraph.show_chain( objgraph.find_backref_chain( random.choice(objgraph.by_type('MyBigFatObject')),objgraph.is_proper_module),filename='chain.png')
```

To help find how much memory the object is holding a tool is provided in src/python/tool. It computes total memory of all references held by an object. This should give a rough memory usage of the object in question. Note that this is not very accurate but should give us an idea.

```python
..
..
pdb> obj = objgraph.by_type('MyFatObject')
pdb> from objsizer import getsize 
pdb> getsize(obj)
pdb> getsize(obj[0])
```

## Python Native

Check the c folder for a helloworld module which exposes a helloworld c api to Python. Read https://www.tutorialspoint.com/python/python_further_extensions.htm

Memory profiling does not include any memory usage in C layer. Need to find a way to co-relate this memory usage so that optimization effort is spent in the right spot.
