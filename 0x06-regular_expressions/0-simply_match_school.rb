#!/usr/bin/env ruby

pattern = /School/

if ARGV.length == 1
  match = ARGV[0].scan(pattern)
  puts match.join('$')
end

