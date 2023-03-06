# Module to manage balances.

user_balances = {}

def create_balance(username, difficulty):
	global user_balances
	if difficulty not in ["easy","medium","hard"]:
		return TypeError
	elif difficulty == "easy":
		user_balances[username] = 2000
		return 2000
	elif difficulty == "medium":
		user_balances[username] = 1000
		return 1000
	elif difficulty == "hard":
		user_balances[username] = 500
		return 500
	else:
		return Exception

def get_balance(username):
	global user_balances
	return user_balances[username]