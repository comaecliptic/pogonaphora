import pandas as pd
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, help='table in tsv format', required=True)
parser.add_argument('--threshold', type=int, help='significant percent', required=True)
parser.add_argument('--out', type=str, help='tag for output', required=True)
args = parser.parse_args()


def sample_specificity(file, threshold, out):
    """
    selects "genes" whose expression level exceeds a given percentage of the total amount of expression in the sample
    """
    data = pd.read_csv(file, sep='\t')
    for sample in data.columns[1:]:
        specific = data[data[sample] >= threshold/100*data.iloc[:, 1:].sum(axis=1)]
        specific.iloc[:, 0].to_csv("{out}.state_specific_in_{sample}.txt".format(out=out, sample=sample), sep='\t', index=False)


if __name__ == "__main__":
    sample_specificity(args.file, args.threshold, args.out)
