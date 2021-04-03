# Using puppet to kill as process


exec { 'pkill killmenow':
    command => 'pkill killmenow',
}
