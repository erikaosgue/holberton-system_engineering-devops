# using Puppet to make changes to our configuration file

file_line { 'Turn off passwd auth':
  ensure             => present,
  path               => '/etc/ssh/ssh_config',
  match              => '#  PasswordAuthentication yes',
  line               => '   PasswordAuthentication no',
  append_on_no_match => true,
}

file_line { 'Declare identity file':
  ensure             => present,
  path               => '/etc/ssh/ssh_config',
  match              => '   IdentityFile ~/.ssh/holberton',
  line               => '   IdentityFile ~/.ssh/holberton',
  append_on_no_match => true,
}
