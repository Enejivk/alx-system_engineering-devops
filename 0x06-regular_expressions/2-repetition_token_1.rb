#!/usr/bin/env ruby
# A regular expression that is simply matching hbttn
puts ARGV[0].scan(/hb{0,1}tn$/).join
