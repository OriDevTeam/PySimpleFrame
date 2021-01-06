Downloading/Installing
======================

The package can be installed in different situations as necessary:

Pip(testpypi)
^^^^^^^^^^^^^
.. code-block:: python

   pip install --index-url https://test.pypi.org/simple/ PySimpleFrame




Pipfile(testpypi)
^^^^^^^^^^^^^^^^^

Before declaring the package, add testpypi source to the Pipfile if not present
   
.. code-block:: python

	[[source]]
	name = "test"
	url = "https://test.pypi.org/simple"
	verify_ssl = true
   
After, add the package normally as:
   
.. code-block:: python

   pysimpleframe = "*"
   
Where '*' is your desired pysimpleframe version

