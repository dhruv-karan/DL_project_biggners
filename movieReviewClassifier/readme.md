The folder contains the Ann classifier on IMDB movie review

<h2> highlight </h2>
<ul>
<li>The data download is stored in code for like : 23,45,6,78(belive me this is review)  </li>
<li> The to decrypt the code u download the word dictinort which contain the word and thier coressponding code</li>
<pre>
                     ----------------------- Example------------------------
                     ('i':1,'am':2,"dhruv":3,"karan":4)------this is dict
                     now sentence can be like either: 4,2,1,3 i.e karan am i dhruv
                     most logical would be like : 1,2,3,4 i.e i am dhruv karan
</pre>
<li>After getting the integer list we, converted it into binary matrix using numpy</li>
<li>Defining the model: 
<li> It has 2 hidden layer </li>
<li> It ha 16 units perlayer </li> </li>
<li>compiling the model, u should go around and play with loss ad optimiser which present in market    </li>
<li> Fit the model (play with epoch and see the accuracy on validation set ) when it is ten the model is overfitted </li>
<li> Plot diagram will be updaing soon </li>
</ul>