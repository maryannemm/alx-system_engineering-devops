#!/usr/bin/env ruby

log_file = ARGF.read

log_file.scan(/(?<=\[from:)([^[\]]+)|(?<=\[to:)([^[\]]+)|(?<=\[flags:)([^[\]]+)/) do |sender, receiver, flags|
  puts "#{sender},#{receiver},#{flags}"
end

