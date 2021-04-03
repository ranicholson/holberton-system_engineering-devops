# Using puppet to create a file

file { 'holberton':
    ensure  => 'present',
    path    => '/tmp/holberton',
    mode    => '0744',
    group   => 'www-data',
    owner   => 'www-data',
    content => 'I love Puppet'
}
