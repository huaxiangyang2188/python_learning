from die import Die
import pygal
# Create two Die instance
die_1 = Die()
die_2 = Die()
# Roll the die and store the result in a variable
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
hist = pygal.Bar()
hist.title = "Results of multiplying two D6 1000 times."
hist.x_labels = [str(x) for x in range(1, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6*D6',frequencies)
hist.render_to_file('dice_visual.svg')
