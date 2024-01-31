#!/usr/bin/env ruby
# A regular expression that is simply matching hbttn
puts ARGV[0].scan(/^hbt[1,4]n$/).join
