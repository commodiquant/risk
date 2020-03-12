import numpy

def lpm(returns, threshold, order):
    # This method returns a lower partial moment of the returns
    # Create an array he same length as returns containing the minimum return threshold
    threshold_array = numpy.empty(len(returns))
    threshold_array.fill(threshold)
    # Calculate the difference between the threshold and the returns
    diff = returns - threshold_array
    # Set the minimum of each to 0
    diff = numpy.clip(diff, None, 0)
    # Return the sum of the different to the power of order
    return numpy.sum(diff ** order) / len(returns)


def hpm(returns, threshold, order):
    # This method returns a higher partial moment of the returns
    # Create an array he same length as returns containing the minimum return threshold
    threshold_array = numpy.empty(len(returns))
    threshold_array.fill(threshold)
    # Calculate the difference between the returns and the threshold
    diff = returns - threshold_array
    # Set the minimum of each to 0
    diff = numpy.clip(diff, 0, None)
    # Return the sum of the different to the power of order
    return numpy.sum(diff ** order) / len(returns)


# Example Usage
# import numpy.random as nrand
# r = nrand.uniform(-1, 1, 50)
# print("hpm(0.0)_1 =", hpm(r, 0.0, 1))
# print("lpm(0.0)_1 =", lpm(r, 0.0, 1))