import pandas as pd
df2 = pd.read_excel('C:/Users/Administrator/Desktop/q.xlsx')
columns = df2.columns.values.tolist()
df3 = pd.DataFrame()
length = len(columns)
df2["diagnose"] = "No"
df2["Mi1"] = 0
df2["Mi2"] = 0
df2["Mi3"] = 0
df2["Mo1"] = 0
df2["Mo2"] = 0
df2["S1"] = 0
df2["S2"] = 0
df2["AL"] = 0
df2["PD"] = 0
df2.fillna(0, inplace=True)
count = 0
while count <= 27:
    print(count)
    for i in range(6):
        df2.loc[df2[columns[count * 12 + i]] == 99, columns[count * 12 + i]] = 0
        df2.loc[df2[columns[count * 12 + i + 6]] == 99, columns[count * 12 + i + 6]] = 0
        df2["AL"] = df2.apply(lambda x: x["AL"] + x[columns[count * 12 + i + 6]], axis=1)
        df2["PD"] = df2.apply(lambda x: x["PD"] + x[columns[count * 12 + i]], axis=1)
        df2.loc[df2[columns[count * 12 + i]] >= 5, 'Mi3'] += 1
        if i == 0 or i == 2 or i == 3 or i == 5:
            df2.loc[(df2[columns[count * 12 + i + 6]] >= 3) & (df2[columns[count * 12 + i + 6]] < 4), 'Mi1'] += 1
            df2.loc[df2[columns[count * 12 + i]] >= 5, 'S2'] += 1
    df2.loc[(df2[columns[count * 12]] >= 4) | (df2[columns[count * 12 + 2]] >= 4) | (df2[columns[count * 12 + 3]] >= 4) | (df2[columns[count * 12 +5]] >= 4), 'Mi2'] += 1
    df2.loc[((df2[columns[count * 12 + 6]] >= 4) & (df2[columns[count * 12 + 6]] < 6)) | ((df2[columns[count * 12 + 2 + 6]] >= 4) & (df2[columns[count * 12 + 2 + 6]] < 6))
            | ((df2[columns[count * 12 + 3 + 6]] >= 4) & (df2[columns[count * 12 + 3 + 6]] < 6)) | ((df2[columns[count * 12 + 5 + 6]] >= 4) & (df2[columns[count * 12 + 5 + 6]] < 6)), 'Mo1'] += 1
    df2.loc[(df2[columns[count * 12]] >= 5) | (df2[columns[count * 12 + 2]] >= 5) | (df2[columns[count * 12 + 3]] >= 5) | (df2[columns[count * 12 + 5]] >= 5), 'Mo2'] += 1
    df2.loc[(df2[columns[count * 12 + 6]] >= 6) | (df2[columns[count * 12 + 2 + 6]] >= 6) | (df2[columns[count * 12 + 3 + 6]] >= 6) | (df2[columns[count * 12 + 5 + 6]] >= 6), 'S1'] += 1
    count += 1
df2.loc[(df2['Mi3'] >= 1) | ((df2['Mi1'] >= 2) & (df2['Mi2'] >= 2)), 'diagnose'] = 'Mild'
df2.loc[(df2['Mo1'] >= 2) | (df2['Mo2'] >= 2), 'diagnose'] = 'Moderate'
df2.loc[(df2['S1'] >= 2) & (df2['S2'] >= 1), 'diagnose'] = 'Severe'
df3['diagnose'] = df2['diagnose']
df3['AL'] = df2['AL'].map(lambda x:x/168)
df3['PD'] = df2['PD'].map(lambda x:x/168)

df3.to_excel('C:/Users/Administrator/Desktop/result.xlsx', index=False, header=True)
