import statistics
import csv
import pandas as pd

print()
print("Calculation of mean,median,mode of data:- ")
df = pd.read_csv("StudentsPerformance.csv")
math_score = df["math score"].tolist()
reading_score = df["reading score"].tolist()
writing_score = df["writing score"].tolist()

m_mean = statistics.mean(math_score)
r_mean = statistics.mean(reading_score)
w_mean = statistics.mean(writing_score)

m_median = statistics.median(math_score)
r_median = statistics.median(reading_score)
w_median = statistics.median(writing_score)

m_mode = statistics.mode(math_score)
r_mode = statistics.mode(reading_score)
w_mode = statistics.mode(writing_score)

print()
print("Mean for All Scores is:-\n","Math Score=>", m_mean,"\nReading Score=>",r_mean,"\nWriting Score=>",w_mean)

print()
print("Median for All Scores is:-\n","Math Source=>",m_median,"\nReading Score=>",r_median,"\nWriting Score=>",w_median)

print()
print("Mode for All Scores is =>\n","Math Source=>",m_mode,"\nReading Score=>",r_mode,"\nWriting Score=>",w_mode)

m_std_dev = statistics.stdev(math_score)
r_std_dev = statistics.stdev(reading_score)
w_std_dev = statistics.stdev(writing_score)

print()
## Math score
print("Standard Deviation for Math Score Data:- ")
first_std_deviation_start, first_std_deviation_end = m_mean - m_std_dev,m_mean + m_std_dev 
second_std_deviation_start, second_std_deviation_end = m_mean-(2*m_std_dev),m_mean+(2*m_std_dev)
third_std_deviation_start, third_std_deviation_end = m_mean-(3*m_std_dev),m_mean+(3*m_std_dev)

# "%" of data within 1
math_score_of_data_within_1_std_deviation=[result for result in math_score if result>first_std_deviation_start and result<first_std_deviation_end]
print("{}% of data of for math lies within 1 standard deviation".format(len(math_score_of_data_within_1_std_deviation)))

# "%" of data within 2
math_score_of_data_within_2_std_deviation=[result for result in math_score if result>second_std_deviation_start and result<second_std_deviation_end]
print("{}% of data of for math lies within 2 standard deviation".format(len(math_score_of_data_within_2_std_deviation)))

# "%" of data within 3
math_score_of_data_within_3_std_deviation=[result for result in math_score if result>third_std_deviation_start and result<third_std_deviation_end]
print("{}% of data of for math lies within 3 standard deviation".format(len(math_score_of_data_within_3_std_deviation)))

print()
##Reading score
print("Standard Deviation for Reading Score Data:- ")
first_std_deviation_start, first_std_deviation_end = r_mean - r_std_dev, r_mean + r_std_dev
second_std_deviation_start, second_std_devation_end = r_mean - (2*r_std_dev), r_mean + (2*r_std_dev)
third_std_deviation_start, third_std_devation_end = r_mean - (3*r_std_dev), r_mean + (3*r_std_dev)

# "%" of data within 1
reading_score_of_data_within_1_std_deviation = [result for result in reading_score if result > first_std_deviation_start and result < first_std_deviation_end]
print("{}% of data of for reading lies within 1 standard deviation".format(len(reading_score_of_data_within_1_std_deviation)))

# "%" of data within 2
reading_score_of_data_within_2_std_deviation=[result for result in reading_score if result>second_std_deviation_start and result<second_std_deviation_end]
print("{}% of data of for reading lies within 2 standard deviation".format(len(reading_score_of_data_within_2_std_deviation)))

# "%" of data within 3
reading_score_of_data_within_3_std_deviation=[result for result in reading_score if result>third_std_deviation_start and result<third_std_deviation_end]
print("{}% of data of for reading lies within 3 standard deviation".format(len(reading_score_of_data_within_3_std_deviation)))

print()
## Writing score
print("Standard Deviation for Writing Score Data:- ")
first_std_deviation_start, first_std_deviation_end = w_mean - w_std_dev, w_mean + w_std_dev
second_std_deviation_start , second_std_deviation_end = w_mean - (2*w_std_dev), w_mean + (2*w_std_dev)
third_std_deviation_start, third_std_deviation_end = w_mean - (3*w_std_dev), w_mean + (3*w_std_dev)

# "%" of data within 1
writing_score_of_data_within_1_std_deviation = [result for result in writing_score if result > first_std_deviation_start and result < first_std_deviation_end]
print("{}% of data of for writing lies within 1 standard deviation".format(len(writing_score_of_data_within_1_std_deviation)))

# "%" of data within 2
writing_score_of_data_within_2_std_deviation=[result for result in writing_score if result>second_std_deviation_start and result<second_std_deviation_end]
print("{}% of data of for writing lies within 2 standard deviation".format(len(writing_score_of_data_within_2_std_deviation)))

# "%" of data within 3
writing_score_of_data_within_3_std_deviation=[result for result in writing_score if result>third_std_deviation_start and result<third_std_deviation_end]
print("{}% of data of for writing lies within 3 standard deviation".format(len(writing_score_of_data_within_3_std_deviation)))



