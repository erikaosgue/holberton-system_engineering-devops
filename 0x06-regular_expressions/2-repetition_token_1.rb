#!/usr/bin/env ruby


if ARGV.length == 1
    puts ARGV[0].scan(/h[b]{0,1}tn/).join("")
end
