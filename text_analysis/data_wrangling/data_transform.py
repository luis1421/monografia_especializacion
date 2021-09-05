import pandas as pd

class Transform:
    def __init__(self, data):
        self.data = data
        self.sankey = None

    def get_sankey(self, index_by, order_by, values, n_t=2, n_c=3):
        self.data['order'] = self.data.sort_values([index_by, order_by])\
                                    .groupby([index_by]).cumcount() + 1
        
        top_values =  list(self.data[values].value_counts()[:n_c].index)

        df_sankey = self.data.copy()
        df_sankey = df_sankey.loc[df_sankey[values].isin(top_values)]

        limit = [i + 1 for i in range(n_t)]
        col_sub = ['Path' + str(i+1) for i in range(n_t)]
        temp = df_sankey
        temp['order_name'] = temp['order'].apply(lambda x: 'Path' + str(x))
        temp = temp.pivot(index=index_by, columns='order_name', values=values)
        temp = temp[col_sub]

        sankey = pd.DataFrame({'from':[], 'to':[], 'weight':[]})
        for i in range(1,len(temp.columns)):
            df_cache = temp.groupby(temp.columns[[i-1,i]].to_list()).size().reset_index()
            df_cache.columns = ['from', 'to', 'weight']
            df_cache['from'] =  df_cache['from'] + ' ' + str(i)
            df_cache['to'] =  df_cache['to'] + ' ' + str(i+1)
            sankey = sankey.append(df_cache)
        self.sankey = sankey
