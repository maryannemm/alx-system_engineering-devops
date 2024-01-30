#!/usr/bin/env ruby

pattern = /hb?tn/

if ARGV.length == 1
  match = ARGV[0].scan(pattern)
  puts match.join
end

