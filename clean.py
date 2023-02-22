import argparse
import pandas as pd

arg_parser = argparse.ArgumentParser(
    prog = 'clean.py',          # program name
    description = 'The script for data cleansing'       # function description
)

arg_parser.add_argument('args',nargs=3)
args = arg_parser.parse_args()

contact_info_file = args.args[0]
other_info_file = args.args[1]
output_file = args.args[2]

#print(args)

if not contact_info_file or not other_info_file or not output_file:
    print("No argument found. Attach -h as the argument to view the help info")
    exit(1)


#(1)
contact_info=pd.read_csv(contact_info_file) 
other_info=pd.read_csv(other_info_file)
df = pd.merge(contact_info,other_info,left_on="respondent_id",right_on="id")

#(2)
df.dropna(inplace=True)
df.drop(df[df['job'].str.lower().str.contains('insurance')].index,inplace=True)
df.to_csv(output_file)
