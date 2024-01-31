#!/usr/bin/env ruby
# A regular expression that is simply matching hbttn
puts ARGV[0].scan(/^\d{10}$/).join
