import seaborn as sns
tips = sns.load_dataset("tips")
print(tips.head())

objective = "Classification: Survived (Yes/No)"
sucess_criteria = "Accuracy > 80%"
constraints = "Limited features, missing values, imbalanced classes"
print("Objective:", objective)
print("Sucess Criteria:", sucess_criteria)
print("Constraints:", constraints)