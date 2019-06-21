
"""
Python File Operations

1. Open a File
2. Read or Write
3. Close the file

# Builtin Functions

1. open()

Example : var.read() or var.write()

2. close()

"""

file = open("abc.txt")
print(file.read())
file.close()

"""**********************************************************"""
# Python File Modes:
------------------
Mode	Description
'r'		Open a file for reading. (default)
'w'		Open a file for writing. Creates a new file if it does not
		exist or truncates the file if it exists.
'x'		Open a file for exclusive creation.
                If the file already exists, the operation fails.
'a'		Open for appending at the end of the file
                without truncating it.
		Creates a new file if it does not exist.
't'		Open in text mode. (default)
'b'		Open in binary mode.
'+'		Open a file for updating (reading and writing)
"""**********************************************************"""

"""**********************************************************"""
Python File Methods:
********************

There are various methods available with the file object.
Some of them have been used in above examples.
Here is the complete list of methods in text mode with a brief description.

Python File Methods:
********************
Method		Description
close()		Close an open file. It has no effect if the file is already closed.
detach()	Separate the underlying binary buffer from the TextIOBase and return it.
fileno()	Return an integer number (file descriptor) of the file.
flush()		Flush the write buffer of the file stream.
isatty()	Return True if the file stream is interactive.
read(n)		Read atmost n characters form the file. Reads till end of file if it is negative or None.
readable()	Returns True if the file stream can be read from.
readline(n=-1)	Read and return one line from the file. Reads in at most n bytes if specified.
readlines(n=-1)	Read and return a list of lines from the file. Reads in at most n bytes/characters if specified.
seek(offset,from=SEEK_SET)	Change the file position to offset bytes, in reference to from (start, current, end).
seekable()	Returns True if the file stream supports random access.
tell()		Returns the current file location.
truncate(size=None)	Resize the file stream to size bytes. If size is not specified, resize to current location.
writable()	Returns True if the file stream can be written to.
write(s)	Write string s to the file and return the number of characters written.
writelines(lines)	Write a list of lines to the file.
"""**********************************************************"""
