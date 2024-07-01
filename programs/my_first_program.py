from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")

    # Define inputs (two SecretInteger inputs)
    input1 = SecretInteger(Input(name="input1", party=party1))
    input2 = SecretInteger(Input(name="input2", party=party1))

    # Compute the squares of inputs
    square1 = input1 * input1
    square2 = input2 * input2

    # Compute the sum of squares
    sum_of_squares = square1 + square2

    # Output the sum of squares result
    return [Output(sum_of_squares, "sum_of_squares_output", party1)]
