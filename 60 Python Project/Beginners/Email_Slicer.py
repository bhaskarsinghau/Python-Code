'''
Email Slicer with Python

To create an email slicer with Python, our task is to write a program that can retrieve the username and the
domain name of the email. For example, look at the image below which shows the domain and username of 
“support@thecleverprogrammer.com”:

So we need to divide the email into two strings using ‘@’ as the separator. Let’s see how to separate the email
and domain name with Python:

''' 
email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)

'''
The code above is very simple and easy to understand. We take user input and use the strip function at the 
same time to remove white space if any. Then we are finding the index of ‘@’ symbol of the user input. 
Then we store the index into a variable known as domain_name to split the email into two parts; the user name
and the domain.

Finally, we are just formatting to print the output. The above code can be enhanced with more ideas depending 
on your needs. As a beginner, you must try these types of programs to improve your coding skills. In the 
long run, it will also help you build your algorithms and increase your ability to think logically.
'''

