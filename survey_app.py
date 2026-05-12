# This program asks users about their favorite things and clothing size

def main():
    print("Welcome to the Favorite Things Survey App!\n")

    # Ask questions
    name = input("What is your name? ")

    favorite_store = input("What is your favorite store? ")

    favorite_food = input("What is your favorite food? ")

    favorite_color = input("What is your favorite color? ")

    clothing_size = input("What is your clothing size? ")

    # Display results
    print("\n--- Survey Results ---")
    print(f"Name: {name}")
    print(f"Favorite Store: {favorite_store}")
    print(f"Favorite Food: {favorite_food}")
    print(f"Favorite Color: {favorite_color}")
    print(f"Clothing Size: {clothing_size}")

    print("\nThank you for completing the survey!")


# Run the app
if __name__ == "__main__":
    main()
