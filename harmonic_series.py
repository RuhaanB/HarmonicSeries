# Hello everybody, this is Ruhaan here! Just a sidenote; please forgive my sloppy programming.

# I am new to python and don't really have a lot of experience in any programming language(s).

# You can run this programmee I have written below for any number of terms of the
# Harmonic Series and find their sum (Time might be a limiting factor as usual).

# Run this on your terminal or IDLE shell and you will have a chance to input the amount of terms you
# want to add up.


# programme Begins
print(
    "Hello, this is the harmonic series summation calculator! What this programme basically does is computation of the harmonic series, upto a term of your CHOICE (Time is a limiting factor though :(, think carefully before inputting any mammoth amount of terms for summation!\nHave fun and hopefully you will observe patterns for yourself!\n\n"
)
# Defining initial Variables:
Play = True
Denominator = 1
S = 1 / Denominator

# Adding a Replay option

while Play == True:
    # Taking the input
    S_n_input = int(
        input(
            "S being: Sum; And S_n being the sum of the Harmonic Series upto term n\nPlease input a value for n here (n ≥ 0): "
        )
    )
    print(" ")
    print(
        "If you have input a large value of n... please be patient. The programme only displays the final summation and not every single step for efficiency reasons"
    )
    print(" ")
    # Running the main Harmonic Series loop
    if S_n_input >= 0:
        for harmonic in range(0, S_n_input - 1):
            Denominator = Denominator + 1
            S = S + (1 / Denominator)
    # Having an Error Message
    else:
        Play_input = input(
            "Your value for n did not comply with the programme. If you want to retry please let me know(Yes/No): "
        ).lower()
        if Play_input == "yes":
            Play = True
        else:
            Play = False
    # Final Results
    print(
        "S_",
        str(S_n_input),
        " ≈ (Approximation to the nearest Billionth) ≈ ",
        round(S, 9),
    )
    Play_input = input(
        "\nIf you want to retry with another value of n; please let me know(Yes/No): "
    ).lower()
    if Play_input == "yes":
        Play = True
    else:
        Play = False
        break
# GoodBye Message
print(" ")
print(
    "I hope you could play around with this programmeme and get an idea for how slow the Harmonic series grows and how shocking it's divergence truly is! \n\nI hope you had fun! \n\nEmail me at: ruhaanbhargav@outlook.com with the subject: HARMONIC SERIES programmeme if you have any questions or concerns regarding this programmeme!"
)
# NOICE (THE END)
