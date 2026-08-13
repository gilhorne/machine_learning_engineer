COMMAND LINE: 

The command line is a text interface for the computer OS.
- Can be used to transverse and edit your computer's filesystem.
- $ :shell prompt
- ls :list
- pwd :print working directory
- cd :change directory
- .. :directory above current working directory
- ../.. :above 2 directories
- mkdir :make directory, creates new directory, directory name as argument
- touch :creates new file within directory
- clear :clears terminal
- echo :prints to terminal
- cat :prints contents of files, file as argument (ex: cat file.txt)
- wc :word count
- history :history of commands entered in current session
- less :displays files in terminal one page at a time (used for larger files)
- glow :formats Markdown content within the terminal

LIST COMMAND OPTIONS: Options modify the behavior of commands

- -a :lists all contents, including hidden files and directories
- -l :(a lowercase “L”) lists all contents of a directory in long format, as well as the file permissions
- -t :orders files and directories by the time they were last modified.
- -alt :lists all contents, including hidden files and directories, in long format, ordered by the date and time they were last modified.

OPTIONS:

- -r : recursive option for deleting directory and child directories
- -i : insensitive case, rewrite the actual file with sed

COPY COMMAND:

- cp: copies files or directories (ex. cp source.txt destination.txt)
    - example: cp source.txt source.bak (.bak file extension is commonly used to notate a file as a backup of a file with the same name)
    - example: cp source.txt directory
    - example: cp source.txt directory/renamed_source.txt (renames the copied file)
    - example: cp directory/source.txt directory
    - example: cp file1.tx file2.tx directory/ (copy multiple files into directory)

WILDCARD COMMAND:

- *: selects groups of files 
    - example: cp * directory/ (copies all files in the current directory into another directory)
    - example: cp *.txt driectory/ (copies just .txt files into another directory)
    - example: cp w*.txt directory/ (copies .txt files in working directory starting with "w", prefix and suffix commands)
    - exmaple: cp * .. (copies to previous directory)
    - example: rm directory/* (deletes all the files in a directory)

MOVE COMMAND:

- mv: moves a file without making a copy
    - use the source file as the first argument and the destination directory as the second argument.
    - example: mv file.txt directory/ (mv file1.txt file2.txt directory/)
    - example: mv file_source.txt file_renamed.txt (renames file)


REMOVE COMMAND:

- rm: deletes files and directories, this is permanent
    - example: rm file.txt (removes file)
    - example: rm -r directory (removes directory with all the child directories using -r (recursive option))

INPUT/OUTPUT REDIRECTION:

- standard input, abbreviated as stdin, is information inputted into the terminal through the keyboard or input device.
- standard output, abbreviated as stdout, is the information outputted after a process is run.
- standard error, abbreviated as stderr, is an error message outputted by a failed process.

- > : redirect command
    - example: echo "Hello" > hello.txt ("Hello" is entered as the standard input, and is then redirected to the file hello.txt by >)
    - the cat command can be used to output contents of the. file to the terminal.
    - example cat file.txt > file2.txt (> takes the standard output of the command on the left, and redirects it to the file on the right)
    
- >> : append command
    - takes the standard output of the command on the left and appends (adds) the content to the file on the right.
    - example: cat file.txt >> file2.txt

- < : takes the standard input from the file on the right and inputs it into the command on the left
    - example: cat < file.txt

- | : pipe command
    - takes the standard output of the command on the left, and pipes it as standard input to the command on the right. You can think of this as “command to command” redirection
    - example: cat file.txt | wc (count the words in file)
    - example: cat file.txt | wc | cat > file2.txt (chain together multiple pipe commands)

- sort : sort
    - takes the standard input and orders it alphabetically for the standard output (it doesn’t change the file itself)
    - example: sort file.txt
    - example: cat file.txt | sort > sorted_file.txt (sorts the oupout of a file into another file)

- uniq : unique
    - filters out adjacent, duplicate lines in a file
    - example: uniq file.txt
    - example: sort file.txt | uniq
    exampple: sort file.txt | uniq > sorted-file.txt (sorts file, then output is filtered into another file)
    
GLOBAL REGULAR EXPRESSION PRINT (GREP)

- grep : searches files for lines that match a pattern and returns the result
- Case sensitive
    - example: grep Text file.txt
    - example: grep -i Text file.txt (-i option allows insensitive case)
    - example: grep -R Text file.txt (-R searches all the files in directory and outputs filename and lines containing the results)
    - grep -Rl Text : searches all files ina directory and outputs only filenames with matched results (no lines)

- sed :stream editor
    - accepts standard input and modifies it based on an expression, before desplaying it as output data
    - example: sed 's/search_text/replacement_text/' file.txt
    - s: substitution. Always used when using sed
    - search_text: the search string, or the text to find
    - replacement_text: the replacement string, or the text to add in place
    - g expression: glabal, this means all instances of search_text on a line will be turned to replacement_text

NANO TERMINAL:

- nano :opens nano terminal
    - follow commands under nano terminal
    - ctrl + O : save
    - nano file.txt : opens file
    - ctrl + X : exit

BASE PROFILE:

- A bash profile is a file used to store environment settings for your terminal. 
On most computer systems, the file is in the home directory and is accessible by the name .bash_profile.

- When you edit the bash profile, you can add commands to execute every time a new terminal session is started.

    - To activate the changes made in .bash_profile for the current session, use the following command: source
    - example: source .bash_profile
- ALIAS COMMAND:
    - One type of setting you can create is called an alias: example: alias pd="pwd"
    - The alias command allows you to create keyboard shortcuts, or aliases, for commonly used commands.
    - There can be as many alias' as neede within .bash_profile

- Environment variables : 
    - variables that can be used across commands and programs and hold information about the environment
    - example: export USER="Name"

    - The line USER="Name" sets the environment variable USER to a name “Name”. Usually the USER variable is set to the name of the computer’s owner.

    - The line export makes the variable available to all child sessions initiated from the session you are in. This is a way to make the variable persist across programs.

    - the command echo $USER returns the value of the variable. Note that $ is always used when returning a variable’s value. Here, the command echo $USER returns the name set for the variable.

    - PS1:
        - environment variable that defines the makeup and style of the command prompt.
        - example: export PS1=">> "
        - export PS1=">> " sets the command prompt variable and exports the variable. Here we change the default command prompt from $ to >>

    - HOME:
        - environment variable that displays the path of the home directory ~
        - specify and change the HOME variable if needed, but in most cases this is not necessary.
        - by typing echo $HOME, the terminal displays the path /home/ccuser as output.

    - PATH:
        - stores a list of directories separated by a colon
        - The PATH variable simply lists which directories contain scripts
        - in advanced cases, you can customize the PATH variable when adding scripts of your own
        - example: echo $PATH
        output:
        /home/ccuser/.gem/ruby/2.0.0/bin:/usr/local/sbin:
        /usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin

    - ENV:
        - env command: stands for “environment,” and returns a list of the environment variables for the current user
        - env | grep VARIABLE :To select the value of a particular environment variable

