# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  mode    => '0644',
  content => "server {\n  listen 80 default_server;\n  listen [::]:80 default_server;\n  root /var/www/html;\n\n  location / {\n    index index.html;\n  }\n\n  location /redirect_me {\n    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n  }\n\n  error_page 404 /404.html;\n  location = /404.html {\n    internal;\n  }\n\n  # Add custom header\n  add_header X-Served-By $hostname;\n}\n",
}

# Create a custom index.html file with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => file,
  mode    => '0644',
  content => "Hello World!\n",
}

# Create a custom 404.html error page
file { '/var/www/html/404.html':
  ensure  => file,
  mode    => '0644',
  content => "Ceci n'est pas une page\n",
}

# Enable the new configuration by creating a symbolic link
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

# Restart Nginx to apply the changes
service { 'nginx':
  ensure => running,
  enable => true,
  require => [
    File['/etc/nginx/sites-enabled/default'],
    File['/var/www/html/index.html'],
    File['/var/www/html/404.html'],
    Package['nginx'],
  ],
}
