# Project Name and Description
The perfomance analysis for De-identification and Colenda methods on Clinical texts.
This project runs on Mac, if you want to run on windows, please see the User Guide file for each de-identification tools.

## Dictionary Training User Guide
* Environment: python 2.7
* Working Path: Tools/DictionaryTraining
* Usage:
     * Generate training and test dataset ---- 90%/ 80%/ 70%/ 60%/ 50%... of original:
     ```
     (i)  Open generateTrainFiles.py
     ```
     ```
     (ii) Set percentage & output path you want and Run the file
     ```

     * Establish external dictionary from the training dataset:
     ```
     (i) Open dictionaryTraining.py
     ```
     ```
     (ii) Set the output path for the dictionary and Run the file
     ```
     ```
     (iii) Add the dictionary in the scrubberConfigurationFile --- conf/ScrubberConfiguration.xml
     ```

## Tools User Guide
#### 1. HMS Scrubber
   * Environment: Java 1.8
   * Working Path: Tools/HMS-Scrubber/scrubber-core-2.8
   * Usage      
        * Add dictionary to the Configuration File:
        ```
        (i) Add the dictionary to the conf/scrubberConfigurationFile 
            E.g. conf/ScrubberConfiguration.xml
        ```      
        ```diff
        + Note: dictionary should under the 'conf' folder
        ```
        
        * Scrub on the test dataset:
        ```
        (i)  Open Terminal(Mac) and work under the Working Path
        ```
        ```
        (ii) Run 'sh scrubber.sh <input_file> <config_file>'
             E.g. sh scrubber.sh test.xml conf/ScrubberConfiguration.xml
        ```
        ```
        (iii) System will create a new file under the root folder
              The scrubbed text is in under 'success' Folder.
        ```
        
        * Analyse on the scubbed texts:
        ```
        (i) Open performanceAnalysis/analysis.py
        ```
        ```
        (ii) Set the output path for the results and Run the file.
             It will show the Total scubbed number, True positive number, False positive number for each category
        ```
        ```diff
        + If you want to calculate the Recall, you need to mannualy calculate the total number of the PHI.
        + I use Sublime Text3 and use command+F to find the PHI I interested, 
        + It will show you the total number in the left corner.
        ```
       
#### 2. DE-ID
   * Environment: perl
   * Working Path: Tools/DEID/deid-1.1
   * Usage:       
        * Add dictionary to the Configuration File:
        ```
        (i) Add the dictionary to the lists/scrubberConfigurationFile
            E.g. lists/stripped_hospital.txt
        ```      
        ```diff
        + Note: The easiest way to add dictionary for this method is just copy and paste our 
                dictionary content into that files already existed.             
        ```
        
        * Scrub on the test dataset:
        ```
        (i)  Open Terminal and work under the Working Path
        ```
        ```
        (ii) Run 'perl deid.pl <input_filename> <config_filename>'
             E.g. perl deid.pl inputFile deid.config
        ```
        ```diff
        + Note: filrname should without extension, where extension must be .text            
        ```
        
        ```
        (iii) System will create a new file under the running path --- filename.res,
              which is the scrubbed text.
        ```
        
        * Analyse on the scubbed text:
        ```
        (i) Open performanceAnalysis/analysis.py
        ```
        ```
        (ii) Set the output path for the results and Run the file.
             It will show the Total scubbed number, True positive number, False positive number for each category
        ```

#### 3. PHI-Reducer
   * Environment: python 3.3
   * Working Path: Tools/PHI-Reducer/phi-reducer-0.4.5/phireducer
   * Usage:       
        * Add dictionary to the Configuration File:
        ```
        (i) Add the dictionary file path to the running file phi_reducer.py line 252,
            as showed in the following image 
            ![alt text](https://github.com/OliviaAo/graduate-Ao/tree/master/Documents/References/images/phi_reducer.jpg)
        ```    
        
        * Scrub on the test dataset:
        ```
        (i)  Open Terminal and work under the Working Path
        ```
        ```
        (ii) Run 'python3 phi_reducer.py'
        ```
        ```diff
        + Note: Need to create two folders <input_test> and <output_test>. 
                Put all of the text you want to scrub into the <input_test> folder         
        ```
        
        ```
        (iii) System will generate all of the corresponding scrubbed texts into the <output_test> folder.
        ```
        
        * Analyse on the scubbed text:
        ```
        (i) Open performanceAnalysis/analysis.py
        ```
        ```
        (ii) Set the output path for the results and Run the file.
             It will show the Total scubbed number, True positive number, False positive number for each category
        ```


#### 4. MIST

## Articles:
- [Automatic de-identification of textual documents in the electronic health record: a review of recent research](https://github.com/OliviaAo/graduate-Ao/tree/master/Documents/References/1471-2288-1070.pdf)

## Author
* **Ao Li** 

## Acknowledgements
* **Karin Verspoor** - *Supervisor*
* **Shuangshuang Wang** - *Initial work*


