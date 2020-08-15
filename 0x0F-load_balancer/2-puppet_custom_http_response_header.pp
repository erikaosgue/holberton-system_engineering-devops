# Add a custom HTTP header with Puppet manifest:

exec { '/usr/bin/env apt-get update -y':
}
package { 'nginx':
    ensure => installed,
}
file { '/var/www/html/index.html':
    content => 'Holberton School!',
}
file_line { 'add header':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    line   => '\tadd_header X-Served-By $HOSTNAME;',
    after  => 'listen [::]:80 default_server;',
}
service { 'nginx':
    ensure => running,
}
