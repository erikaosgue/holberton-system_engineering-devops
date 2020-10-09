# Add sof limit of files
exec {'add a Soft':
  command => 'bash -c "echo nginx       soft    nofile  30000" >> /etc/security/limits.conf',
  path    => '/bin',
}
# Add hard limit of files
exec {'add a Hard':
  command => 'bash -c "echo nginx       hard    nofile  50000" >> /etc/security/limits.conf',
  path    => '/bin',
}

# Comment the ULIMIT line
exec { 'comment Ulimit':
  command => 'sed -i s/ULIMIT/#ULIMIT/ /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}
# Restart Nginx
exec {'Restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
