from flask import Blueprint, render_template, request

# Define a Blueprint
views = Blueprint('views', __name__)

data = {
    'tab1': [f'Item 1.{i}' for i in range(1, 51)],  # 50 items for tab1
    'tab2': [f'Item 2.{i}' for i in range(101, 161)]   # 60 items for tab2
}

ITEMS_PER_PAGE = 5

@views.route('/tabs')
def tabs():
    defaultTab = 'tab1'
    tab = request.args.get('tab', defaultTab)

    pageNum = int(request.args.get('page', default=1))
    start = (pageNum - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE

    total_items = len(data.get(tab, []))
    items = data.get(tab, [])[start:end]

    total_pages = (total_items + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE

    # if tab == 'tab1':
    #     # Dummy data for Tab 1
    #     items = data[tab]
    # else:
    #     # Dummy data for Tab 2
    #     # items = ['Item 2.1', 'Item 2.2', 'Item 2.3']
    #     items = data[tab]

    return render_template('tabs.html', tab=tab, items=items, page=pageNum, total_pages=total_pages)
