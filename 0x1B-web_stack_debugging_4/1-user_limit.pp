# Puppet config that changes the soft and hard limits for "holberton" user
exec { 'Change soft limit for holberton user':
  command  => 'sed -i "s/^holberton\ssoft.*/holberton\tsoft\tnofile\t10000/" /etc/security/limits.conf',
  path     => '/usr/bin:/bin',
  provider => shell,
  unless   => 'grep -q "^holberton\ssoft\tnofile\t10000" /etc/security/limits.conf',
}

exec { 'Change hard limit for holberton user':
  command  => 'sed -i "s/^holberton\shard.*/holberton\thard\tnofile\t100000/" /etc/security/limits.conf',
  path     => '/usr/bin:/bin',
  provider => shell,
  unless   => 'grep -q "^holberton\shard\tnofile\t100000" /etc/security/limits.conf',
}
