#!/usr/bin/env ruby

pattern = /hbt{2,5}n/

if ARGV.length == 1
  match = ARGV[0].scan(pattern)
  puts match.join
end

