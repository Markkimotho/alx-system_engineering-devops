# Puppet file that fixes a bug in an apache2 server
exec { 'Rename the file correctly':
  command => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin'],
  user    => 'root',
}
