# Install the puppet-lint package
# install_flask.pp

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => '/usr/bin',
  environment => ['LANG=en_US.UTF-8'],
  unless      => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
