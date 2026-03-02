import pandas as pd
if __name__ == "__main__":
    df = pd.read_csv("clean.csv")
    query_df = pd.read_csv("query.csv")

    out = []
    for idx, row in query_df.iterrows():

        min_dist = 0
        max_dist = 100
        out_dict = {}
        center_x = row.iloc[0]
        center_y = row.iloc[1]

        while max_dist > min_dist:
            middle_dist = (min_dist + max_dist)/2
            middle_df = df[(df['x'].between(center_x - middle_dist, center_x + middle_dist)) &
               (df['y'].between(center_y - middle_dist, center_y + middle_dist))]
            if len(middle_df) == 3:
                diffs = middle_df[["x", "y"]] - row
                squares = diffs**2
                dists = squares.sum(axis=1) ** 0.5
                sorted = dists.sort_values()
                for i in range(3):
                    ith_closest_idx = sorted.index[i]
                    out_dict[f"top{i+1}_title"] = df.loc[ith_closest_idx, "title"]
                    out_dict[f"top{i+1}_id"] = df.loc[ith_closest_idx, "imdb_id"]
                out.append(out_dict)
                break
            elif len(middle_df) > 3:
                max_dist = middle_dist
            else:
                min_dist = middle_dist
    
    pd.DataFrame(out).to_csv("out.csv", index=False)
    print("Rows written:", len(out))
    print("Final dataframe:")
    print(pd.DataFrame(out))
    