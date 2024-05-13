# Puppet manifest to adjust file limits for the holberton user

# Change OS configuration for holberton user
exec { 'change-os-configuration-for-holberton-user':
  command => '/bin/sed -i "s/^\(session\s\+required\s\+pam_limits\.so\)/#\1/" /etc/pam.d/su',
  onlyif  => '/bin/grep -q "^session\s\+required\s\+pam_limits\.so" /etc/pam.d/su',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Apply changes to PAM configuration
exec { 'apply-pam-changes':
  command     => '/bin/bash -c "echo -e \"holberton\t-\tnofile\t65536\" >> /etc/security/limits.conf"',
  unless      => '/bin/grep -q "^holberton\s\+-\s+nofile\s+65536" /etc/security/limits.conf',
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  notify      => Exec['reload-pam'],
}

# Reload PAM configuration
exec { 'reload-pam':
  command     => '/sbin/sysctl -p',
  refreshonly => true,
}

