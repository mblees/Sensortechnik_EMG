# Quellen: https://www.researchgate.net/figure/EMG-recordings-and-gesture-recognition-with-BCEMs-a-EMG-signals-arising-from-a-pattern_fig5_360887241

from random import *
import matplotlib.pyplot as plt


def generate_small_amplitude_signal():
    signal = [0]
    global random_start
    global random_end
    global pos_low
    global pos_high
    global random_pos_1
    global random_pos_2
    global random_pos_3
    global random_pos_4
    global random_pos_5
    global random_pos_6
    global random_pos_7
    global random_pos_8

    # Signal with an Amplitude of < 0.1
    for i in range(1, 200):
        # generate an interval starting from 0.1mV
        if (i >= random_start) and (i <= random_end):
            if (i >= random_pos_1) and (i < random_pos_2):
                signal.append(round(uniform(0.03, 0.1), 4))
                signal.append(round(uniform(-0.1, -0.03), 4))
            elif (i >= random_pos_2) and (i < random_pos_3):
                signal.append(round(uniform(0.03, 0.1), 4))
                signal.append(round(uniform(-0.1, -0.03), 4))
            elif (i >= random_pos_3) and (i < random_pos_4):
                signal.append(round(uniform(0.02, 0.08), 4))
                signal.append(round(uniform(-0.08, -0.02), 4))
            elif (i >= random_pos_4) and (i < random_pos_5):
                signal.append(round(uniform(0.02, 0.08), 4))
                signal.append(round(uniform(-0.08, -0.02), 4))
            elif (i >= random_pos_5) and (i < random_pos_6):
                signal.append(round(uniform(0.02, 0.06), 4))
                signal.append(round(uniform(-0.06, -0.02), 4))
            elif (i >= random_pos_6) and (i < random_pos_7):
                signal.append(round(uniform(0.02, 0.06), 4))
                signal.append(round(uniform(-0.06, -0.02), 4))
            elif (i >= random_pos_7) and (i < random_pos_8):
                signal.append(round(uniform(0.02, 0.04), 4))
                signal.append(round(uniform(-0.04, -0.02), 4))
            elif (i >= random_pos_8) and (i <= random_end):
                signal.append(round(uniform(0.02, 0.04), 4))
                signal.append(round(uniform(-0.04, -0.02), 4))

        else:
            signal.append(round(uniform(-0.02, 0.02), 3))

    return signal


def generate_medium_amplitude_signal():
    signal = [0]
    global random_start
    global random_end
    global pos_low
    global pos_high
    global random_pos_1
    global random_pos_2
    global random_pos_3
    global random_pos_4
    global random_pos_5
    global random_pos_6
    global random_pos_7
    global random_pos_8

    # Signal with an Amplitude of < 0.3
    for i in range(1, 200):
        # generate an interval starting from 0.1mV
        if (i >= random_start) and (i <= random_end):
            if (i >= random_pos_1) and (i < random_pos_2):
                signal.append(round(uniform(0.04, 0.10), 4))
                signal.append(round(uniform(-0.10, -0.02), 4))
            elif (i >= random_pos_2) and (i < random_pos_3):
                signal.append(round(uniform(0.04, 0.10), 4))
                signal.append(round(uniform(-0.10, -0.02), 4))
            elif (i >= random_pos_3) and (i < random_pos_4):
                signal.append(round(uniform(0.08, 0.16), 4))
                signal.append(round(uniform(-0.16, -0.08), 4))
            elif (i >= random_pos_4) and (i < random_pos_5):
                signal.append(round(uniform(0.08, 0.18), 4))
                signal.append(round(uniform(-0.18, -0.08), 4))
            elif (i >= random_pos_5) and (i < random_pos_6):
                signal.append(round(uniform(0.04, 0.12), 4))
                signal.append(round(uniform(-0.12, -0.04), 4))
            elif (i >= random_pos_6) and (i < random_pos_7):
                signal.append(round(uniform(0.04, 0.12), 4))
                signal.append(round(uniform(-0.12, -0.04), 4))
            elif (i >= random_pos_7) and (i < random_pos_8):
                signal.append(round(uniform(0.04, 0.10), 4))
                signal.append(round(uniform(-0.10, -0.02), 4))
            elif (i >= random_pos_8) and (i <= random_end):
                signal.append(round(uniform(0.02, 0.04), 4))
                signal.append(round(uniform(-0.04, -0.02), 4))

        else:
            signal.append(round(uniform(-0.02, 0.02), 3))

    return signal


def generate_high_amplitude_signal():
    signal = [0]
    global random_start
    global random_end
    global pos_low
    global pos_high
    global random_pos_1
    global random_pos_2
    global random_pos_3
    global random_pos_4
    global random_pos_5
    global random_pos_6
    global random_pos_7
    global random_pos_8

    # Signal with an Amplitude of < 0.3
    for i in range(1, 200):
        # generate an interval starting from 0.1mV
        if (i >= random_start) and (i <= random_end):
            if (i >= random_pos_1) and (i < random_pos_2):
                signal.append(round(uniform(0.08, 0.16), 4))
                signal.append(round(uniform(-0.16, -0.08), 4))
            elif (i >= random_pos_2) and (i < random_pos_3):
                signal.append(round(uniform(0.08, 0.16), 4))
                signal.append(round(uniform(-0.16, -0.08), 4))
            elif (i >= random_pos_3) and (i < random_pos_4):
                signal.append(round(uniform(0.08, 0.25), 4))
                signal.append(round(uniform(-0.25, -0.08), 4))
            elif (i >= random_pos_4) and (i < random_pos_5):
                signal.append(round(uniform(0.08, 0.28), 4))
                signal.append(round(uniform(-0.28, -0.08), 4))
            elif (i >= random_pos_5) and (i < random_pos_6):
                signal.append(round(uniform(0.08, 0.25), 4))
                signal.append(round(uniform(-0.25, -0.08), 4))
            elif (i >= random_pos_6) and (i < random_pos_7):
                signal.append(round(uniform(0.08, 0.16), 4))
                signal.append(round(uniform(-0.16, -0.08), 4))
            elif (i >= random_pos_7) and (i < random_pos_8):
                signal.append(round(uniform(0.05, 0.14), 4))
                signal.append(round(uniform(-0.14, -0.05), 4))
            elif (i >= random_pos_8) and (i <= random_end):
                signal.append(round(uniform(0.05, 0.14), 4))
                signal.append(round(uniform(-0.14, -0.05), 4))

        else:
            signal.append(round(uniform(-0.02, 0.02), 3))

    return signal


def ploting_signal(signal, name):
    plt.plot(signal)
    plt.title('Example Signal: ' + name)
    plt.xlabel('Time in Csec')
    plt.ylabel('Value in mV')
    plt.ylim(-0.5, 0.5)  # Set y-axis limit


def ploting_signal_for_channel(signal, name):
    plt.figure(figsize=(40, 10))
    plt.plot(signal)
    plt.title('Example Signal: ' + name)
    plt.xlabel('Time in Csec')
    plt.ylabel('Value in mV')
    plt.ylim(-0.5, 0.5)  # Set y-axis limit


def save_signal(name):
    save_location = "C:\\Users\\mariu\\Documents\\plots\\"
    save_location = save_location + name + ".png"
    print(save_location)

    plt.savefig(save_location)
    plt.close()


def generate_random_signal(name, x):
    # Hauptliste Element: 0: Daumen, 1: Zeigefinger, 2: Mittelfinger, 3: Ringfinger, 4: kleiner Finger
    # untergeordnete Liste: 1: small_amplitude_signal, 2: medium_amplitude_signal, 3: high_amplitude_signal
    possible_combinations = [[2, 1, 1], [2, 1, 2], [1, 2, 3], [2, 3, 3], [1, 1, 2]]
    combination_in_use = possible_combinations[randint(0, 4)]

    # arrays for the different channels
    global channel_1
    global channel_2
    global channel_3

    small_amplitude_signal_counter = 0
    medium_amplitude_signal_counter = 0
    high_amplitude_signal_counter = 0
    counter = 1

    for element in combination_in_use:
        example_signal = []
        if element == 1:
            example_signal = generate_small_amplitude_signal()
            ploting_signal(example_signal, "small")
            save_signal(name + "__" + str(element) + "." + str(small_amplitude_signal_counter))
            small_amplitude_signal_counter += 1

        elif element == 2:
            example_signal = generate_medium_amplitude_signal()
            ploting_signal(example_signal, "medium")
            save_signal(name + "__" + str(element) + "." + str(medium_amplitude_signal_counter))
            medium_amplitude_signal_counter += 1

        elif element == 3:
            example_signal = generate_high_amplitude_signal()
            ploting_signal(example_signal, "high")
            save_signal(name + "__" + str(element) + "." + str(high_amplitude_signal_counter))
            high_amplitude_signal_counter += 1

        else:
            print("\nIhre Eingabe der Signale im Hauptarray war fehlerhaft. Bitte überprüfen!")

        if counter == 1:
            channel_1 += example_signal

        elif counter == 2:
            channel_2 += example_signal

        else:
            channel_3 += example_signal

        counter += 1


# ------------------main------------------
random_start = randint(60, 80)
random_end = randint(150, 170)
random_pos_1 = randint(random_start, 90)
random_pos_2 = randint(random_pos_1, 100)
random_pos_3 = randint(random_pos_2, 110)
random_pos_4 = randint(random_pos_3, 120)
random_pos_5 = randint(random_pos_4, 130)
random_pos_6 = randint(random_pos_5, 140)
random_pos_7 = randint(random_pos_6, 150)
random_pos_8 = randint(random_pos_7, random_end)
pos_low = 5
pos_high = 52

# arrays for the different channels
channel_1 = []
channel_2 = []
channel_3 = []

for x in range(5):
    generate_random_signal("graph_" + str(x), x)

ploting_signal_for_channel(channel_1, "channel_1")
save_signal("channel_1")

ploting_signal_for_channel(channel_2, "channel_2")
save_signal("channel_2")

ploting_signal_for_channel(channel_3, "channel_3")
save_signal("channel_3")


def rectify_signal(signal):
    for i in range(len(signal)):
        if signal[i] < 0:
            signal[i] = signal[i] * -1


def integral_signal(signal):
    signal_integral = [0, 0, 0, 0, 0]
    for step in range(len(signal) - 10):
        sum = 0
        for i in range(10):
            sum = signal[step + i] + sum
        signal_integral.append(sum / 10)
    return signal_integral


def analyse_signal(signal):
    size_signal = 150
    activator = 0.025
    ignore = 0
    sum_analysis = 0
    for step in range(len(signal) - size_signal):
        if ignore == 1 and ((signal[step] + signal[step + 1]) / 2) > activator:
            signal[step] = sum_analysis
            if ((signal[step + 1] + signal[step + 2]) / 2) <= activator:
                ignore = 0
        elif ((signal[step] + signal[step + 1]) / 2) > activator:
            sum_analysis = 0
            for i in range(size_signal):
                sum_analysis = signal[step + i] + sum_analysis
            sum_analysis = sum_analysis / size_signal
            ignore = 1
        else:
            signal[step] = 0
    for step in range(size_signal):
        signal[len(signal) - size_signal + step] = sum_analysis


def cleanup_signal(signal):
    front = 0
    for i in range(len(signal)):
        if signal[i] != front and front == 0:
            front = signal[i]
            signal[i] = 0
        else:
            front = signal[i]


def klassify_analysis(signal):
    for step in range(len(signal)):
        value = signal[step]
        if value == 0:
            signal[step] = 0
        if 0 < value < 0.055:
            signal[step] = 1
        if 0.055 <= value < 0.1:
            signal[step] = 2
        if 0.1 <= value < 0.2:
            signal[step] = 3


def compare_signals(signal1, signal2, signal3):
    combined_signal = []
    output_signal = []
    for step in range(len(signal1)):
        combined_signal.append([signal1[step], signal2[step], signal3[step]])
        if combined_signal[step] == [2, 1, 1]:
            output_signal.append(1)
        elif combined_signal[step] == [2, 1, 2]:
            output_signal.append(2)
        elif combined_signal[step] == [1, 2, 3]:
            output_signal.append(3)
        elif combined_signal[step] == [2, 3, 3]:
            output_signal.append(4)
        elif combined_signal[step] == [1, 1, 2]:
            output_signal.append(5)
        else:
            output_signal.append(0)
    return output_signal


def analyse_channel(channel, channel_name):
    plt.figure(figsize=(40, 10))
    plt.plot(channel)
    rectify_signal(channel)
    plt.plot(channel)
    channel = integral_signal(channel)
    plt.plot(channel)
    analyse_signal(channel)
    cleanup_signal(channel)
    plt.plot(channel)
    analyse_analysis(channel)
    plt.plot(channel)
    plt.title('Example Signal: ' + channel_name)
    plt.xlabel('Time in Csec')
    plt.ylabel('Value in mV')
    save_signal(channel_name + "_analysis")

    return channel


channel_1 = analyse_channel(channel_1, "channel_1")
channel_2 = analyse_channel(channel_2, "channel_2")
channel_3 = analyse_channel(channel_3, "channel_3")

plt.figure(figsize=(40, 10))
plt.plot(compare_signals(channel_1, channel_2, channel_3))
save_signal("output_signal")
