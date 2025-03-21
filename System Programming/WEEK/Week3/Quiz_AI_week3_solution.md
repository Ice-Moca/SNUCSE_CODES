# 2025 Spring SNU System Programming - Weekly Quiz (Week 3, with Solutions)

We have prepared some light quizzes related to class content of week 3.  
These problems have been selected from those generated by **AI tool (Cramify)**,  
based on your class ppt content.

There is no need to submit anything after reviewing this material,  
but we hope it will help you review the class content you learned this week and prepare for the quiz.

---

Weekly Quiz has two documents, one with only the problems and  
the other with both the problems and solutions.  

# Question 1

Unix-like systems follow the "everything is a file" philosophy.  
Which of the following examples satisfy this philosophy?

A) A program writes data to a log file to record events.  
B) A programmer reads data from a file stored on a hard disk.  
C) A user creates a new text file to store a document.  
D) A system administrator configures network settings by modifying a file representing a network interface.  

**Answer: A, B, C, D (all of the above)**

**Solution:**  
A key principle of Unix-like systems is that everything — ranging from log files, regular disk files, text documents, to network interfaces — is handled as though it were a file.  
The above scenarios all illustrate this concept by showing how various resources or actions in the system can be managed and accessed through file operations (reading and writing).

# Question 2

Given the commands and outputs related to file linking in a Unix-like file system, analyze the following statements about hard links and soft links.  
Indicate True or False for each statement.

- a) A hard link creates a new file with identical content to the original file, effectively resulting in two separate files with the same data.

**Answer: False**

**Solution:**  
A hard link does not create a new file with separate content.  
Instead, it creates another directory entry pointing to the same inode as the original file.  
Both directory entries refer to the same data blocks on the storage device; there are not two copies of the file's content.

- b) Deleting a file that has multiple hard links removes the file's content from the storage device only when all hard links pointing to that file are deleted.

**Answer: True**

**Solution:**  
Each hard link increments the link count associated with the inode.  
The file's content, stored in data blocks, is only deleted when the link count reaches zero, meaning no directory entries refer to that inode.

- c) Modifying a file through one hard link is reflected in all other hard links pointing to the same file, as they all share the same underlying data.

**Answer: True**

**Solution:**  
Since all hard links point to the same inode and thus the same data blocks, any changes made through one hard link are immediately visible through all other hard links.

- d) A soft link, also known as a symbolic link, stores a copy of the target file's data, ensuring that even if the original file is deleted, the soft link still retains the data.

**Answer: False**

**Solution:**  
A soft link only stores a pointer to the target file's pathname, not the actual file data.  
If the original file is deleted, the soft link becomes a "dangling" or broken link, pointing to a non-existent file.

- e) Soft links can point to files across different file systems or even different storage devices, while hard links are restricted to the same file system as the original file.

**Answer: True**

**Solution:**  
Soft links store the pathname of the target file, allowing them to reference files across different file systems.  
Hard links, however, directly point to an inode, which is a file system-specific structure, restricting them to the same file system.

# Question 3

A file named "report.pdf" has the permissions set as `-rwxr-x---`. The owner is "john", and the group is "finance".  
Which of the following actions can "lisa", a member of the "marketing" group, perform on this file?

A) Lisa can read and execute the file.  
B) Lisa cannot perform any actions on the file.  
C) Lisa can read the file but not execute it.  
D) Lisa can execute the file but not read it.

**Answer: B**  

**Solution:**  
The permission string `-rwxr-x---` breaks down as follows:
- `-`: Represents a regular file.
- `rwx`: The owner ("john") has read, write, and execute permissions.
- `r-x`: Members of the group "finance" have read and execute permissions, but not write permissions.
- `---`: All others (including "lisa" who is not in the "finance" group) have no permissions.
Therefore, "lisa" cannot perform any actions on the file.

# Question 4

Given the following statements concerning file system security in a Unix-like environment, indicate True or False for each statement.

- a) A world-writable directory with execute permission allows any user on the system to execute files placed within that directory, posing a significant security risk if exploited by malicious actors.

**Answer: True**

**Solution:**  
World-writable execute permissions mean any user can add and run a file in the directory, creating a vulnerability for malicious code execution.

- b) The sticky bit, when set on a directory, restricts file deletion within that directory to only the file owner and the directory owner, regardless of other users' permissions.

**Answer: True**

**Solution:**  
The sticky bit prevents users who aren't the file owner or directory owner from deleting or renaming files within the directory, even if they have write permissions on the directory itself.

- c) The SUID (Set User ID) bit permits a program to execute with the file owner's permissions, while the SGID (Set Group ID) bit allows execution with the group's permissions, potentially enabling access to resources beyond the executing user's normal privileges.

**Answer: True**

**Solution:**  
SUID allows a program to run with the owner's permissions, and SGID with the group's permissions, potentially granting access beyond the user's usual rights.

- d) Setting the sticky bit on a file prevents its execution even if the execute permission is granted for the owner, group, or others.

**Answer: False**

**Solution:**  
The sticky bit applies only to directories, not files.  
It affects file deletion and renaming within the directory, not execution permissions.

- e) If a file system has the NOSUID option enabled, the SUID and SGID bits on files within that file system are ignored, mitigating the security risks associated with privilege escalation.

**Answer: True**

**Solution:**  
The NOSUID option disables the effect of the SUID and SGID bits, preventing programs from inheriting the owner or group's permissions upon execution.

# Question 5

In a Unix-like operating system, a process is attempting to write data to a file.  
Describe the role of file descriptors in this process, explaining how they are obtained, what they represent, and how they are used by system calls like write() to interact with the file.  
Furthermore, explain what happens if the process attempts to write to a file descriptor that has already been closed.

**Answer:**  
File descriptors are abstract handles obtained via system calls such as `open()`.  
They represent open files within a process, acting as indices into a per-process file descriptor table.  
System calls like `write()` use these descriptors to locate the appropriate file and perform operations on it.  
If a process attempts to write to a file descriptor that has been closed, the `write()` system call fails.

**Solution:**  
1. Obtaining a File Descriptor:  
A process obtains a file descriptor by calling the `open()` system call with parameters such as the file path and the desired access mode (for example, read, write, or append).  
When the call is successful, a non-negative integer is returned, which serves as the file descriptor.
2. Representation:  
The file descriptor is an abstract value that represents an open file in the context of the process.  
It functions as an index into the process’s file descriptor table, a data structure maintained by the kernel that stores information about each open file (such as the current file offset).
3. Use by System Calls:  
When a system call like `write()` is made, the file descriptor is used by the kernel to find the corresponding entry in the file descriptor table.  
The kernel then accesses the file associated with that entry and performs the write operation starting from the current file offset, updating it accordingly.
4. Writing to a Closed File Descriptor:  
If the process attempts to write to a file descriptor that has already been closed, the `write()` operation fails, indicating that the descriptor is no longer valid.

# Question 6

A program opens a file named "data.txt" for writing, appending data to it if it exists.  
If an error occurs during the open operation, the program should exit.  
Which code snippet correctly implements this behavior?

A)
```c
int fd = open("data.txt", O_WRONLY | O_CREAT | O_APPEND, S_IRUSR | S_IWUSR);
if (fd < 0) {
  perror("open");
  exit(EXIT_FAILURE);
}  
```
B)
```c
FILE *fp = fopen("data.txt", "w");
if (fp == NULL) {
  perror("fopen");
  exit(EXIT_FAILURE);
}
```
C)
```c
int fd = open("data.txt", O_RDONLY | O_CREAT, S_IRUSR | S_IWUSR);
if (fd < 0) {
  perror("open");
  exit(EXIT_FAILURE);
}
```
D)
```c
int fd = creat("data.txt", O_WRONLY | O_APPEND);
if (fd < 0) {
  perror("creat");
  exit(EXIT_FAILURE);
}
```

**Answer: A**  

**Solution:**  
The correct approach involves using the open system call with appropriate flags.  
The `O_WRONLY` flag specifies write-only access.  
`O_CREAT` tells open to create the file if it doesn't exist, and `O_APPEND` ensures data is appended to the end of the file.  
A mode must be provided when `O_CREAT` is used, such as `S_IRUSR | S_IWUSR` to grant read and write permissions to the owner.  
The return value of open should be checked for errors (a negative value indicates an error).

# Question 7

| Feature | Unix I/O | Standard I/O |
|-------|-------|-------|
| Buffering	| No | Yes (fully buffered, line buffered, unbuffered) |
| Efficiency | High (direct system calls) |	Higher for character/line operations due to buffering|
| Complexity | More complex, requires handling short counts | Simpler interface, automatic short count handling |
| Async-signal safety	| Yes	| No |
| File Metadata Access | Yes | No |
| Suitability	| Signal handlers, network sockets, high-performance needs | Disk/terminal files, general programming tasks |

Consider the table above comparing Unix I/O and Standard I/O.  
A programmer is developing a real-time application that needs to log error messages to a file immediately, even during signal handling.  
Which I/O approach is more suitable for this scenario, and why?  
Explain the key factors influencing this choice, referencing specific features from the table.

**Answer:**  
Unix I/O is more suitable due to its async-signal safety, which is crucial for writing to files within signal handlers.  
Standard I/O lacks this safety feature.

**Solution:**  
Unix I/O is more suitable for this scenario.  
The critical factor here is async-signal safety.  
As the table shows, Unix I/O functions are async-signal-safe, meaning they can be safely called within signal handlers.  
Standard I/O functions are not async-signal-safe.  
Since the application needs to log errors during signal handling, using Standard I/O could lead to unpredictable behavior or crashes.  
The immediate logging requirement also aligns with Unix I/O's unbuffered nature, ensuring data is written to the file without delay.

# Question 8

Explain the differences between fully buffered, line buffered, and unbuffered I/O in Standard I/O.  
Describe a scenario where each type would be most appropriate and explain how each impacts the frequency of system calls.

**Answer:**  
Fully buffered I/O is best for large file operations, minimizing system calls by buffering data until the buffer is full.  
Line buffered I/O, suitable for interactive applications, buffers data until a newline or full buffer, allowing line-by-line output.  
Unbuffered I/O writes data immediately, ideal for time-sensitive information like error logging.

**Solution:**  
- Fully Buffered:  
Data is accumulated in a buffer and written to the file only when the buffer is full.  
This minimizes system calls, making it efficient for large file operations.  
A scenario where this is appropriate is writing large amounts of data to a disk file.  
- Line Buffered:  
Data is buffered until a newline character is encountered or the buffer is full, at which point it's written.  
This is suitable for interactive applications where output needs to be displayed line by line.  
A common scenario is writing to a terminal.  
- Unbuffered:  
Data is written to the file immediately without buffering.  
This is useful for logging errors or other time-sensitive information where immediate output is crucial.  
A common scenario is writing to stderr.

# Question 9

A program needs to write a large volume of data to a file.  
Explain how using Standard I/O's `fwrite()` improves performance compared to directly using Unix I/O's `write()` system call, and describe the interaction between the two.

A) `fwrite()` uses a separate, faster system call than `write()` for file operations, leading to improved performance.  
B) Standard I/O and Unix I/O operate independently; `fwrite()`'s performance advantage comes from its optimized implementation in user space, not its interaction with `write()`.  
C) `fwrite()` bypasses the kernel and writes directly to the hard drive, making it faster than `write()`.  
D) Standard I/O's `fwrite()` buffers data, reducing the number of expensive `write()` system calls made by Unix I/O, thus improving performance for large file writes.

**Answer: D**  

**Solution:**  
Standard I/O's `fwrite()` uses buffering.  
Instead of writing each piece of data directly to the file with a `write()` system call (which is expensive), `fwrite()` stores data in a buffer.  
When the buffer is full, Standard I/O performs a single `write()` call to write the entire buffer's contents to the file at once.  
This reduces the number of system calls, significantly improving performance, especially for large writes.  
Standard I/O functions like `fwrite()` ultimately rely on Unix I/O system calls like `write()` for file access, but they add a buffering layer to enhance efficiency.

