def print_chessboard(size):
    for i in range(size):
        for j in range(size):
            # Alternating characters based on row and column indexes
            if (i + j) % 2 == 0:
                print("■", end=" ")
            else:
                print("□", end=" ")
        print()  # Move to the next line after each row


def main():
    row= int(input("Enter the number of row : "))
    print_chessboard(row)
main()