exec { 'Add text to /etc/ssh/ssh_config':
  # path    => '/etc/ssh/ssh_config',
  path    => '/bin:/sbin:/usr/bin:/usr/sbin',
  command => 'echo "IdentityFile ~/.ssh/holberton\nPasswordAuthentication no" | sudo tee -a /etc/ssh/ssh_config',
}
