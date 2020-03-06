from web_objects.web_page_objects import generation_random_numbers
from web_objects.web_page_objects import validate_file_in_path

class ww_task_helper(object):

    def generate_random_numbers(self, number_range=None, count=None, nth_min=None):
        """
        If Parameters are NONE default values will be used
        :param number_range: numbers from to number_range
        :param count: total number of numbers
        :param nth_min: nth minimum value
        :return: returns nth_min value and it's Index
        """
        random_class = generation_random_numbers(number_range, count, nth_min)
        return random_class.random_numbers()

    def is_file_existed_in_path(self, file_name, file_path):
        """
        Parameter are Mandatory to get the required file within the path
        :param file_name: Name of the file to search
        :param file_path: Directory of the file
        :return: returns False if it unable to find the file in the path
        """
        path_to_file = validate_file_in_path(file_name, file_path)
        return path_to_file.is_file_existed()

    def read_file_values_in_path(self, file_name, file_path):
        """
        This Method Reads the data and prints the values
        :return: returns data in the file
        """
        file_path = validate_file_in_path(file_name, file_path)
        return file_path.get_file_content()

if __name__ == '__main__':
    pass