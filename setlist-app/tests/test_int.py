import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from application import app, db
from application.models import Songs, SetList, SetLink

#set test variables
test_songb_song_name = "Genesis" 
test_songb_song_album = "Cross"
test_songb_song_artist = "Justice"
test_songb_song_key = "C"
test_songb_song_bpm = "117"
test_edit_song_name = "Safe and Sound"
test_edit_song_album = "Woman"
test_edit_song_artist = "Justice"
test_edit_song_key = "Db/C#"
test_edit_song_bpm = "115"
test_vedset_set_name = "Across the Universe"
test_edit_set_name = "Nope"
test_add_song_set ="1"
test_add_set_song = "1"

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DB_URI'))
        app.config['SECRET_KEY'] = getenv('TEST_SECRET_KEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)


class TestHomeButton(TestBase):

	def test_home_button(self):
#testing home button will bring user to home page
		self.driver.find_element_by_xpath('/html/body/a[1]').click()
		time.sleep(1)
#asserting browser redirects to home page
		assert url_for('home') in self.driver.current_url


class TestAddSongBankButton(TestBase):

	def test_add_song_bank_button(self):
#testing add song to songbank  button will bring user to add songbank page
		self.driver.find_element_by_xpath('/html/body/a[2]').click()
		time.sleep(1)
		self.driver.find_element_by_xpath('//*[@id="song_name"]').send_keys(test_songb_song_name)
		self.driver.find_element_by_xpath('//*[@id="song_album"]').send_keys(test_songb_song_album)
		self.driver.find_element_by_xpath('//*[@id="song_artist"]').send_keys(test_songb_song_artist)
		#not inclusing select as elemant will be pre populated with C
		self.driver.find_element_by_xpath('//*[@id="song_key"]').send_keys('C')
		self.driver.find_element_by_xpath('//*[@id="song_bpm"]').send_keys(test_songb_song_bpm)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)
#asserting browser redirects to songbank page
		assert url_for('songbank') in self.driver.current_url

class TestSongBankButton(TestBase):

	def test_song_bank_button(self):
#testing songbank  button will bring user to songbank page
		self.driver.find_element_by_xpath('/html/body/a[3]').click()
		time.sleep(1)
#asserting browser redirects to home page
		assert url_for('songbank') in self.driver.current_url


class TestViewEditDeleteSetButton(TestBase):

	def test_view_edit_delete_set_button(self):
#testing view/edit/delete set nav bar  button will bring user to view/edit/delete set page
		self.driver.find_element_by_xpath('/html/body/a[4]').click()
		time.sleep(1)
#asserting browser redirects to view/edit/delete set  page
		assert url_for('create') in self.driver.current_url

class TestAddSongSetButton(TestBase):
	
	def test_add_song_set_button(self):
#testing add song to set set nav bar  button will bring user to add song to set page
		self.driver.find_element_by_xpath('/html/body/a[5]').click()
		time.sleep(1)
#asserting browser redirects to add song to set set  page
		assert url_for('querysetsong') in self.driver.current_url



if __name__ == '__main__':
	unittest.main(port=5000)
