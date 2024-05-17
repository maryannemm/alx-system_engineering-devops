# Puppet manifest to fix Nginx configuration to handle increased load

# Fixing the number of failed requests to get to 0
exec { 'fix--for-nginx':
  command => "sed -i 's/15/4096/' /etc/default/nginx; sudo service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}

