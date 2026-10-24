
from collections import Counter
from statistics import mean, median, pvariance, variance
import random


# 1. STAFF COLOUR DATA


days = {
    "MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "FRIDAY": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
}

colors_by_day = {
    day: [color.strip().upper() for color in text.split(",")]
    for day, text in days.items()
}

all_colors = [
    color
    for daily_colors in colors_by_day.values()
    for color in daily_colors
]

frequencies = Counter(all_colors)


# 2. COLOUR FREQUENCIES


print("\nCOLOUR FREQUENCIES")
for color, count in sorted(frequencies.items()):
    print(f"{color}: {count}")

print("Total entries:", len(all_colors))


# 3. MOST-WORN COLOUR (MODE)

highest_frequency = max(frequencies.values())

most_worn = [
    color for color, count in frequencies.items()
    if count == highest_frequency
]

print("\nMOST-WORN COLOUR:", ", ".join(most_worn))


# 4. MEAN, MEDIAN AND VARIANCE

# Colours are categories, not numbers. Therefore, these statistics are calculated on the FREQUENCY COUNTS, not colour names.

frequency_values = list(frequencies.values())

print("\nSTATISTICS OF COLOUR FREQUENCIES")
print("Mean frequency:", mean(frequency_values))
print("Median frequency:", median(frequency_values))
print("Population variance:", pvariance(frequency_values))
print("Sample variance:", variance(frequency_values))


# 5. PROBABILITY OF RED

total = len(all_colors)
red_count = frequencies.get("RED", 0)

if total > 0:
    probability = red_count / total
    print("\nProbability of RED:", probability)
    print("Percentage of RED:", probability * 100, "%")
else:
    print("\nNo colour data available.")



# 6. RECURSIVE BINARY SEARCH

def recursive_search(numbers, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if numbers[middle] == target:
        return middle

    if target < numbers[middle]:
        return recursive_search(
            numbers, target, left, middle - 1
        )

    return recursive_search(
        numbers, target, middle + 1, right
    )


numbers = [2, 5, 8, 12, 16, 23, 38]

print("\nRECURSIVE SEARCH")
try:
    target = int(input("Enter a number to search for: "))

    result = recursive_search(
        numbers, target, 0, len(numbers) - 1
    )

    if result == -1:
        print("Number not found.")
    else:
        print("Number found at index:", result)

except ValueError:
    print("Please enter a valid integer.")


# 7. FOUR-DIGIT BINARY TO DECIMAL


binary_number = "".join(
    random.choice("01") for _ in range(4)
)

decimal_number = int(binary_number, 2)

print("\nBINARY CONVERSION")
print("Binary number:", binary_number)
print("Decimal number:", decimal_number)


# 8. SUM OF FIRST 50 FIBONACCI TERMS


def fibonacci_sum(count):
    a, b = 0, 1
    total_sum = 0

    for _ in range(count):
        total_sum += a
        a, b = b, a + b

    return total_sum


print("\nFIBONACCI")
print("Sum of first 50 terms:", fibonacci_sum(50))


# 9. SAVE TO POSTGRESQL


def save_to_postgresql():
    import os
    import psycopg

    with psycopg.connect(
        dbname=os.environ["PGDATABASE"],
        user=os.environ["PGUSER"],
        password=os.environ["PGPASSWORD"],
        host=os.environ.get("PGHOST", "localhost"),
        port=os.environ.get("PGPORT", "5432")
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS colour_frequencies (
                    colour VARCHAR(50) PRIMARY KEY,
                    frequency INTEGER NOT NULL
                )
            """)

            for color, count in frequencies.items():
                cursor.execute("""
                    INSERT INTO colour_frequencies (colour, frequency)
                    VALUES (%s, %s)
                    ON CONFLICT (colour)
                    DO UPDATE SET frequency = EXCLUDED.frequency
                """, (color, count))

    print("Colour frequencies saved to PostgreSQL.")

save_to_postgresql()
