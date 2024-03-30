# Define a custom fact to get the hostname
Facter.add('custom_hostname') do
  setcode 'hostname'
end

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define a custom Nginx config file
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => present,
  content => "server_tokens off;\nadd_header X-Served-By $::custom_hostname;\n",
  notify  => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

