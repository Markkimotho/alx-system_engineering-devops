# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;
                root /var/www/html;
                index index.html;

                location / {
                    return 200 'Hello World!';
                }

                location /redirect_me {
                    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
                }
              }",
  notify  => Service['nginx'],
}

# Create index.html file with 'Hello World!' message
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!",
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
}
