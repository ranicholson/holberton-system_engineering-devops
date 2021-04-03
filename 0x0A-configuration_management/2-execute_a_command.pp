# Using puppet to kill as process

exec { 'pkiller':
    command => 'pkill -f killmenow',
    path => '/usr/bin/:/usr/local/bin/:/bin/',
}