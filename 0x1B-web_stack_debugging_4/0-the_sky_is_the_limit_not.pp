# Puppet manifest to fix Nginx configuration to handle increased load

# Increase buffer size to handle larger responses
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server ipv6only=on;

                root /usr/share/nginx/html;
                index index.html index.htm;

                server_name localhost;

                location / {
                        # First attempt to serve request as file, then
                        # as directory, then fall back to displaying a 404.
                        try_files $uri $uri/ =404;
                        # Increase buffer size
                        fastcgi_buffers 16 16k;
                        fastcgi_buffer_size 32k;
                        # Uncomment the following line if HTTPS is enabled
                        # add_header X-Frame-Options "SAMEORIGIN";
                        # Uncomment the following line if using a larger file size
                        # client_max_body_size 100M;
                }
        }",
  notify  => Exec['reload-nginx'],
}

# Reload Nginx configuration after changes
exec { 'reload-nginx':
  command     => '/usr/sbin/service nginx reload',
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
}

