# Puppet manifest to adjust file limits for the holberton user

exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }

