I have used Networkx for graph construction.

1.)  For 1st question, you need to run "articles.sh".
      The python file "article.py" is used to give ids to the articles from "articles.tsv" file from A0001 to A4604.


2.) For 2nd question, you need to run "category.sh".
     The python file "category.py" is used to give ids to the categories using BFS from "categories.tsv" from C0001 to C0146.


3.) For 3rd question, you need to run "article_category.sh".
     The python file "article_category.py" is used to assign categories for an article and if any article has no category then assign it the highest category i.e. "subject".
     The output of this code is "article-categories.csv" file.


4.) For 4th question, you need to run "edges.sh".
     The python file "edges.py" is used to show edges between two articles if they exist (their existence is taken only if their value from "shortest-path-distance-matrix.txt" is 1) .


5.) For 5th question, you need to run "graph-components.sh".
     The python file "graph-components.py" is used to find number of components and their nodes,edges,diameter.
     I have constructed undirected graph using Networkx.


6.) For 6th question, you need to run "finished-paths.sh".
     The python file "finished-paths.py" is used to find length of humanpath, length of shortestpath and their ratio for each path.
     We have 2 versions where back click is counted and another where not counted.
      For shortest path, i have constructed directed graph using Networkx.


7.) For 7th question, you need to run "percentage-paths.sh".
     The python file "percentage-paths.py" is used to find the subcases mentioned in question.


8.) For 8th question, you need to run "category-paths.sh".
     The python file "category-paths.py" is used to find no. of paths a category has traversed and no. of times a category has traversed for each finished human path.


9.) For 9th question, you need to run "category-subtree-paths.sh".
     The python file "category-subtree-paths.py" is used to find no. of paths a category and has traversed and no. of times a category  has traversed considering it's parents too for each finished human path .

10.) For 10th question, you need to run "category-pairs.sh".
     The python file "category-pairs.py" is used to find percentage of finished and unfinished paths for every source-destination category pair.


11.) For 11th question, you need to run "category-ratios.sh".
     The python file "category-ratios.py" is used to find the average ratio of humanpath to shortestpath for every source-destination category pair.