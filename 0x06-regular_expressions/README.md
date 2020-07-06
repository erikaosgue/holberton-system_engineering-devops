
# 0x06. Regular expression

## Background Context
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

    sylvain@ubuntu$ cat example.rb
    #!/usr/bin/env ruby
    puts ARGV[0].scan(/127.0.0.[0-9]/).join
    sylvain@ubuntu$
    sylvain@ubuntu$ ./example.rb 127.0.0.2
    127.0.0.2
    sylvain@ubuntu$ ./example.rb 127.0.0.1
    127.0.0.1
    sylvain@ubuntu$ ./example.rb 127.0.0.a

## Resources

### Read or watch:

* Regular expressions - basics
* Regular expressions - advanced
* Rubular is your best friend
* Use a regular expression against a problem: now you have 2 problems
* Learn Regular Expressions with simple, interactive exercises

## Requirements
### General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
* All your regex must be built for the Oniguruma library

## Tasks

[0. Simply matching Holberton]()
Requirements:

* The regular expression must match Holberton
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

[1. Repetition Token #0]()
Requirements:

* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

[2. Repetition Token #1]()
Requirements:

* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

[3. Repetition Token #2]()
Requirements:

* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

[4. Repetition Token #3]()
Requirements:

* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
[5. Not quite HBTN yet]()

Requirements:

* The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

[6. Call me maybe]()
Requirement:

The regular expression must match a 10 digit phone number
