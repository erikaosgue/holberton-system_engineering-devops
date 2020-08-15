# Add a custom HTTP header with Puppet manifest:

exec { 'update':
    command => '/usr/bin/env apt-get -y update'
}
package { 'nginx':
    ensure => 'installed',
}
file { '/var/www/html/index.html' :
    content => 'Holberton School!',
}
file_line { 'add header':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    line   => "\tadd_header X-Served-By ${hostname};",
    after  => 'listen [::]:80 default_server;',
}
exec { 'service nginx restart':
    command => '/usr/sbin/service nginx restart',
}
