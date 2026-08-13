# CONCURRENT PROGRAMMING:

- Sequential Programming:
	- process that follow a set order of instructions.

- Concurrent Programming:
	- process in which we have multiple tasks running 
	and completing during overlapping periods of time.

	- library: threading


- Parallel Programming:
	- process in which we simultaneously have multiple tasks or separate parts
	of the same task running using multiple CPUs (core processing units)

	- library: multiprocessing


- Asynchronous Programming:
	- process in which tasks are queued and handled in unspecified order.
	
	- library: asyncio


## PROCESSES

- A process is an abstraction representing the program when it is running.
- A process is created when a program is executed.
- processes generally operate independtly and do not share data.
- processes are central to usability of a computer and operating system development


![Process Lifecycle](images/process_lifecycle.png)
* Diagram of process lifecycle *

- Processes are put into one of five states:

	- New :the program has been started and waits to be added into memory
	in order to become a full proces.

	- Ready :process fully initialized, loaded into memory, and waiting to
	be picked up by the processor.

	- Running :currently being executed by the processor.

	- Blocked :the process requires a contested resource that it must wait for.

	- Finished :the process has been completed.


## Process Layout / Process Control Block:

- When a process is initialized, its layout within memory has four distinct sections:

	- Text section for the compiled code
	
	- data section for initialized variables

	- stack for local variables defined within functions

	- heap for dynamic memory allocation

- Processes are also initialized within a Process Control Block

- Process Control Block is required by the operating system for managing
the process :

	- Unique process ID, and ID of any parent processes that launched
	the current one

	- current process state

	- Time process has been running, time limits process may have

	- allowed system resources and permissions

	- priority of the process

	- program counter for the address of the instruction currently being executed

	- address of other registers within the CPU holding intermediate values

	- information required for memory management (page and segment tables)

- When one process launches another, the original enters a parent-child relationship
with the newly-launched process that shares much of the above data.

- Example:
	- when an existing music player process starts a new process for scanning the user’s music library, 
both of these processes generally share the same system resources and permissions.
 
	- Parent processes usually also wait for their children to complete before terminating themselves, 
unless the child was created specifically to run independently in the background.

![Process Layout](images/process_layout_control_block.png)


- A process is an abstract data structure that represents all of the necessary
information to run a program. 

## Threads

- Thread represents the actual sequence of processor instructions that are actively
being executed. 

- process contains at least one thread to be executed.
(more can be created to allow for concurrent processing if supported by CPU)

- threads live within the process and shares all common resources:
(memory pages, active files)

- by sharing data directly, communication and context switching between threads are
faster. While taking fewer system resources.

![Threads](images/process_thread.png)

### Multithreading:

- parallelizing computations benefits:
	improved system utilization and responsiveness

- Tasks can be more evenly split between multiple threads
- all computing resources are exhuasted
- allowing longer tasks to run in the background, seperate from user input

![Multithreading](images/process_multithreading.png)

---

- data races : where multiple threads attempt to modify the same piece of data.

- deadlocks : where multiple threads all attempt to wair for each other and
freeze the system.

- non-deterministic programs are untestable

- bugs are usually related to tight timing CPU interactions. 

### Kernal Threads / User Threads:

- Threads can behave differently depending on the environment they're created in.

	- kernel thread: built within existing process.
	:: means that the kernel within the operating system is fully aware of
	theae threads and directly manages their execution.

	- user thread: exist solely in userspace.
	:: identical functionality, is not known or controlled by the kernel

	- user threads are more efficient that kernel threads, they operate
	independently od the kernel.

	- user threads do not need to be mapped to existing kernel threads in
	order to have the operating system execute them.

- 3 Common Models : For mapping user threads to kernel threads

	- 1:1 Kernel-level Threading: Simple implementation that best allows for
	hardware accerleration provided by the kernal threads.

	- N:1 User-level Threading: For ultra-light threads that can quickly
	communicate and context switch.
		- does not benefit from hardware acceleration due to sharing
		the same kernel thread.

	- M:N Hybrid Threading: To get best of both solutions;
		- very-light and fast threads that can be hardware accelerated 
		- complex-implementation can lead to bugs; ie - priority inversion:
		- less important tasks are mistakenly prioritized and run first

![Thread Model](images/process_thread_models.png)

## KEY NOTES:

- Process : processess exist in five ststes that are leverged to allow th CPU cores
to alternate between ready ans blocked processes to best take advantage of limited 
computing resources.

- Thread : represents the actual sequence of processor instructions that are actively
being executed. 

	- each process contains at least one thread.

	- can contain structures that share resources among each other to allow
	for faster communication and context-switching.

	- lighter, require fewer system resources.

	- multithreading individual cores further impoves system utilization and
	responsivness by efficiently spltting tasks.


## CONCURRENT PROGRAMMING (Python Modules)

- threading

- asyncio

- multithreading

---

## Threading Module:

> **Threading Module**

```python
import threading
example_thread = threading.Thread(target = function1, args =(arg1,..))
```

- target : function to execute with thread(s), Default is `None`

- args : argument or set of arguments applied to the target function,
It's a tuple, and defaults to `None`


**Example**

- to apply thread to a function called `analyzed_list()`, 
using arguments `l1, l2, l3` 

```python
t = threading.Thread(target = analyzed_list(), args = (l1, l2, l3))

t.start() #starts thread to execute on run.
```

---

- Multiple Threading (Method 1)
```python
t1 = threading.Thread(target=target_function, args=(arg1,))

t2 = threading.Thread(target=target_function, args=(arg2,))

t3 = threading.Thread(target=target_function, args=(arg3,))

t1.start()
t2.start()
t3.start()
```

---

- Multiple Threading (Method 2)
```python
threads=[]
args = [arg1, arg2, arg3]

for i in range(len(args)):
	t = threading.Thread(target=target_function, args=(args[i],))
	threads.append(t)
	t.start()
```

---







