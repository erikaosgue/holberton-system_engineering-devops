# create a manifest that kills a process named killmenow

exec { 'killmenow':
  path    => '/bin:/sbin:/usr/bin:/usr/sbin',
  command => 'pkill killmenow',
}
