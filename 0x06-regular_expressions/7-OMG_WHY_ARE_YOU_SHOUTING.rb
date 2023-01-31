#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method
# Regex that only matches capital letters OR
# picks out the capital letters from a string.
puts ARGV[0].scan(/[A-Z]/).join
