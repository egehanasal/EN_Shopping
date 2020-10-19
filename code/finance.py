class Finance:

    budget = 35000

    @staticmethod
    def report(person, expense, type):
        if type == "income":
            print("From: " + person + ", " + str(expense) + "\nBudget now: " + str(Finance.budget) + "\n")
        else:
            print("To: " + person + ", " + str(expense) + "\nRemaining budget: " + str(Finance.budget) + "\n")


