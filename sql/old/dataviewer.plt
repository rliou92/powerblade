set terminal postscript enhanced eps solid color font "Helvetica,14" size 3.25in,2.3in
set output "temp.eps"

set xlabel "Timestamp" offset 0,-4
set ylabel "Power (W)"

#set yrange [-2:]

set datafile separator "\t"
set timefmt "%Y-%m-%d %H:%M:%S"
set xdata time

set format x "%m-%d %H:%M"

#unset key

set bmargin 8

