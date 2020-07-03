# Import the random module and reference it as rd
import random as rd

num_trials = 100 # Sets the number of flips
heads = 0 # A counter for the number of heads
tails = 0 # A counter for the number of tails
p_heads = 0.5  # The probability for heads

# Simulate coin flips up to the num_trials specified
for i in range(num_trials):
    # Collect a random number between [0,1]
    random_number = rd.random()
    # If the number is less than heads count it as heads
    # Otherwise, count it as tails
    if random_number <= p_heads:
        heads = heads + 1
    else:
        tails += 1

print("In", num_trials, "trials there were", heads, "heads and", tails, "tails")
print("PERCENT HEADS:", 100 * heads/num_trials, "percent")