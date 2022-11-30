# Set variables for amount due (50) and total inserted coins (0)
ad = 50
ct = 0
# Prompt to insert coins one at a time (loop)
while True:
    ci = int(input("Insert coin: "))
    if ci == 25 or ci == 10 or ci == 5:
        ct = ct + ci
        ad = ad - ci
        # Once reached 50 cents, output how many cents in change
        if ct >= 50:
            print(f"Change owed: {ct - 50}")
            break
    # After coin inserted, inform of amount due
    print(f"Amount due: {ad}")


