from die import Die
import pygal
# Create a Die instance
die = Die()
# Roll the die and store the result in a variable
results = [die.roll() for roll_num in range(1000)]

# Analyze the results
frequencies = [results.count(value) for value in range(1,die.num_sides+1)]

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [str(i) for i in range(1,die.num_sides+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')
print(frequencies)