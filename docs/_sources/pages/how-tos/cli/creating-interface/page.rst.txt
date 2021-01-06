Pages
=====

The CLI Interface is mostly based on Pages, when a Page is displayed it renders first the PageControl Base content
then it renders the Page content

For example, lets create the Home Page by creating a file at *interface/default/Home.py*:

First, import the Page module:

.. code-block:: python
   
   from pysimpleframe.interface.pages.Page import Page



Then make a class based on Page:

.. code-block:: python

   class Run(Page):
	def __init__(self):
		## Initialize the page
		Page.__init__(self, "Home")
		self.Run()
	
	def __call__(self):
		## Run the page
		self.Run()
	
	def Run(self):
		## Make a space to divide
		Display.Print("")
		
		## Write a message
		Display.Print("Hello World!")
		
If done correctly, on calling this Page the following will appear:

.. code-block::
   
   Hello World!
	