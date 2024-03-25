# 7-puppet_install_nginx_web_server.pp
# This manifest installs and configures Nginx using Puppet.

class web_server {
    package { 'nginx':
        ensure => 'installed',
    }

    file { '/var/www/html/index.html':
        content => 'Hello World!',
    }

    file { '/etc/nginx/sites-available/default':
        content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
",
    }

    service { 'nginx':
        ensure => 'running',
        enable => true,
    }
}

include web_server

