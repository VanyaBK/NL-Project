 
informationRetrieval_LSI.py - Implements the Latent Semantic Indexing Model
informationRetrieval_VSM.py - Implements the Vector Space Model
informationRetrieval_LDA.py - Implements the Latent Dirichlet Allocation Model
informationRetrieval_Word2Vec.py - Implements the Word2Vec model 
				   Download link for google word2vec embeddings - https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit
Change the name of the above files whose model you want to implemt to informationRetrieval.py. Then follow the below steps :

To test the code, run main.py with the appropriate arguments.
Usage: main.py [-custom] [-dataset DATASET FOLDER] [-out_folder OUTPUT FOLDER]
               [-segmenter SEGMENTER TYPE (naive|punkt)] [-tokenizer TOKENIZER TYPE (naive|ptb)] 

When the -custom flag is passed, the system will take a query from the user as input. For example:
> python main.py -custom
> Enter query below
> Papers on Aerodynamics
This will print the IDs of the five most relevant documents to the query to standard output.

When the flag is not passed, all the queries in the Cranfield dataset are considered and precision@k, recall@k, f-score@k, nDCG@k and the Mean Average Precision are computed.

In both the cases, *queries.txt files and *docs.txt files will be generated in the OUTPUT FOLDER after each stage of preprocessing of the documents and queries.