from flask import render_template, send_file


def make_endpoints(app, backend):

    @app.route("/")
    def home():
        return render_template("main.html",
                               page_name="Wiki Index",
                               is_home=True)

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/images/<image>")
    def images(image):
        return send_file(backend.get_image(image), mimetype='image/jpeg')

    @app.route("/pages")
    def all_pages():
        return render_template("pages.html",
                               page_name="Wiki Index",
                               all_pages=backend.get_all_page_names())

    @app.route("/pages/<name>")
    def pages(name):
        all_pages_list = list(backend.get_all_page_names())
        content = backend.get_wiki_page(name)

        if content is None:
            return "Page not found", 404

        try:
            current_index = all_pages_list.index(name)
            prev_page = all_pages_list[current_index - 1] if current_index > 0 else None
            next_page = all_pages_list[current_index + 1] if current_index < len(all_pages_list) - 1 else None
        except ValueError:
            prev_page = None
            next_page = None

        return render_template("main.html",
                               page_name=name,
                               page_content=content,
                               prev_page=prev_page,
                               next_page=next_page)