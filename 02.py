# Created by Roman Beya
# Created 4 ICS3U
# Created on Nov-1-2017
# This program takes a decimal number, then rounds said number to a user generated number of decimal places

import ui

def round_number(number_entered, number_of_decimals):
	# this procedure rounds the number entered by a certain number of decimal places
	
	# apply number of decimals variable to math function
	rounded_number = int(number_entered * 10 ** number_of_decimals + 0.5)
	rounded_number = rounded_number / 10 ** number_of_decimals
	
	# output rounded number
	view['output_label'].text = "Number to be rounded: {0}\n\nNumber of decimal places: {1}\n\nRound number: {2}".format(number_entered, number_of_decimals, rounded_number)

def number_of_decimals_touch_up_inside(sender):
	# round a number by a certain amount of decimals specified by user
	
	# first, we need to get number
	user_number = float(view['enter_number_textfield'].text)
	num_of_decimal_places = float(view['number_of_decimals_textfield'].text)
	round_number(user_number, num_of_decimal_places)

view = ui.load_view()
view.present('sheet')
