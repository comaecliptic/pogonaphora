import pandas as pd
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, required=True)
parser.add_argument('--threshold', type=int, required=True)
parser.add_argument('--out', type=str, required=True)
args = parser.parse_args()


def act_measure(file, threshold, out):
    """
    Selects active sequences (expression above a given threshold) for each sample
    """
    data = pd.read_csv(file, sep='\t')
    for sample in data.columns[1:]:
        specific = data[data[sample] >= threshold]
        specific.iloc[:, 0].to_csv("{out}.all_active_in_{sample}.txt".format(out=out, sample=sample), sep='\t', index=False)


if __name__ == "__main__":
    act_measure(args.file, args.threshold, args.out)