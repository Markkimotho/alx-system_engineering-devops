# Puppet file that configures nginx to handle multiple requests and restarts it when notified
file { '/etc/default/nginx':
  content      => 'ULIMIT="-n 4096"',
  notify       => Service['nginx'],
  refreshonly  => true,
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
