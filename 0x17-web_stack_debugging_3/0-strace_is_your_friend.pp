# Fix error server 500 for wordpress, having bad extension <phpp> to <php> in <wp-settings.php> file
exec { 'fix-wordpress':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/bin:/sbin:/bin:/usr/sbin'
}
