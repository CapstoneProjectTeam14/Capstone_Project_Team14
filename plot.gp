# Set output format and file name
set terminal png size 800,600 enhanced font 'Verdana,12'
set output "cbench_plot.png"

# Set plot title and axis labels
set title "Cbench Data"
set xlabel "Time"
set ylabel "Response/Requests"

# Adjust the background color
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb "#f0f0f0" behind

# Enable grid lines
set grid

# Define the data file and format
datafile = "cbench.txt"
set datafile separator "/"

# Define line styles with different colors
set style line 1 lc rgb "blue" lt 1 lw 2
set style line 2 lc rgb "red" lt 1 lw 2
set style line 3 lc rgb "green" lt 1 lw 2
set style line 4 lc rgb "orange" lt 1 lw 2
set style line 5 lc rgb "purple" lt 1 lw 2
# Add more line styles if you have more switches

# Set a legend
set key at graph 0.95, graph 0.95
set key box lt -1 lw 1
set key spacing 1.5

# Plot data
plot datafile using 1:2 with lines ls 1 title 'Switch 1 Response', \
     datafile using 1:3 with lines ls 2 title 'Switch 1 Requests', \
     datafile using 1:4 with lines ls 3 title 'Switch 2 Response', \
     datafile using 1:5 with lines ls 4 title 'Switch 2 Requests'
# Add more plot commands if you have more switches
