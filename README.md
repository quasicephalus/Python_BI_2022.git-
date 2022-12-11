### Command line tools python implementation
Every tool present as `.py` script with the name corresponding to bash analog.
Usage: in command line:
```
$ ./[script_name].py [arguments]
```
There is pipeline support for all scripts where pipe is usable, for example:
```
$ echo word3 >> file
$ echo word2 >> file
$ echo word1 >> file
$ ./cat.py file | ./sort.py | ./wc.py -lwc
> 3 3 18
```
1. `wc.py` with flags `-l -w -c` - count lines, words and bytes in file(s) or `stdin`
Usage: `$ ./wc.py [-l -w -c] [file(s)]`
`-l` - lines. Counts only lines.
`-w` - words. Counts words
`-c` - bytes. Counts bytes
All three is "on" by default, as if script started with `-lwc`.
If there is no `file`, input is `stdin`. Pipe input supported.
Example:
```
$ echo word3 >> file1
$ echo word2 >> file1
$ echo word1 >> file1
$ echo word3 >> file2
$ echo word4 >> file2
$ echo word5 >> file2
$ ./wc.py -lw file1 file2
3 3 file1
3 3 file2
6 6 total
```
2. `ls.py` with flag `-a` - list items in directory.
Usage: `$ ./ls.py [-a] [path]`
If no path provided, default is cwd. Could be multiple pahtes. Pipe suported. 
`-a` - all. Do not hide items that start with ".".
Example:
```
$ mkdir 1
$ mkdir 2
$ touch 1/file1
$ touch 1/.file2
$ touch 2/file3
$ touch 2/.file4
$. /ls.py 1 2 -a
1: 
. .. file1 .file2
2:
. .. file3 .file4
$ ./ls.py 1 2 
1:
file1
2:
file3
```
3. `sort.py` - sort file(s) or `stdin`
Usage:  `$ ./sort.py [file(s)]`
If no files provided, reads `stdin`. If multiple files, sorts them concatenated. Pipe supported.
Example:
```
$ ./sort.py file1 file2 # files created in `wc.py` example
word1
word2
word3
word3
word4
word5
```
4. `rm.py` with flag `-r` - remove files or directories
`-r` - recursive - allows to remove directory
Usage: `$ ./rm.py [-r] [file(s)]`
Example:
```
$ ./ls.py
file ls.py rm.py
$ ./rm.py file
$ ./ls.py
lr.py rm.py
```
5. `cat.py` - write file(s) or `stdin` in `stdout`.
Usage: `$ ./cat.py [file(s)]`. If multiple files, they passed concatenated. If no files, reads `stdin`.
Example: 
```
$. ./cat.py file1 file2
word3
word2
word1
word3
word4
word5
```
6. `tail.py` with flag `-n` - write file(s) or `stdin` in `stdout`.
Usage: `$ ./tail.py [-n N] [file(s)]`. If multiple files, they passed concatenated. If no files, reads `stdin`. Pipe supported.
`-n` is an integer number, default N is 10.
Example: 
```
$. ./tail.py  -n 1 file1 file2 #same two files
==> file1 <==
word1

==> file2 <==
word5
```
7. `mkdir.py` with flag `-p` - make a directoy (can be multiple) is it doesn't exist.
Usage: `$ ./mkdir.py [-p] [path(s)]`.
`-p` - no error if existing, make parent directories as needed
Example:
```
$ ./ls.py
ls.py mkdir.py
$ ./mkdir.py dir
$ ./ls.py
dir lrs.py mkdir.py
```
8. `cp.py` with flag `-r` - copy source file(s) into destination directory
`-r` - recursive - allows to copy directory
`source` - source files to copy
`destination` - where to copy
Usage: `$ ./cp.py [-r] [source(s)]  [destination]`
Example:
```
$ ./ls.py somedir
file1 file2
$ ./cp.py -r file3 file4 otherdir somedir
$ ./ls.py somedir
file1 file2 file3 file4 otherdir
```
9.  `mv.py` - move source to directory (destination) or rename source as destination
`source` - source files or empty directories to move
`destination` - where to move or how to rename
Usage: `$ ./mv.py [-r] [source(s)]  [destination]`
Example:
```
$ ./ls.py somedir
file1 file2
$ ./mv.py file3 file4 somedir
$ ./ls.py somedir
file1 file2 file3 file4
```
