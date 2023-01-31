#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method
# Regular expression that matches "h-b-(min of 2 t's, max of 5 t's)-n"
puts ARGV[0].scan(/hbt{2,5}n/).join
