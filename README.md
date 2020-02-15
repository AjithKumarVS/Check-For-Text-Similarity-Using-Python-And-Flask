# Check For Text Similarity
 
## Problem Statement
Objective is to write a program that takes as input two texts and uses a metric to determine how similar they are. Documents that are exactly the same should get a score of 1 and documents that don't have any words in common should get a score of 0. In addition to this, package this application as a web service that performs the comparison in response to a POST request containing the two texts in the body of the payload. (No scikit-learn, NLTK, spacy)

## Sample Texts:
- Sample 1
The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you.
- Sample 2
The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you.
- Sample 3
We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way.