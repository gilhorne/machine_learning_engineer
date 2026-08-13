- Version Control system.

GIT PROJECT WORKFLOW:
The Git workflow consists of editing files in the working directory, adding files to the staging area, and saving changes to a Git repository.

- A Working Directory: where you’ll be doing all the work: creating, editing, deleting and organizing files

- A Staging Area: where you’ll list changes you make to the working directory

- A Repository: where Git permanently stores those changes as different versions of the project

- Git terminal commands:
    - git init :creates new Git repository

    - git status :inspects the contents of the working directory and staging area

    - git diff :shows the difference between the working directory and the staging area

    - git log :shows a list of all previous commits

    - git commit (-m :adds message to commit) :permanently stores file changes from the staging area in the repository

    - git add :adds files from the working directory to the staging area

    - git clone 

    - git checkout -b var_name

    - git push --set_upstream origin var_name

- HEAD commit:
    - In Git, the commit you are currently on is known as the HEAD commit. 
    - In many cases, the most recently made commit is the HEAD commit.
    - example: git show HEAD
    - git checkout HEAD filename.txt 
        - :restore the file in your working directory to look exactly as it did when you last made a commit.
    - git reset HEAD filename.txt
        - resets the file in the staging area to be the same as the HEAD commit. 
        - It does not discard file changes from the working directory, it just removes them from the staging area.
        - M :short for modification
        - git reset commit_SHA 
            - This command works by using the first 7 characters of the SHA of a previous commit

- STASH:
    - will store your work temporarily for later use in a hidden directory.
    - example: git stash
    - example: git stash

- GIT LOG:
    - git log --oneline :shows the list of commits in one line format
    - git log -S "keyword" :displays a list of commits where the number of occurrences of the keyword changes within at least one file via addition, deletion, or modification
    - git log --graph :displays a visual representation of how the branches and commits were created in order to help you make sense of your repository history
    - the description can be very lengthy, so you can combine the command with --oneline in order to shorten the description

- GIT COMMIT AMEND:
    - git commit --amend :replace the whole previous commit
    - --no-edit :keeps the same commit message when using --amend (example: git commit --amend --no-edit)
    - --reset-author :reset editor of commit

- GIT ALIAS COMMANDS: Examples:
    - git config --global alias.co "checkout"
    - git config --global alias.br "branch"
    - git config --global alias.glop "log --pretty-format:"%h %s" --graph"

- GITHUB:
    - GitHub is both a website and a service that facilitates software development by allowing you to store your code in containers, called repositories, and by tracking changes made to your code.
    - It offers a hosting service and tools to build, test, and deploy code

- GIT CONFIG:
    - git config --global --edit :edits author of commit

- GIT IGNORE:
	- git ignore :	

- SSH KEY SETUP:


