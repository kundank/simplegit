def stopword(word):
        sw_list=['a','about', 'above', 'across', 'after', 'again', 'against', 'along', 'already','also','although', 'always', 'among', 'an', 'and', 'another', 'any', 'anybody'
                 'anyone', 'anything', 'anywhere', 'are', 'area', 'areas', 'around', 'as', 'ask','asked', 'asking', 'asks', 'at', 'away', 'back', 'backed', 'backing', 'backs'
                 'be', 'became', 'because', 'become', 'becomes', 'been', 'began', 'behind', 'being', 'beings', 'between', 'but', 'by', 'came', 'can', 'cannot', 'case', 'cases'
                 ,'me', 'could', 'did', 'do', 'does', 'done', 'during', 'each', 'early','either', 'even', 'evenly', 'everybody', 'everyone', 'fact', 'facts', 'far', 'felt',
                 'find', 'finds', 'for', 'from', 'further', 'furthered', 'furthering', 'furthers', 'gave', 'general', 'generally', 'get', 'gets', 'give', 'given', 'gives', 'go',
                 'going', 'got', 'group', 'grouped', 'grouping', 'groups', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'herself', 'himself', 'his', 'how', 'however', 'i',
                 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'just', 'keep', 'keeps', 'kind', 'knew', 'know', 'known', 'knows', 'last', 'later', 'let', 'man', 'may', 'me',
                 'member', 'members', 'men','mon,','mar', 'might', 'mr', 'mrs', 'my', 'myself', 'nobody', 'not', 'now', 'number', 'numbers', 'of','off', 'often', 'once','on','open', 'opened',
                 'opening', 'opens', 'or', 'order', 'ordered', 'ordering', 'orders', 'other', 'others', 'out', 'over', 'part', 'parted', 'parting', 'parts', 'per', 'perhaps', 
                 'put', 'puts','posted:','posted', 'said', 'same', 'saw', 'say', 'says', 'see', 'seem', 'seemed', 'seeming', 'seems', 'sees', 'several', 'shall', 'she', 'should', 'show', 'showed',
                 'shows', 'side', 'sides', 'since', 'so', 'some','subscribe','rss', 'take', 'taken', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'therefore', 'these', 'they'
                 , 'thing', 'things', 'think', 'thinks', 'this', 'those', 'though', 'thought', 'thoughts', 'through', 'thus', 'to', 'together', 'too', 'took', 'toward', 'turn',
                 'turned', 'turning', 'turns', 'under', 'until', 'up', 'upon', 'us', 'was', 'went','we','were', 'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'whole'
                 , 'whose', 'why', 'will', 'with', 'without', 'would', ' ','.','?','!','1 comment','','-','1','2009','comment','comments','yet','apr']
        if sw_list.__contains__(word):
                return 0
        else:
                return 1

