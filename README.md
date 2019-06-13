# Mail_extraction-machine

In this project, i connect two html pages with the help of Python(Flask libarary).Make sure that your .html file should be present inside a templates folder and the folder is must be kept inside the project folder this is because when you are going to deploy a flask app the compiler will find your .html files inside a templates folder.



* requirements.txt


You may use Python for others projects besides web-development.

Your projects might have different versions of Python installed, different dependencies and packages.

We use virtualenv to create an isolated environment for your Python project. This means that each project can have its own dependencies regardless of what dependencies every other project has.

soo to provide all the need or dependencies which our program needs is fulfill by the requirements.txt file.



* app.yaml



When I first attempted to deploy my simple web app, my deployment never worked. After many attempts, I learned that we needed to include the SSL library.

The SSL Library allows us to create secure connections between the client and server. Every time the user goes to our website they will need to connect to a server run by Google App Engine. We need to create a secure connection for this. (I recently learned this, so if you have a suggestions for this let me know!)


soo that's why i create a app.yaml Reference. You configure your App Engine app's settings in the app.yaml file. This file specifies how URL paths correspond to request handlers and static files. The app.yaml file also contains information about your app's code, such as the runtime and the latest version identifier.


