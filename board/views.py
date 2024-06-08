from flask import Blueprint, render_template, request

# Define a Blueprint
views = Blueprint('views', __name__)

# dummy data for the tabs
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

    # indexed items for the current tab
    items = data.get(tab, [])[start:end]

    # How do we calc total pages now ?
    # ex: 45 items in tab, ITEMS_PER_PAGE = 10
    # total_items = 45
    # total_pages needed = 45 // 10 = 4 ??
    # pg1: 1-10, pg2: 11-20, pg3: 21-30,
    # pg4: 31-40, pg5:41-45
    # 

    # - 1 ensures that we account for any leftover items that wouldn't fit completely on a full page
    total_pages = (total_items + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE

    # if tab == 'tab1':
    #     # Dummy data for Tab 1
    #     items = data[tab]
    # else:
    #     # Dummy data for Tab 2
    #     # items = ['Item 2.1', 'Item 2.2', 'Item 2.3']
    #     items = data[tab]

    return render_template('tabs.html', tab=tab, items=items, page=pageNum, total_pages=total_pages)
