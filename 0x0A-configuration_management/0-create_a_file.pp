# Using Puppet, create a file in /tmp/holberton with the requirements.

file { '/tmp/holberton':
  path    => '/tmp/holberton',
  owner   => www-data,
  group   => www-data,
  mode    => '0744',
  content => 'I love Puppet',
}
