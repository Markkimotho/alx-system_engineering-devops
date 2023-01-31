#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method
# Regex that outputs: [SENDER],[RECEIVER],[FLAGS] of the log argument
#     The sender phone number or name (including country code if present)
#     The receiver phone number or name (including country code if present)
#     The flags that were used
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
