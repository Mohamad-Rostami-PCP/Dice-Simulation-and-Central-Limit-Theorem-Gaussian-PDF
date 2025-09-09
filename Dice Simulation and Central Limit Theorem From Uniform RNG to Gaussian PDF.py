# import libs
import numpy as np
import random
import matplotlib.pyplot as plt



# variables
N = 1000
discrete = 69




# Dice Set Generator
def DiceSet(N):
    Dice = np.zeros(N)
    for i in range(N):
        value = random.random() * 6
        for j in range(6):
            if j < value < j + 1:
                Dice[i] = j + 1
    return Dice


# Statistics Printer Function
def StatisticPrinter(data):
    # Mean
    mean = np.mean(data)
    print(f"the mean is: {mean}")
    # Variance
    var = np.var(data)
    print(f"the var is: {var}")
    # std
    std = np.std(data)
    print(f"the std is:{std}")

    # Auto-Correlation
    def ACF(DataSet):

        def Cov(X, Y):
            n = X.shape[0]
            XY = np.zeros(n)
            for i in range(n):
                XY[i] = X[i] * Y[i]
            cov = np.mean(XY) - np.mean(X) * np.mean(Y)
            return cov

        def Cor(X, Y):
            covariance = Cov(X, Y)

            # if (np.sqrt(np.var(X) * np.var(Y)) == 0):
            #     print("here are naughty X and Y")
            #     print(f"X:{X}")
            #     print(f"Y:{Y}")

            cor = covariance / np.sqrt(np.var(X) * np.var(Y))

            return cor

        N = DataSet.shape[0]

        ACF_SET = np.zeros(N)



        for θ in range(N):
            X_nθ = np.zeros(N)
            for i in range(θ, N + θ):
                X_nθ[i - θ] = DataSet[i % N]

            ACF_SET[θ] = Cor(X_nθ, DataSet)


        return ACF_SET

    global AutoCorrelation
    AutoCorrelation = ACF(data)

    print(f"the auto-correlation set is: {AutoCorrelation}")


# subseter function
def subseter(M, Dice_arb):
    Big_data = np.zeros((M, 10))
    Big_data_mean = np.zeros(M)

    for p in range(M):
        for j in range(10):
            Big_data[p, j] = random.choice(Dice_arb)
        Big_data_mean[p] = np.mean(Big_data[p, :])

    return Big_data_mean


# PDF functions
def PDF(distribution, noIntervals):
    x = np.zeros(noIntervals)
    P_x = np.zeros(noIntervals)

    breakpoints = np.zeros(noIntervals + 1)
    # min = np.min(distribution)
    # max = np.max(distribution)

    min = 0
    max = 7

    steps_length = (max - min) / noIntervals
    for a in range(noIntervals + 1):
        if a == 0:
            breakpoints[a] = min
        else:
            breakpoints[a] = breakpoints[a - 1] + steps_length

    for i in range(noIntervals):
        if i == 0:
            x[0] = breakpoints[0] + breakpoints[1]
        else:
            x[i] = x[i - 1] + steps_length

    for number in distribution:
        for z in range(noIntervals):
            if breakpoints[z] < number < breakpoints[z + 1]:
                P_x[z] += 1
                break
    P_x /= distribution.shape[0]

    return P_x, x


# creat and subset for 1K Dice
Dice_1K = DiceSet(1000)
SubSets_1K = subseter(100, Dice_1K)

# creat and subset for 1M Dice
Dice_1M = DiceSet(1000000)
SubSets_1M = subseter(100000, Dice_1M)

# Printing statistics
StatisticPrinter(Dice_1K)

# plot subsets distributions----------------------------------------
figure, axis = plt.subplots(3)
P_ss_1K, x_ss_1K = PDF(SubSets_1K, 75)
P_ss_1M, x_ss_1M = PDF(SubSets_1M, 69)
axis[0].plot(x_ss_1K, P_ss_1K, 'o', ms=5)
axis[0].set(ylabel="PDF (1K)", xlabel="probability")
axis[0].set_title = "cas"
axis[1].plot(x_ss_1M, P_ss_1M, 'o', ms=5)
axis[1].set(ylabel="PDF (1M)", xlabel="probability")

axis[2].plot(AutoCorrelation)
axis[2].set(ylabel="AUtocorrelation", xlabel="time lage")
plt.show()


# print the plot implication
def print_implication():
    jim = """
    OMG: this guy looks like the Normal distribution we see that with increasing
    the number of throws in our dices more and more our peak of mean distribution
    gets close to the value 3.5 which is dew to the uniform distribution of our
    random generator the mean we excpect after infinit throws also the fact that
    we can see from comparison of this two distribution is that by increasing the
    number of throws more and more our variance decreases and more likely we will
    get to the peak whcich is 3.5 but why is this distribution looks soo much like
    the normal distribution?
    I believe it's dew to centeral limit theorem, which states that if we have infinit
    source of number of noises which in this case the effect each of our dices value
    have on our mean value, the distribution should finally by increasing of numbers
    approach to the Normal distribution.

    Two wonderful things can be induced:
    1. by increasing the size of the random population, if you chose one data it is more 
       likeliy to be the mean value (here 3.5).

    2. if you look at the each 10set as a random source with mean (3.5) and variance(Sigma) 
        then by increasing the number of this sources(in here from 1000 to 1000000) centeral limit theorem propose the 
        distribution should approach to a Normal distribution, and as we can see it does.
    """

    print(jim)


print_implication()
