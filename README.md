# Take a look at our final report to learn more!

# Recreating Our Results

## Data
All of our data is in the match_data.csv file, which was gotten from http://tennis-data.co.uk/data.php. An explanation of the data can be found at the website as well, along with how the data was collected and what each of the rows mean. 

## Baseline
All of our baseline models can be found in the baseline notebook. It features all of our traditional ML models, along with their results. This can easily be reran on anyone's home system using Conda or any other Jupyter notebook virtual machine. 

## LLM Expirements
All of our expirements were done using the LLM_finetuning Jupyter notebook. There is code for each of our expirements, although some of it is commented out. To recreate these results, you will need your own OpenAI API key, which can be placed in the first line of the notebook. After that, the entire notebook should be able to run. You will also be able to track your progress and get results on the OpenAI portal. Note that running this script will cost money, as finetuning an OpenAI model costs money per token. Therefore, you will need to have some OpenAI credits to recreate our results. Also, there is some randomness in LLMs, so your results may not be the exact same as ours, although they should be relatively close. 
