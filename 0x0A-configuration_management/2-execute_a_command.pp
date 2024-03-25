# 2-execute_a_command.pp

# Description: Execute a command to kill a process named "killmenow"
# Command: pkill -f killmenow

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/bin',
}

