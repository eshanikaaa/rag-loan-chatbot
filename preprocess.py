def convert_row_to_text(row):
    return (
        f"Applicant is a {'male' if row['Gender']=='Male' else 'female'}, "
        f"{'married' if row['Married']=='Yes' else 'single'}, "
        f"{'a graduate' if row['Education']=='Graduate' else 'not a graduate'}, "
        f"{'self-employed' if row['Self_Employed']=='Yes' else 'not self-employed'}, "
        f"with an income of {row['ApplicantIncome']} and loan amount of {row['LoanAmount']}. "
        f"Credit history is {'good' if row['Credit_History']==1.0 else 'bad'}. "
        f"Loan was {'approved' if row['Loan_Status']=='Y' else 'rejected'}."
    )

def preprocess_data(df):
    df = df.fillna({
        "Gender": "Male",
        "Married": "No",
        "Education": "Graduate",
        "Self_Employed": "No",
        "ApplicantIncome": df["ApplicantIncome"].median(),
        "LoanAmount": df["LoanAmount"].median(),
        "Credit_History": 1.0,
    })

    return df.apply(convert_row_to_text, axis=1).tolist()
