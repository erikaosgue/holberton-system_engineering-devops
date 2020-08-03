# 0x0A Configuration management

## Resources
### Read or watch:

    Intro to Configuration Management
    Puppet resource type: file (check “Resource types” for all manifest types in the left menu)
    Puppet’s Declarative Language: Modeling Instead of Scripting
    Puppet lint
    Puppet emacs mode

## Requirements
### General
    All your files will be interpreted on Ubuntu 14.04 LTS
    All your files should end with a new line
    A README.md file at the root of the folder of the project is mandatory
    Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
    Your Puppet manifests must run without error
    Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
    Your Puppet manifests files must end with the extension .pp
    Note on Versioning
    Your Ubuntu 14.04 VM should have Puppet 3.4 preinstalled.


## Install puppet-lint

    $ apt-get install -y ruby
    $ gem install puppet-lint -v 2.1.1

## Tasks

[0. Create a file mandatory](https://github.com/erikaosgue/holberton-system_engineering-devops/blob/master/0x0A-configuration_management/0-create_a_file.pp)

Using Puppet, create a file in /tmp.

Requirements:

    File path is /tmp/holberton
    File permission is 0744
    File owner is www-data
    File group is www-data
    File contains I love Puppet

[1. Install a package mandatory](https://github.com/erikaosgue/holberton-system_engineering-devops/blob/master/0x0A-configuration_management/1-install_a_package.pp)

Using Puppet, install puppet-lint.

Requirements:

    Install puppet-lint
    Version must be 2.1.1
    
Example:

    root@d391259bf577:/# puppet apply 1-install_a_package.pp
    Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.10 seconds
    Notice: /Stage[main]/Main/Package[puppet-lint]/ensure: created
    Notice: Finished catalog run in 2.83 seconds
    root@d391259bf577:/# gem list

    *** LOCAL GEMS ***

    puppet-lint (2.1.1)
    root@d391259bf577:/#


[2. Execute a command mandatory](https://github.com/erikaosgue/holberton-system_engineering-devops/blob/master/0x0A-configuration_management/2-execute_a_command.pp)

Using Puppet, create a manifest that kills a process named killmenow.

Requirements:

    Must use the exec Puppet resource
    Must use pkill
Example:

    Terminal #0 - starting my process

    root@d391259bf577:/# cat killmenow
    #!/bin/bash
    while [[ true ]]
    do
        sleep 2
    done

    root@d391259bf577:/# ./killmenow
    Terminal #1 - executing my manifest

    root@d391259bf577:/# puppet apply 2-execute_a_command.pp
    Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
    Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
    Notice: Finished catalog run in 0.10 seconds
    root@d391259bf577:/# 
    Terminal #0 - process has been terminated

    root@d391259bf577:/# ./killmenow
    Terminated
    root@d391259bf577:/#
