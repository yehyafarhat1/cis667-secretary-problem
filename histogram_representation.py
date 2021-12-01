import json
import matplotlib.pyplot as plt
import pandas as pd
import algorithms.domain_impl
import numpy as np


class HistogramRepresentation():
    def __init__(self):
        pass

    def histogram(self, recorder_list):
        list_finals = []
        for recorder in recorder_list:
            list_records = recorder.get_record_list()  # one recorder, one game
            print(
                'Size {size}   ----------------------------------------------------------------------------'.format(
                    size=algorithms.domain_impl.get_size_str(list_records[0]["size"])))
            print(
                '========================================================================================================')

            # print("Current result: MODEL:{model_score} ; DOMAIN:{domain_score} "
            #       "\t\tsize: {size}, game: {game}, index: {round}, "
            #       "value: {val}, best_value: {best_val}".format(model_score=self.model_score,
            #                                                     domain_score=self.domain_score, size=record["size"],
            #                                                     game=record["game"], round=record["index"],
            #                                                     val=record["value"],
            #                                                     best_val=record["best_value"]))
            # {"size": size, "game": game, "index": round,
            #  "value": val, "best_value": best_val,
            #  "domain_selected": domain_selected,
            #  "domain_best_value": domain_best_value,
            #  "model_selected": model_selected,
            #  "model_best_value": model_best_value}

            current_ai_score = 1
            current_domain_score = 1
            for rec in list_records:
                if "model_score" in rec.keys():
                    current_ai_score = max(current_ai_score, rec["model_score"])
                if "domain_score" in rec.keys():
                    current_domain_score = max(current_domain_score, rec["domain_score"])
            list_finals.append({"size": list_records[0]['size'], "game": list_records[0]['game'],
                                'ai_score': current_ai_score, 'domain_score': current_domain_score,
                                'total_score': current_ai_score / current_domain_score,
                                'search_node_count': 0})

        df = pd.read_json(json.dumps(list_finals))
        print(df.describe())
        bin_sizes = np.arange(0,1.01,0.125).tolist()
        #bin_sizes.append(max(df["total_score"]))
        plt.hist(df["total_score"], bins=bin_sizes)
        plt.xlabel("Final AI Scores (AI score)/(Domain score) higher is better ")
        plt.title('AI Scores Distribution (No matter win or lose)')
        plt.show()

        plt.hist(df['search_node_count'])
        plt.xlabel("Search Nodes (Not applicable)")
        plt.title('AI Search Node Distribution (Not applicable if non-tree search algorithm)')
        plt.show()

        print(
            '--------------------------------------------------------------------------------------------------------')
        print(
            '========================================================================================================')

        pass
