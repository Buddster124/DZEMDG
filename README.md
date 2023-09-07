# DZEMDG
# Description
  This python script will automatically create the data for the Days Expansion Market / Trader mod.

#Requirements
- Python

# How to use
 1. Create a file called ```Input.txt```
 2. Fill ```Input.txt``` With all the class names for the mod you are trying to add. The Format Has to be as follows.
 ```
 Item 1
 Item 2
 Item 3
 ```
 3. Run the following command in the command line ```python DZEMDG.py```
 4. The Script Will Ask for the ```input path```, input the full path of the file we created earlyer (```Input.txt```).
 5. The Script Will Ask for the ```output path```, input the path you would like it to save the file to.
 6. Wait for the script to finish.
 7. The script will generate a file called ```Output.txt```, In the directory you specified in ```step 5```.
 Example Output of ```Output.txt```
 ```
          {
            "ClassName": "Item_1",
            "MaxPriceThreshold": 20,
            "MinPriceThreshold": 10,
            "SellPricePercent": -1.0,
            "MaxStockThreshold": 100,
            "MinStockThreshold": 1,
            "QuantityPercent": -1,
            "SpawnAttachments": [],
            "Variants": []
        },
```  
8. Open ```Output.txt``` And Navigate to the last line, Remove the ```,``` On the last entry.
9. Copy all of the data from ```output.txt``` to the proper ```Market.json``` file.

#Notes
- Important: When installing python make sure you check the box to install python to PATH, If you do not do this you will run into errors when trying to run the script.

- Video Tutorial Here (Will Make an updated video soon): https://youtu.be/vG36CnhzU7Y
