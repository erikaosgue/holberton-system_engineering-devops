#!/usr/bin/env ruby


if ARGV.length == 1
    puts ARGV[0].scan(/hb[t]{0,4}n/).join("")
end
