"""
My First Module
"""
word = 'Hello World! my name is Mark Brian G. Solero'

def calculateLoan(months_Contribution) :
    """
    Parameter: The total number of Months of Company membership contribution
    Returns: The Loanable Amount
    """
    loan_Factor = None
    Loanable = None
    if months_Contribution > 120 :
        loan_Factor = 0.80
    else :
        loan_Factor = 0.60
    Loanable = (months_Contribution * 100) * loan_Factor
    return (Loanable)
