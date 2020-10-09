# Configuring the User limits
# More Info https://www.ibm.com/support/knowledgecenter/SSGSG7_7.1.3/srv.install/t_srv_startsrv_set_access_ulimit-linux.html

exec {'Change Hard Number Limit Files':
  command => 'sed -i "/holberton hard/s/5/65536/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
exec {'Change Soft Number Limit Files':
  command => 'sed -i "/holberton soft/s/4/65536/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
