#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method
# Regex that matches "h-b-(t 0 or as many times)-b" 
puts ARGV[0].scan(/hbt*n/).join
