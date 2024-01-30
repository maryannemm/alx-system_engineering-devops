#!/usr/bin/env ruby

pattern = /^[0-9]{10}$/

if ARGV.length == 1
  match = ARGV[0].scan(pattern)
  puts match.join
end

