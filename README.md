# Voice_Blue

Steps to Run the Smart Assistant on a Local Device:

	1. Copy all the Files to a folder (All files to be present in the same folder)
	2. Open the current Folder with VS Code or any Python Editors (Recommended VS Code)
	3. Run the following command in the Terminal of the editor. (To install required modules)
		" pip install -r requirements.txt " 
	4. Create a file Keys.py and add the following format.

		```API_KEY = 'xx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
		   APP_ID = 'XXXXXX-XXXXXXXXXX'
		   MAIL = "xxxxxxxxx@gmail.com"
		   PASS = "xxxxxxxxx" ```

	5. Get the API keys from respective Links and add them to keys.py(As above format).

		```API_KEY link -->  https://platform.openai.com/account/api-keys
		   APP_ID  link -->  https://developer.wolframalpha.com/portal/myapps/
		   MAIL --> Your Personal Email.
		   PASS --> Password of your Email.```

	6. Now Run the command to run the main file 
		" python main.py "
	7. The popped-up Python GUI is the Smart Assistant.
	8. To Terminate the GUI Use the close Button on GIU's Top right corner (OR)
	   Press " CTRL+C " to terminate the file running.
