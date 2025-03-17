car_rental = {
    "Honda Civic": {"daily_rate": 35, "available":True, "category": "Standard"}
}
rental_request= {"model": "Honda Civic", "days": 8}
def rentCar(cars, requests):
    modelRequest = requests["model"]
    if cars[modelRequest]["available"] == True:
        print(f"{requests["model"]} rented.")
    else: print(f"{requests["model"]} is unavailable. Suggesting") #SUGGEST OTHER CAR

    daysRenting = requests["days"]
    discount = 0
    if cars[modelRequest]["category"] == "Standard" and daysRenting > 7:
        discount = .15
        print("Applying 15% discount for renting standard for more than 7 days.")
    elif cars[modelRequest]["category"] == "Luxury" and daysRenting >= 5:
        discount = .10  
        print("Applying 10% discount for renting luxury for more than 5 days.")

    beforeDiscount = cars[modelRequest]["daily_rate"] * daysRenting
    afterDiscount = beforeDiscount - (beforeDiscount * discount)
    print(f"Total rental cost before discounts: {beforeDiscount}")
    print(f"Total rental cost after discount: {afterDiscount}")

    print(afterDiscount)
rentCar(car_rental, rental_request)