# This is an updated Puppet manifest file (100-puppet_ssh_config.pp)
# that configures the SSH client to use the private key ~/.ssh/school
# and refuse password authentication.

file { '/etc/ssh/ssh_config':
  ensure => present,
  content => "PasswordAuthentication no\nIdentityFile ~/.ssh/school\n",
}

