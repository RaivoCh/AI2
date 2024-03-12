#AI for Everyone LESSON 7: Understanding Pictures and Images as Data Arrays
#https://www.youtube.com/watch?v=W43MpRroplA&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=10

##HOMEWORK
#chessboard
#chessboar is square, so same number of rows and colums

###############################################################
## this code created Gemini after I asked to analyze my code ##
## and it does not work propperly                            ##
###############################################################


import cv2
import numpy as np

# Define chessboard properties
size_board = 250
num_rows_cols = 7

# Calculate square size
square_size = size_board // num_rows_cols

# Ensure board size is divisible by number of squares
if size_board % num_rows_cols != 0:
    size_board = num_rows_cols * square_size

# Define black color
black_color = (0, 0, 125)

# Create empty frame
frame = np.zeros((size_board, size_board, 3), dtype=np.uint8)

# Fill black squares
for i in range(0, num_rows_cols, 2):
    for j in range(0, num_rows_cols, 2):
        frame[i * square_size:(i + 1) * square_size, j * square_size:(j + 1) * square_size] = black_color

# Display the chessboard
cv2.imshow("Chessboard", frame)
cv2.waitKey(0)  # Wait indefinitely until 'q' is pressed

# Close the window
cv2.destroyAllWindows()
