# Project Name
The perfomance analysis for De-identification and Colenda methods on Clinical texts.

## Tools User Guide
#### 1. HMS Scrubber
   * Environment: Java 1.8, python 2.7, Apple MacBook
   * Usage
        * Generate training and test dataset ---- 90%/ 80%/ 70%/ 60%/ 50% of original:
        
        ```
        (i)  Open process/generateTrainFiles.py
        ```

        ```
        (ii) Set percentage & output path you want and Run the file
        ```
        
        * Establish external dictionary from the training dataset:
        ```
        (i) Open process/dictionaryTraining.py
        ```
        ```
        (ii) Set the output path for the dictionary and Run the file
        ```
        ```
        (iii) Add the dictionary in the scrubberConfigurationFile --- conf/ScrubberConfiguration.xml
        ```
        ```diff
        + Note: dictionary should under the 'conf' folder
        ```
        
        * Scrub on the test dataset:
        ```
        (i)  Open Terminal and work under scrubber folder
        ```
        ```
        (ii) Run 'sh scrubber.sh inputFile scrubberConfigurationFile'
             Example: sh scrubber.sh test.xml conf/ScrubberConfiguration.xml
        ```
        ```
        (iii) System will create a new file under the root folder
              The scrubbed text is in under 'success' Folder.
        ```
        
        * Analyse on the scubbed text:
        ```
        (i) Open process/analysis.py
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
#### 3. PHI-Reducer
#### 4. MIST

## Articles:
- [Automatic de-identification of textual documents in the electronic health record: a review of recent research](https://github.com/OliviaAo/graduate-Ao/tree/master/Documents/References/1471-2288-1070.pdf)

## Author
* **Ao Li** 

## Acknowledgements
* **Karin Verspoor** - *Supervisor*
* **Shuangshuang Wang** - *Initial work*


