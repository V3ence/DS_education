import pandas as pd

melb_df = pd.read_csv('C:\IDE\melb_data.csv')
melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)

popular_sellers = melb_df['SellerG'].value_counts().nlargest(49).index

melb_df['SellerG'] = melb_df['SellerG'].apply(lambda x: x if x in popular_sellers else 'other')

a = melb_df[melb_df['SellerG'] == 'Nelson']['Price'].min()
b = melb_df[melb_df['SellerG'] == 'other']['Price'].min()
print (round(a/b , 1))