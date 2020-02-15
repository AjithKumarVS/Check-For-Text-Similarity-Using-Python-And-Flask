def similarity(str1, str2):
    symbols = "!\"#$%&()*+-./:;<=>?@[\],^_`{|}~"

    stop_words=["i", "me", "my", "myself", "we", "we'll", "our", "ours", "ourselves", "the", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "did", "doing", "a", "an", "and", "if", "or", "for", "to", "from", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "only", "own"]

    word_sp1=str1.split()
    word_split1=""
    for word in word_sp1:
        if len(word)>1:
            if word.lower() not in stop_words:
                word_split1=word_split1+ " " +word.lower()
    for i in symbols:
        word_split1=word_split1.replace(i," ")
    word_split1=word_split1.split()

    word_sp2=str2.split()
    word_split2=""
    for word in word_sp2:
        if len(word)>1:
            if word.lower() not in stop_words:
                word_split2=word_split2+ " " +word.lower()
    for i in symbols:
        word_split2=word_split2.replace(i," ")
    word_split2=word_split2.split()

    str1_two=list(map(' '.join, zip(word_split1[:-1], word_split1[1:])))
    str2_two=list(map(' '.join, zip(word_split2[:-1], word_split2[1:])))

    up_s1=set(str1_two)
    up_s2=set(str2_two)
    
    x=up_s1.intersection(up_s2)
    similarity12=0
    similarity12=(len(x)/(len(up_s1)+len(up_s2)-len(x)))

    return similarity12