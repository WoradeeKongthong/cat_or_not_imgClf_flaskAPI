My transfer learning ipython notebook and its dataset for image classification (cat-or-not) are stored in model folder.  
You can check it up to see how to get the final_model.h5 file.  

# How to use this "cat-or-not" image classification model flask API
1. create your virtual environment
2. download or clone my project
3. install the packages in requirements.txt by going to your terminal and type the command `$ pip install -r requirements.txt`
4. start using api with `python app.py`
5. now you can use my api. 

I suggest you use the api through Postman application.  
# Postman
1. send a GET request to http://0.0.0.0:8000/ to go to the home page
2. send a POST request to http://0.0.0.0:8000/predict along with your picture file to get the prediction.
	- in Body tab
	- select form-data
	- specify KEY as file
	- at the drop down in KEY, select File
	- specify VALUE by selecting file as you want
	- then hit Send button and see the prediction in the Response

# How to containerize the model
1. create a docker image named as you want by running the command `$ docker build -t <imageName> .`
2. create a container by running the image, `$ docker run -p 8000:8000 <imageName>`
3. check the IPAddress of your running container, `$ docker inspect <containerID> | grep IP`
4. use the API in Postman app as before but change the url to the IPAddress that you get from step 3 and use the same port (8000), such as http://172.17.0.2:8000. 

# My Docker image 
You can use my docker image by running the command `$ docker pull woradee/cat_or_not_flaskapi:simple`
