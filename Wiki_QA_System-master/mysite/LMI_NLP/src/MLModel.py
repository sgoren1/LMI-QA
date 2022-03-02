import pandas as pd
from transformers import pipeline


class MLModel:
    def __init__(self):
        self.fquad_findings = []

    # def RobertaModel(self,TopNDf,query):
    #     #trying different exisiting pre trained models in hugging face
    #     qa_pipeline = pipeline("question-answering",model="deepset/roberta-base-squad2",tokenizer="deepset/roberta-base-squad2", revision="v1.0")
    #     #looping through all context
    #     for x,context in enumerate(TopNDf['Context']):
    #       prediction = qa_pipeline({'context': context,'question': query})
    #       self.roberta_findings.append([prediction['answer'],prediction['score'],TopNDf.iloc[x,2],context])
    #     return self.roberta_findings

    def FquadModel(self, TopNDf, query):
        # trying different exisiting pre trained models in hugging face
        qa_pipeline = pipeline("question-answering", model="etalab-ia/camembert-base-squadFR-fquad-piaf",
                               tokenizer="etalab-ia/camembert-base-squadFR-fquad-piaf")
        # looping through all context
        for x, context in enumerate(TopNDf['Context']):
            prediction = qa_pipeline({'context': context, 'question': query})
            self.fquad_findings.append([prediction['answer'], prediction['score'], TopNDf.iloc[x, 2], context])
        return self.fquad_findings

    def TopNFindings(self, top_n=3):
        return sorted(self.fquad_findings, key=itemgetter(1), reverse=True)[:top_n]

    def ConverttoDf(self):
        Converted_Df = pd.DataFrame(self.fquad_findings, columns=['Prediction', 'Score', 'Wiki_Page', 'Context'])
        return Converted_Df

    def TopNDf(self, Df, top_n=3):
        return Df.sort_values(by=['Score'], ascending=False).iloc[:top_n, ]

    def GetContext(self, Df):
        return Df['Context'].tolist()

    def GetPrediction(self, Df):
        return Df['Prediction'].tolist()
