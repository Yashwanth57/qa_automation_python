from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import os
import re

class web_page_objects(object):
    """
    Class docs: Objects for weight watchers web page
    """
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.today = datetime.datetime.today().now().strftime("%A")

    def navigate_to_page(self, address):
        return self.browser.get(address)

    def maximize_browser(self):
        return self.browser.maximize_window()

    def close_web_browser(self):
        return self.browser.close()

    def get_element_of_page(self, link_text=None, element_name=None):
        if link_text is not None:
            button = self.browser.find_element_by_link_text("{}".format(str(link_text)))
        elif element_name is not None:
            button = self.browser.find_element_by_name("{}".format(str(element_name)))
        else:
            raise PermissionError(f"Invalid parameters provided")
        return button

    def get_element_by_property(self, link_text=None, element_name=None):
        element_property = self.get_element_of_page(link_text, element_name).get_property("id")
        return self.browser.find_element_by_id(element_property)

    def dismiss_popup(self, wait_time=50):
        self.browser.implicitly_wait(wait_time)
        return webdriver.ActionChains(self.browser).send_keys(Keys.ESCAPE).perform()

    def get_element_by_class(self, class_name, single_element=True):
        self.browser.implicitly_wait(10)
        if single_element:
            button = self.browser.find_element_by_class_name(str(class_name))
        else:
            button = self.browser.find_elements_by_class_name(str(class_name))
            abc = []
            for element_day in button:
                abc.append(element_day.text)
            return abc
        return button

    def get_page_title(self, convert_uni=False):
        title_txt = self.browser.title
        if convert_uni:
            return title_txt.replace(u'\xa0', u' ')
        return title_txt

    def scroll_web_page(self, scroll_to):
        return self.browser.execute_script('arguments[0].scrollIntoView(true);', scroll_to)

    def get_element_by_xpath(self, expath):
        xpath = self.browser.find_element_by_xpath(expath)
        return xpath

    def get_operating_hours_or_appointments(self, class_name):
        available_timings = self.get_element_by_class(class_name, False)
        hours = []
        for day in available_timings:
            if day.split("\n")[0] == str(self.today)[:3].upper():
                operating_hours = day
                hours.append(operating_hours)
        return hours

class generation_random_numbers(object):
    """
    Class docs: This Class generates random numbers within tht given range
    """
    def __init__(self, to_generate=None, number_count=None, nth_value=None):
        """
        :param to_generate: Generate number within range
        :param number_count:
        :param nth_value:
        """
        self.generate = 2000 if to_generate is None else to_generate
        self.count = 500 if number_count is None else number_count
        self.value = 100 if nth_value is None else nth_value

    def random_numbers(self):
        new_list = []
        for numbers in range(self.count):
            new_numbers = randint(0, self.generate)
            if new_numbers not in new_list:
                new_list.append(new_numbers)
        for first in range(len(new_list)):
            for second in range(first + 1, len(new_list)):
                if new_list[first] < new_list[second]:
                    new_list[first], new_list[second] = new_list[second], new_list[first]
        nth_min_index = len(new_list) - self.value
        nth_mim_value = new_list[nth_min_index]
        return f"The {self.value}th minimum value is {nth_mim_value} found at index {nth_min_index}"

class validate_file_in_path(object):
    """
    Class docs: This is the class to get the file in path
    """
    def __init__(self, file, filepath):
        """
        File name and filepath has to be provided
        :param file: Filename
        :param filepath: Filepath
        """
        self.filename = file
        self.root_dir = filepath
        self.required_file = os.path.join(self.root_dir, self.filename)

    def is_file_existed(self):
        try:
            with open(self.required_file) as ftp:
                ftp.close()
                print(f"{self.filename} existed at {self.required_file}")
                return True
        except FileNotFoundError as err:
            print(err)
            return False

    def get_file_content(self):
        with open(self.required_file, "r") as fl:
            total_data = fl.readlines()
            return [re.split("=|,|:|;|[\n]|>|<", contents) for contents in total_data]

if __name__ == '__main__':
    pass