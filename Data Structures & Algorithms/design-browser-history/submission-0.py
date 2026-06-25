class Node: #doubly listed node
    def __init__(self, url: str): #url : str ??
        self.url = url
        self.prev = None
        self.next = None 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        new_page = Node(url)

        new_page.prev = self.current
        self.current.next = new_page

        self.current = self.current.next

    def back(self, steps: int) -> str:
        while(steps > 0) and (self.current.prev is not None):
            self.current = self.current.prev
            steps -= 1
        
        return self.current.url

    def forward(self, steps: int) -> str:
        while(steps > 0) and (self.current.next is not None):
            self.current = self.current.next
            steps -= 1
        
        return self.current.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)