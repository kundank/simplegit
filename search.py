from stopwords import *

def ImpWords(BlogSents):
        ImpWordsBlogs=[]                #ImpWordsBlogs -->[ '[blog1 sentences without stopwords]', .....]                                                
        for blog in BlogSents:
                ImpWord=[]
                for sentence in blog:
                        strg=' '
                        SentWord=[]
                        SentWord=sentence.split()
                        for i in range(0,(len(SentWord))):
                                if (stopword(SentWord[i])):                                       
                                       strg=strg+' '+SentWord[i]                                  
                        ImpWord.append(strg)                             
                ImpWordsBlogs.append(ImpWord)   #end of procedure to create ImpWordsBlogs.
        
        return  ImpWord       


def Bigram(ImpWords):
    
    for blog in ImpWords:
                bigram_blog=[]
                for sents in blog:
                        bigram_sent=[]
                        words=sents.split()
                        for i in range(0,len(words)-1):
                                bigram_sent.append(words[i]+' '+words[i+1])
                        bigram_blog.append(bigram_sent)     #end of procedure to create Bigram for all blogs....

    return bigram_blog          
    
def SearchResult(paras,blogs):
    FreqDic={}
    ImpWordsBlog=[]
    for blog in blogs:
            for sentences in blog:
                ImpWordsBlog=[ImpWords([[sentences]])]
                BlogBigram=Bigram(ImpWordsBlog)
                for bigram in BlogBigram[0]:
                        if bigram not in FreqDic:
                            FreqDic[bigram] = 1
                        else:
                            FreqDic[bigram] += 1
   
    res = []
    for key, value in FreqDic.items():
        res.append((value, key))
    print '\n\n----------LIST OF MOST DISCUSSED TERMS-------------\n'
    res.sort()
    for k in range(0,15):
            print res[len(res)-k-1]
            
                        

    quest=[[ raw_input('\n\nENTER TOPIC OR PHRASE TO BE SEARCHED IN BLOGS... ')]]
    ImpWordsQuest=[ImpWords(quest)]
   
    if(len(ImpWordsQuest[0][0].split())>1):
        QuestBigram=Bigram(ImpWordsQuest)

        
        
        Relevent=[]
        ImpWordsBlog=[]
        for blog in blogs:
            for sentences in blog:
                ImpWordsBlog=[ImpWords([[sentences]])]
                BlogBigram=Bigram(ImpWordsBlog)
                for parses in QuestBigram[0]:
                    if BlogBigram[0].__contains__(parses):
                        Relevent.append(sentences)
        print '\n\n--------BIGRAM SEARCH RESULTS( MORE SPECIFIC )----------\n\n'                
        for i in range(0,len(Relevent)):
            print Relevent[i]
            print
      
    questwords=quest[0][0].split()
    
    relevent=[]
    for blog in blogs:
            for sentences in blog:
                AppendSignal=0
                ImpWordsBlog=ImpWords([[sentences]])
                BlogWords=ImpWordsBlog [0].split()       
                for word in questwords:
                        if (BlogWords.__contains__(word) and AppendSignal==0):                               
                                relevent.append(sentences)
                                AppendSignal=1

            #print ImpWordsBlog [0].split()       
    print '\n\n------------UNIGRAM SEARCH RESULTS----------\n\n'
    for i in range(0,len(relevent)):
            print relevent[i]
            print
    

                
    
            
