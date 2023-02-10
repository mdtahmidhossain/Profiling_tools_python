### cProfile
cProfile is a built-in profiler in Python that provides statistical profiling information for Python code. For example, if you want to profile the my_function function, you would run the following code:
```python
import cProfile
cProfile.run('my_function()', sort='time')

```
Or
```shell
python -m cProfile -s tottime coin_change.py
python -m cProfile -o prof.out coin_change.py
```
#### To plot with KCacheGrind
KCachegrind is a Graphical User Interface (GUI) useful to analyze the profiling output emitted by cProfile.

Convert the output file with pyprof2calltree and launch KCachegrind:

```shell
pyprof2calltree -i prof.out -o prof.calltree
kcachegrind prof.calltree # or qcachegrind prof.calltree
```
### perf
perf is a performance analysis tool for Python programs. It helps in profiling the performance of Python code, including the time it takes to run each function and how often each function is called.
```shell
pip install perf
```
To use **perf**, you can use the perf module in your Python code. For example, to profile a specific function, you can wrap the function with the **perf.perf_counter()** method:

```python
import perf

def my_function():
    # Your code here

if __name__ == "__main__":
    perf_counter = perf.perf_counter()
    perf_counter.start()
    my_function()
    perf_counter.stop()
    perf_counter.print_stats()

```
You can also run perf from the terminal using the **python -m perf **command. For example:
```shell
python -m perf timeit my_script.py
```
```shell
python -m perf timeit --setup 'from simul import benchmark' 'benchmark()
```
The **python -m perf timeit** command measures the execution time of a Python script or command using the **perf** module. The **--setup** argument allows you to specify a setup string that will be executed prior to the command you want to time. In this case, the setup string '**from simul import benchmark**' is importing the **benchmark** function from the **simul** module. Finally, the command **'benchmark()'** specifies the function you want to time. So the full command will time the execution of the **benchmark** function from the **simul** module.
### line_profiler

line_profiler is a tool that provides line-by-line profiling information for Python code. To use line_profiler, you need to install it using pip. For example, if you want to profile the my_function function, you would run the following code:
```python
import line_profiler

def my_function():
    # Your code here
    
lp = line_profiler.LineProfiler()
lp.add_function(my_function)
lp.run("my_function()")
lp.print_stats()

```
Or
```shell
kernprof -l -v coin_change.py
```
### memory_profiler
memory_profiler is a Python package that provides memory profiling for Python code. To use memory_profiler, you need to install it using pip. For example, if you want to profile the my_function function, you would run the following code:
```python
import memory_profiler

@profile
def my_function():
    # Your code here
    
my_function()

```
Or
```shell
pip install memory_profiler
mprof run coin_change.py
mprof plot
```
### dis module
The dis module in Python is a tool that can be used to disassemble (i.e., convert into assembly-like code) Python bytecode, which is the compiled representation of Python code. This can be useful for understanding how Python code is executed and how the Python interpreter works.

The dis module provides a function called dis() that can be used to disassemble a single Python function or a whole module. The disassembled code is presented in a form that resembles assembly code, making it easier to understand how the code is executed.

For example, the following code uses the dis module to disassemble the my_function function:
```python
import dis

def my_function():
    a = 1
    b = 2
    c = a + b
    return c

dis.dis(my_function)

```
This will output the disassembled code for the my_function function:
      2           0 LOAD_CONST               1 (1)
                  2 STORE_FAST               0 (a)
    
      3           4 LOAD_CONST               2 (2)
                  6 STORE_FAST               1 (b)
    
      4           8 LOAD_FAST                0 (a)
                 10 LOAD_FAST                1 (b)
                 12 BINARY_ADD
                 14 STORE_FAST               2 (c)
    
      5          16 LOAD_FAST                2 (c)
                 18 RETURN_VALUE
    

In summary, the dis module in Python is a tool for disassembling Python bytecode, which can be useful for understanding how Python code is executed and how the interpreter works. The dis module provides the dis() function, which can be used to disassemble a single function or a whole module.
