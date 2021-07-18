def convert(number):

    factors = { 3: "Pling", 5: "Plang", 7: "Plong" }
    raindrop = ""

    for key, val in factors.items():
        if number % key == 0:
            raindrop += val

    return raindrop or str(number)
