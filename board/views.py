from flask import Blueprint, render_template, request

# Define a Blueprint
views = Blueprint('views', __name__)

@views.route('/tabs')
def tabs():
    default = 'tab1'
    tab = request.args.get('tab', default)

    if tab == 'tab1':
        # Dummy data for Tab 1
        items = list(range(1, 101))
    else:
        # Dummy data for Tab 2
        # items = ['Item 2.1', 'Item 2.2', 'Item 2.3']
        items = list(range(201, 301))

    return render_template('tabs.html', tab=tab, items=items)
