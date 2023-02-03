from flask import Flask, render_template, request, redirect
from budget_tracker import BudgetTracker

app = Flask(__name__)

# Initialize a budget tracker object
tracker = BudgetTracker()

@app.route('/')
def home():
    # Get a list of all categories and their current balances
    categories = tracker.get_all_categories()

    return render_template('home.html', categories=categories)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    # Get the form data from the request
    category = request.form['category']
    amount = request.form['amount']
    description = request.form['description']

    # Add the transaction to the budget tracker
    tracker.add_transaction(category, amount, description)

    # Get the updated list of categories and balances
    categories = tracker.get_all_categories()

    # Render the template with the updated list of categories
    return render_template('home.html', categories=categories)

@app.route('/entries')
def list_entries():
    categories = tracker.get_all_categories()
    return render_template('entries.html', categories=categories)

if __name__ == '__main__':
    app.run()