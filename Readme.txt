
Scilab Web Interface (Milestone 5)

Requirements:

1. Python 3.8
2. scilab 5.5.0
3. Add scilab to your path:

    C:\Program Files (x86)\scilab-5.5.0\bin

    C:\Program Files (x86)\scilab-5.5.0\modules

4. scilab2py library : pip install scilab2py
5. scipy library:      pip install scipy
6. Flask :             pip install flask

Installation :

Step 1:
  Activate the virtual Envionment:
   1.After Ectracting zip file you will get scilab_flask folder. open CMD in this location.
   2.Navigate to "venv/scripts" that is "cd venv/Scripts"
   3.Type "activate" and press enter.
   
Step 2:
  Run the application:
   1.Now the environment will be activated after that navigate back to main folder.
   2.Now run the command "python app.py". 
   3.Now your server will run at "http://127.0.0.1:5000/"
   4.Visit "http://127.0.0.1:5000/" in your web browser and You will see the plot basic Graph button click on it you will get the output window.

Note: we are using flask(https://flask.palletsprojects.com/en/1.1.x/) open source framework for the entire project because by using the pyramid framework we were unable to run the development server. 
      we have saved the error screenshots to pyramid_error folder inside the project folder. 
      flask is also the same framework like pyramid and also it has more better features as compared to pyramid and also was more ligthweigth and fast.
      Mainly flask is compatible with scilab2py library.
      Hence due to the above reasons flask becomes our only choice for the further development of the project.

Also saved the output screenshots to the output folder inside the project folder.

Milestone 1 & 2:
   In this Milestone we have demonstrated how to connect scilab 5.5.0 to a web server using flask which is a python web framework and to access plotting functions of scilab using sci2py library.

Milestone 3:
   In this milestone we have saved the plot in .png extension using xs2png() function of scilab inside Plot_Images folder with unique randomly generated file name.

Milestone 4:
  Fetched the generated plot image and displayed it in the WebPage.

Milestone 5:
  Provide user input to the interface and plotting of 3d plots and other scilab commands and also the ability to execute multiple commands and get the output.


Video Screen cast demonstration:
https://drive.google.com/file/d/1BTrlElNs6P8ahrwkQkh5IGBEErlg0u5y/view?usp=sharing
 

      







   