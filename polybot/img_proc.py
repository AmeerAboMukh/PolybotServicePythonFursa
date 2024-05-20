import random
from pathlib import Path
from matplotlib.image import imread, imsave


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


class Img:

    def __init__(self, path):
        """
        Do not change the constructor implementation
        """
        self.path = Path(path)
        self.data = rgb2gray(imread(path)).tolist()

    def save_img(self):
        """
        Do not change the below implementation
        """
        new_path = self.path.with_name(self.path.stem + '_filtered' + self.path.suffix)
        imsave(new_path, self.data, cmap='gray')
        return new_path

    def blur(self, blur_level=16):

        height = len(self.data)
        width = len(self.data[0])
        filter_sum = blur_level ** 2

        result = []
        for i in range(height - blur_level + 1):
            row_result = []
            for j in range(width - blur_level + 1):
                sub_matrix = [row[j:j + blur_level] for row in self.data[i:i + blur_level]]
                average = sum(sum(sub_row) for sub_row in sub_matrix) // filter_sum
                row_result.append(average)
            result.append(row_result)

        self.data = result

    def contour(self):
        for i, row in enumerate(self.data):
            res = []
            for j in range(1, len(row)):
                res.append(abs(row[j-1] - row[j]))

            self.data[i] = res

    def rotate(self):
        # Get the height and width of the original image
        height_of_original_image = len(self.data)
        width_of_original_image = len(self.data[0])

        # Create a new list to hold the rotated image data
        rotated_data = []

        # Iterate over each column of the original image (from last to first)
        for j in range(width_of_original_image):
            new_row = []
            # Iterate over each row of the original image (from first to last)
            for i in range(height_of_original_image):
                # Append the pixel value to the new row
                new_row.append(self.data[height_of_original_image - 1 - i][j])
            # Append the new row to the rotated image data
            rotated_data.append(new_row)

        # Update the current image data with the rotated data
        self.data = rotated_data

    def salt_n_pepper(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                # Generate a random number between 0 and 1
                rand_num = random.random()
                # If the random number is less than 0.2, set the pixel to 255 (salt)
                if rand_num < 0.2:
                    self.data[i][j] = 255
                # If the random number is greater than 0.8, set the pixel to 0 (pepper)
                elif rand_num > 0.8:
                    self.data[i][j] = 0

    def concat(self, other_img, direction='horizontal'):
        # Get the dimensions of the current image
        height_of_first_image, width_of_first_image = len(self.data), len(self.data[0])
        # Get the dimensions of the other image
        height_of_second_image, width_of_second_image = len(other_img.data), len(other_img.data[0])

        if direction == 'horizontal':
            # Check if the heights of both images are the same
            if height_of_first_image != height_of_second_image:
                raise RuntimeError("Images do not have the same height and cannot be concatenated horizontally!!")

            # Create a new list to hold the concatenated image data
            concatenated_data = []
            for row_in_first_image, row_in_second_image in zip(self.data, other_img.data):
                concatenated_data.append(row_in_first_image + row_in_second_image)  # Concatenate each row horizontally

        elif direction == 'vertical':
            # Check if the widths of both images are the same
            if width_of_first_image != width_of_second_image:
                raise RuntimeError("Images do not have the same width and cannot be concatenated vertically!!")

            # Concatenate the images vertically
            concatenated_data = self.data + other_img.data  # Concatenate each row vertically

        else:
            raise ValueError("Direction must be either 'horizontal' or 'vertical'!!")

        # Update the current image data with the concatenated data
        self.data = concatenated_data

    def segment(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                # Check if the pixel intensity is greater than 100
                if self.data[i][j] > 100:
                    self.data[i][j] = 255  # Set to white
                else:
                    self.data[i][j] = 0  # Set to black
