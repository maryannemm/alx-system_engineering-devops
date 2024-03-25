# 1-install_a_package.pp

# Description: Install Flask using pip3 with version 2.1.0
# Package name: Flask
# Version: 2.1.0

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

