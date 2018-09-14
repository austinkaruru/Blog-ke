class Blog:
    all_blogs = []

    # def __init__(self.blog):
    #     self.blog = blog

    def save_blog(self):
        Blog.all_blogs.append(self)

    @classmethod
    def clear_blogs(cls):
        Blog.all_blogs.clear()
