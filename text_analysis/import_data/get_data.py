from google_play_scraper import app, Sort, reviews, reviews_all

class GooglePlayData:
    """A class for extracting data from google play reviews using play-scraper 

       :param app_id: id from the app
       :ivar data: data extract from the api 
    """
    def __init__(self, app_id):
        self.app_id = app_id
        self.data = []

    def get_results(self, lang, country, count_per_page, limit=10):
        # Result of reviews is a list of dictionaries
        results, continuation_token = reviews(self.app_id, lang, country, sort=Sort.MOST_RELEVANT, count=count_per_page)
        l = 1
        _ = continuation_token

        while l < limit:
            result, _ = reviews(self.app_id, lang, country, sort = Sort.MOST_RELEVANT, count = count_per_page, 
            continuation_token = _)
            results += result
            l += 1
    
        # Create country and language variable   
        len_results = len(results)    
        for i in range(len_results):
            results[i]['country'] = country
            results[i]['language'] = lang
    
        self.data += results
    
    