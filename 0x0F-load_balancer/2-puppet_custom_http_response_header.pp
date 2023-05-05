# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Set up a custom Nginx configuration file
file { '/etc/nginx/conf.d/custom.conf':
  content => "location / {
                add_header X-Served-By $hostname;
                root /var/www/html;
                index index.html;
              }",
}

# Restart Nginx service to apply changes
service { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/nginx/conf.d/custom.conf'],
}
