#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method
# Regex that matched a 10-digit phone number
# DESCRIPTION:
#     It can only start with a digit an end with a digit
#     It is restricted to 10 digits
#     It can only contain digits
puts ARGV[0].scan(/^[0-9]{10}$/).join
