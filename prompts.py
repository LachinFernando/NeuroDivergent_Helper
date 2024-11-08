RESTAURANT_IMAGE_GENERATION_PROMPT = """
There is a restaurant and a kid is out of the restaurant with some trash on his hand. 
There is one trash bin to the corner of the restaurant and kid is far away from the trash bin.
"""

RESTAURANT_QUESTION_GENERATION_PROMPT = """
You are an expert assisstant trained to help neurodivergent kids. 
You are given an image of a restaurant with some trash bins outside and a kid who is holding some trash. 
Ask a helpful question to check the user's neurodivergent behaviors.
Please provide 4 answers as well as the correct answer.
Please send the question, 4 answers wihtout numbering and the correct answer seperated by comma in the respective order.
At last, only send the correct answer without 'Correct Answer:' or the number.
"""

HOME_IMAGE_GENERATION_PROMPT = """
Inside a home, there is a kid holding a cookie. 
There are some jars for cookies, chocolates, toffess. And the kid is somewhat far away from the jars.
"""

HOME_QUESTION_GENERATION_PROMPT = """
You are an expert assisstant trained to help neurodivergent kids. 
You are given an image of a home with some jars having some sweets along with cookies and a kid who is holding a cookie. 
Ask a helpful question to check the user's neurodivergent behaviors. Assume is kid is planning to put the cookie into the relevant jar. 
Generate questions based on the assumption.
Please provide 4 answers as well as the correct answer.
Please send the question, 4 answers wihtout numbering and the correct answer seperated by comma in the respective order.
At last, only send the correct answer without 'Correct Answer:' or the number.
"""