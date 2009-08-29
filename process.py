import paragraph 
import sentence
from stopwords import *
from search import *
import re

def Topic(blog):
        return(blog[0])


def Author(blog):

        probables=[]
        regex=re.compile('posted by .* on')

        for sentence in blog:
                if(re.search (regex,sentence)):
                        probables.append( re.search(regex,sentence).group()[10:-2] )

        return probables[(len(probables)-1)]


def Comments(blog):

        probables=[]
        regex=re.compile('[0-9]{1,3} comment?')

        for sentence in blog:
                if(re.search (regex,sentence)):
                        probables.append( re.search(regex,sentence).group()[0:-8] )
        
        if (len(probables)==0 ):
                probables.append('0')

        return probables[(len(probables)-1)]



def BlogAsses(bloginfo,blogs):

        print '\n\n\n.....................ANALYSIS OF COMPANY MEMBERS BLOGS.........................\n\n'
        print '\n----------------------  ASSESMENT OF THE BLOGGERS  ----------------------------\n'
        print 'AUTHORS  COMMENTS  ..TOPIC OF THE BLOG..'
        for i in range(0,len(bloginfo)):
                print  bloginfo[i][1],'\t ',bloginfo[i][2],'\t   ',bloginfo[i][0]

        print'\n\n-----------------------Result Analysis----------------------------------------\n'
        i=0
        max_cmnt=0
        dic={}
        for blog in bloginfo:
                
                if (max_cmnt < blog[2]):
                                max_cmnt=blog[2]
                                loc=i
                if dic.__contains__(blog[1]):
                        dic[blog[1]]=dic[blog[1]]+1
                else:
                        dic[blog[1]]=1
                i=i+1
        cnt=0              
        for keys in dic:
                if (dic[keys] > cnt):
                        cnt=dic[keys]
                        key=keys
                
                        
        print '* BLOGGER WHO RECEIVED MAXIMUM COMMENTS----->', bloginfo[loc][1]
        print '\n* MAXIMUM NUMBER OF BLOGS POSTED BY -------->',key
        print '\n* TOPIC OF MOST COMMENTED BLOG--------->',bloginfo[loc][0]
        
        
        	

def Bigrams(ImpWordsBlogs):

        Bigram=[]       #Bigram --> [   '['[bigrams of sents1]','[bigrams sents 2]',...]'  ,  '['[bgrms sents1]','[bgrms sents2]'....]'  ,  ......]
        for blog in ImpWordsBlogs:
                bigram_blog=[]
                for sents in blog:
                        bigram_sent=[]
                        words=sents.split()
                        for i in range(0,len(words)-1):
                                bigram_sent.append(words[i]+' '+words[i+1])
                        bigram_blog.append(bigram_sent)
                Bigram.append(bigram_blog)      #end of procedure to create Bigram for all blogs....

        
        Priority=[]
       

        for blg in Bigram:
                priority=[]
                for i in range(0,len(blg)):     #len(blog)=no. of sentences in one blog.
                        prt=0
                        for j in range(0,len(blg[i])):  #len(blog[i])=no. of bigram in one sentence.
                                for k in range(0,len(blg)):
                                        if (blg[k].__contains__(blg[i][j]) and (k != i) ):
                                                prt=prt+2
                        priority.append(prt)
                Priority.append(priority)
        return Priority



def Unigrams(ImpWordsBlogs):
        Freq=[]
        for blg in ImpWordsBlogs:
                freq={}
                for sents in blg:
                        wrds=sents.split()
                        for wrd in wrds:
                                        for sent in blg:
                                                if sent.__contains__(wrd):
                                                        if freq.__contains__(wrd):
                                                                freq[wrd]=int(freq[wrd])+int(1)
                                                        else:
                                                                freq[wrd]=int(1)
                                                                
               
                Freq.append(freq)                
       
        
        Unipr=[]
        i=0
        for blg in ImpWordsBlogs:
                unipr=[]
                for sents in blg:                                
                        wrds=sents.split()
                        temp=0
                        for m in range(0,len(wrds)):
                                z=Freq[i]       
                                temp=temp+int(z[wrds[m]])
                        unipr.append(temp)
                i=i+1                             
                Unipr.append(unipr)
                    
        return (Unipr)


def PrintSummary(BlogSents,Priority):
        Index=[]
        for i in range(0,len(Priority)):
                temp1=0
                temp2=0
                for j in range(0,len(Priority[i])):
                        if (temp1<Priority[i][j]):
                                        temp1=Priority[i][j]
                                        loc1=j
                    
                Index.append(loc1)
        
        print '\n\n\n-------------BLOGS AND THEIR MOST WEIGHTED SENTENCES(SUMMARY)------------------\n'
        print
        for n in range(0,len(Index)):
                print 'BLOG -',(n+1)
                print BlogSents[n][0]
                print BlogSents[n][Index[n]]
                print
        return(Index)

        
def SummaryEval(BlogSents):
        
        #BlogSents -->[ '[blog1 sentences]','[blog2 sentences]',......] . 
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
                
               
        
        BiPriority=Bigrams(ImpWordsBlogs)
        UniPriority=Unigrams(ImpWordsBlogs)
        Priority=[]
        for i in range(0,len(BiPriority)):
                priority=[]
                for j in range(0,len(BiPriority[i])-1):
                        l= UniPriority[i][j]
                        m= BiPriority[i][j]
                        priority.append(0.35*l+0.65*m)
                Priority.append(priority)
        print
        print
        IndexList=PrintSummary(BlogSents,Priority) 
        return(IndexList)
        
        
def BlogInfo(blogs):
        bloginfo=[]
        for blog in blogs:
                info=[]
                info.append(Topic(blog))
                info.append(Author(blog))
                info.append(Comments(blog))
                bloginfo.append(info)
        
        return bloginfo


if __name__=="__main__":
	
	paras=paragraph.get_para('asgit.txt') #paras --> ['blog1 as string','blog2 as string',....]. 
	blogs=[]                                #blogs -->[ '[blog1 sentences]','[blog2 sentences]',......] .
        
	for blog in paras:
		blogs.append(sentence.get_sentence(blog))

        bloginfo=[]
        bloginfo=BlogInfo(blogs)
        BlogAsses(bloginfo,blogs)
        IndexList=SummaryEval(blogs)
        SearchResult(paras,blogs)
        
                        
        	

