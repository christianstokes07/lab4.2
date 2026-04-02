import util # Ensure this is at the top of your file

@app.route('/pages/<name>')
def pages(name):
    # 1. Get the actual list of all wiki filenames
    all_pages_list = util.list_entries() 
    
    # 2. Get the content of the current page
    content = util.get_entry(name)

    if content is None:
        return "Page not found", 404
    
    # 3. Find the neighbors in the list
    try:
        current_index = all_pages_list.index(name)
        # Get the name of the page before this one
        prev_p = all_pages_list[current_index - 1] if current_index > 0 else None
        # Get the name of the page after this one
        next_p = all_pages_list[current_index + 1] if current_index < len(all_pages_list) - 1 else None
    except ValueError:
        prev_p = None
        next_p = None

    # 4. SEND THE REAL NAMES TO THE HTML
    return render_template("page.html", 
                           page_name=name, 
                           page_content=content, 
                           prev_page=prev_p, 
                           next_page=next_p)