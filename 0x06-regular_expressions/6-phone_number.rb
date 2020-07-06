#!/usr/bin/env ruby


if ARGV.length == 1
    puts ARGV[0].scan(/^\d{10,10}/).join("")
    # puts ARGV[0].scan(/^[0-9]{10,10}/).join("")
end
