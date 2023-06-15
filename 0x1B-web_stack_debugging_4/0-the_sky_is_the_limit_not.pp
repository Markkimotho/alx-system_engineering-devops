file { '/etc/default/nginx':
  content => 'ULIMIT="-n 4096"',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/default/nginx'],
}
