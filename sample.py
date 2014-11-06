import requests, os

# configuration
CRUNCHBASE_API_KEY = os.environ.get('CRUNCHBASE_API_KEY')
APP_SECRET_KEY = os.environ.get('APP_SECRET_KEY')


def main():
	
	#get a list of investment companies from CB
	investment_company_items = requests.get("http://api.crunchbase.com/v/2/organizations?organization_types=investor&user_key="+str(CRUNCHBASE_API_KEY)).json()["data"]["items"]
	
	#iterate through items and append investment company name to the investors dictionary
	investment_company_dict = {"name": [item["name"] for item in investment_company_items]}
	print investment_company_dict["name"][1:2]

	standardized_investment_co = investment_company_dict["name"][2].lower().replace("(", " ").replace(")", " ").replace(",", "").replace(" | ", " ").replace(".", " ").replace(" - ", "-").replace(" ","-").replace("--", "-")
	
	print "standardized name", standardized_investment_co

	list_standardized_investment_co_items = requests.get("http://api.crunchbase.com/v/2/organization/"+standardized_investment_co+"/investments?user_key="+str(CRUNCHBASE_API_KEY)).json()["data"]["items"]
	
	investment_co_portfolio_companies_dict = {"name": [item["invested_in"]["name"] for item in list_standardized_investment_co_items]}
	
	print "portfolio companies", investment_co_portfolio_companies_dict

	









#user select investment company 1 and company 2 to find common investments






	# for investment_company in investment_company_dict["name"]:  # investment_company_dict["name"] gives me the value to the name key, which is a list, so I have to iterate over the list

	# 	standardized_investment_co = investment_company.lower().replace("(", " ").replace(")", " ").replace(",", "").replace(" | ", " ").replace(".", " ").replace(" - ", "-").replace(" ","-").replace("--", "-")
	# 	standardized_investment_co_items = requests.get("http://api.crunchbase.com/v/2/organization/"+standardized_investment_co+"/investments?user_key="+str(CRUNCHBASE_API_KEY)).json()["data"]["items"]
	

	# Need to iterate over the list above and for each item in the list, go to crunchbase and grab the names of their investments
		
	#for each company, get a list of their portfolio companies
	# list_of_sutter_investment_items = requests.get("http://api.crunchbase.com/v/2/organization/sutter-hill-ventures/investments?user_key="+str(CRUNCHBASE_API_KEY)).json()["data"]["items"]
	
	# list_of_iqt_investment_items  = requests.get("http://api.crunchbase.com/v/2/organization/in-q-tel/investments?user_key="+str(CRUNCHBASE_API_KEY)).json()["data"]["items"]

######### combined these lines in the two lines above ############	
	# The response is json object
	# Turn into a dictionary with .json()
	# iqt_dict = iqt_info.json()
	# sutter_hill_dict = sutter_hill_info.json()

	# Traverse through the dictionary to where the list of investment items are
	# list_of_iqt_investment_items = iqt_dict["data"]["items"]
	# list_of_sutter_investment_items = sutter_hill_dict["data"]["items"]
###################################################################
	
	# Iterate through each investment item list, drilling down to the portfolio company name and appending the name to the appropriate list of portfolio companies.
	iqt_portfolio_companies_dict = {"name": [item["invested_in"]["name"] for item in list_of_iqt_investment_items]}			
	sutter_portfolio_companies_dict = {"name": [item["invested_in"]["name"] for item in list_of_sutter_investment_items]}
	common_investments = [item for item in set(iqt_portfolio_companies_dict["name"]) & set(sutter_portfolio_companies_dict["name"])]  ## THIS IS AN AMAZING TIME SAVER!!!
	# for item in common_investments:
		#print item
				

	# for item in list_of_iqt_investment_items:
	# 	portfolio_company_name = item["invested_in"]["name"]
	# 	iqt_portfolio_companies["name"].append(portfolio_company_name)
		# portfolio_companies["in-q-tel"].append(portfolio_company_name)

	# for item in list_of_sutter_investment_items:
	# 	portfolio_company_name = item["invested_in"]["name"]
	# 	sutter_portfolio_companies["name"].append(portfolio_company_name)
		# portfolio_companies["sutter_hill"].append(portfolio_company_name)

	# for portfolio_company in iqt_portfolio_companies["name"]:
	# 		if portfolio_company in sutter_portfolio_companies["name"]:
	# 			if portfolio_company not in common_investments["name"]:
	# 				common_investments["name"].append(portfolio_company)
			
	# return common_investments



if __name__ == "__main__":
	main()