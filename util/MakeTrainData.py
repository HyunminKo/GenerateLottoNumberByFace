import pandas as pd

sheetName = 'lotto_winning_numbers' 
data = pd.read_excel('lotto_winning_numbers.xlsx', sheet_name = sheetName,skiprows=1)
df = pd.DataFrame(data)
df.columns=['DrawNumber','Date','TotalOfWinning','WinningPrize','W1','W2','W3','W4','W5','W6','Bonus']

with open('data/WinningNumberByDraw.txt','w') as f:
    for index, row in df.iterrows():
        temp = []
        temp.append(str(row['W1']))
        temp.append(str(row['W2']))
        temp.append(str(row['W3']))
        temp.append(str(row['W4']))
        temp.append(str(row['W5']))
        temp.append(str(row['W6']))
        tempStr = ','.join(temp)
        print(row['DrawNumber'],tempStr)
        f.write('{} {}\n'.format(row['DrawNumber'],tempStr))
