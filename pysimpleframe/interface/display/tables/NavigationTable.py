#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PySimpleFrame
   Name: TOFILL
   Author: Miguel Silva
   Description: TOFILL
   License: CC BY-SA 4.0 - Check LICENSE file
"""

## System imports ##

## Library imports ##
import termtables
from colorama import Fore, Back, Style

## Application imports ##
from pysimpleframe.interface.display import Display


class NavigationTable:
	def __init__(self, header, data, amount, width=60):
		## Reference header list
		self.Header = header
		
		## Reference data list
		self.Data = data
		
		## Insert the selected label text at header beginning
		self.Header.insert(0, "X")
		
		## The width of the table (default 60)
		self.width = width
		
		## The amount to show in the table
		self.showAmount = amount
		
		## The page to show in the table
		self.page = 1
		
		## The selected table item index
		self.selectedIndex = 1
		
		## The current displaying table
		self.table = None
	
	def __del__(self):
		pass
	
	def ShowTable(self):
		## Reference the data count
		dataCount = len(self.Data)
		
		## Check if there is any data to show
		if dataCount < 1:
			Display.Print("There isn't any data to show")
			return
		
		## Calculate the page amount
		pageCount = max(dataCount / self.showAmount, 1)
		
		idx = 0 ## Initial index
		startIdx = self.showAmount * self.page  ## Starting index
		startIdx = startIdx if startIdx < dataCount else 0 ## Starting index
		endIdx = startIdx + self.showAmount ## Ending index
		endIdx = endIdx if dataCount > endIdx else dataCount ## Ending index
		
		localSelectedIndex = ((self.selectedIndex - 1) % self.showAmount) + 1
		
		## Create the data table item list
		dataTableItemList = []
		
		for i in range(int(startIdx), int(endIdx)):
			## Reference the data item by index
			dataItem = self.Data[i]
			
			## Create the data item list
			dataItemList = []
			
			## Increase the local index
			idx += 1
			
			## Append the index selection status
			dataItemList.append("x" if idx == localSelectedIndex else "")
			
			## Append the data items for the selection and fill the data list
			for item in dataItem:
				dataItemList.append(item)			
			
			dataTableItemList.append(dataItemList)
		
		## Generate the data table by list
		self.table = table = termtables.to_string(
			dataTableItemList,
			header = self.Header,
			style = termtables.styles.ascii_thin_double,
		)
		
		## Print the accounts data table
		Display.Print(table)
		
		## Show the table details
		self.ShowNavigationLabel(self.page, self.selectedIndex)
		
	def ShowNavigationLabel(self, page, selectedIndex):
		## Display the status of the table navigation
		if page <= 1:
			Display.Print('{:^94s}'.format("Page %u/%u : Selected %u/%u | %u >>" % 
						 (page, self.__GetPageCount(),
						  selectedIndex, self.__GetItemCount(), page + 1)))
		elif page >= self.__GetPageCount():
			Display.Print('{:^94s}'.format("<< %u | Page %u/%u : Selected %u/%u" % 
						 (page - 1, page, self.__GetPageCount(),
						  selectedIndex, self.__GetItemCount())))
		else:
			Display.Print('{:^94s}'.format("<< %u | Page %u/%u : Selected %u/%u | %u >>" % 
						 (page - 1, page, self.__GetPageCount(),
						  selectedIndex, self.__GetItemCount(), page + 1)))
		
		## Make a space to divide
		Display.Print("")
	
	
	def __GetItemCount(self):
		## Return the data item count
		return len(self.Data)
	
	def __GetPageCount(self):
		## Calculate the page amount
		pageAmount = max(self.__GetItemCount() / self.showAmount, 1)
		
		## Return the page amount
		return pageAmount
	
	def __GetSelectedSessionIndex():
		return self.page * self.showAmount + self.selectedIndex
	
	def ChangeSelected(self, amount):
		## Check if the data item amount is greater than the data item count
		if self.selectedIndex + amount > self.__GetItemCount():
			self.selectedIndex = self.__GetItemCount()
		
		## Check if the session amount is less than 0
		elif self.selectedIndex + amount < 1:
			self.selectedIndex = 1
		
		## Change the session index
		else:
			self.selectedIndex += amount
		
		## Recalculate the page index
		if self.selectedIndex > self.showAmount:
			self.page = int((self.selectedIndex - 1) / self.showAmount) + 1
		else:
			self.page = 1

	def ChangePage(self, amount):
		## Check if the page amount is greater than the page count
		if self.page + amount > self.__GetPageCount():
			self.page = self.__GetPageCount()

		## Check if the page amount if less than 0
		elif self.page + amount < 1:
			self.page = 1
		
		## Change the page count
		else:
			self.page += amount
		
		## Reset the selected index to default
		self.selectedIndex = (self.page - 1) * self.showAmount + 1
	
	