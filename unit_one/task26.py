
import pandas
import matplotlib
import matplotlib.pyplot as plt

#  help(pandas)
#  help(matplotlib)

#cov_data = pandas.read_csv('D:\python_course\DDVMV_JOSX-07__S14.amplicon_coverage.tsv', delimiter = '\t')

cov_data = pandas.read_csv('test_data\DDVMV_JOSX-07__S14.amplicon_coverage.tsv', delimiter = '\t')

sorted = cov_data.sort_values(by = ['total_reads'])  # Sort data frame by total reads in ascending order

fig, ax = plt.subplots()  # Create a figure containing a single axes.

ax.plot(sorted.amplicon_id, sorted.total_reads) # Plot some data on the axes.

plt.xticks(rotation=90)  # Rotate X axis label to vertical

matplotlib.pyplot.title('Total reads per amplicon', fontdict=None, loc='center', pad=None)  # Add plot title

matplotlib.pyplot.xlabel('Amplicon ID', fontdict=None, labelpad=None)  # Add X axis label

matplotlib.pyplot.ylabel('Total reads', fontdict=None, labelpad=None)  # Add Y axis label

plt.show()  # Print plot
