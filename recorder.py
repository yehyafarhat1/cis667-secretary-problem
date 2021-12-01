class Recorder:
    def __init__(self):
        self.model_score = 0
        self.domain_score = 0
        self.record_list = []
        pass

    def get_record_list(self):
        return self.record_list

    def append(self, record):
        # {"size": size, "game": game, "index": round,
        #  "value": val, "best_value": best_val,
        #  "domain_selected": domain_selected,
        #  "domain_best_value": domain_best_value,
        #  "model_selected": model_selected,
        #  "model_best_value": model_best_value}

        if record is None:
            return

        action = False
        if record["domain_selected"] or record["model_selected"]:
            action = True

            if record["domain_best_value"] == record["model_best_value"]:
                pass
                # no points
            else:
                if record["domain_best_value"] > record["model_best_value"]:
                    if record["domain_best_value"] == record["best_value"]:
                        self.domain_score += 3
                    else:  # record["domain_best_value"] < record["best_value"]
                        self.domain_score += 1
                else:  # record["domain_best_value"] < record["model_best_value"]
                    if record["model_best_value"] == record["best_value"]:
                        self.model_score += 3
                    else:  # record["model_best_value"] < record["best_value"]
                        self.model_score += 1

            record["action"] = True
            record["model_score"] = self.model_score
            record["domain_score"] = self.domain_score

        self.record_list.append(record)

        if action or self.record_list.__len__() % 10 == 0:
            # print current result
            print("Current result: MODEL:{model_score} ; DOMAIN:{domain_score} "
                  "\t\tsize: {size}, game: {game}, index: {round}, "
                  "value: {val}, best_value: {best_val}".format(model_score=self.model_score,
                                                                domain_score=self.domain_score, size=record["size"],
                                                                game=record["game"], round=record["index"],
                                                                val=record["value"],
                                                                best_val=record["best_value"]))
            pass
