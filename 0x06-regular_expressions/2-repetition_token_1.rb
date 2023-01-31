#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method
# Regex that accepts "h-('an optional b')-t-n"
puts ARGV[0].scan(/hb?tn/).join
