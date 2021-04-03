# Using puppet to kill as process

exec { 'pkill killmenow':
    path => '/usr/bin/:/usr/local/bin/:/bin/',
}