from gi.repository import Gtk
from FileList import *

class DataSetWindow(Gtk.Window):

	def get_dataset_list(self):
		self.ds_list = []
		for row in self.selection_list:
			self.ds_list.append(row[0])
		return self.ds_list

	def get_selection_list(self):
		return self.selection_list

	def on_button_ok_clicked(self, widget):
		self.selection_list = []
		self.listbox.temp_store.clear()
		for row in self.listbox.store:
			# print row
			self.selection_list.append(row)
			self.listbox.temp_store.append(row[:])
		self.hide()

	def on_button_cancel_clicked(self, widget):
		self.listbox.store.clear()
		for row in self.listbox.temp_store:
			self.listbox.store.append(row[:])
		self.hide()
	
	# def on_button_close_clicked(self, widget):#
	# 	self.hide()
	
	def set_loaded_settings(self, d_set_list):
		self.selection_list = []
		self.listbox.store.clear()
		self.listbox.temp_store.clear()
		for i in d_set_list:
			self.listbox.store.append([i])
			self.listbox.temp_store.append([i])
		for row in self.listbox.store:
			self.selection_list.append(row)

	def hide_window(self, window, event):
		self.hide()
		return True


	def __init__(self):
		Gtk.Window.__init__(self, title="Select DataSets")
		self.set_default_size(800, 400)
		self.connect('delete-event', self.hide_window)

		# containers
		self.mainbox = Gtk.VBox()
		self.listbox = FileList("DataSet", True)

		self.buttonbox = Gtk.HButtonBox(False, 6)
		self.buttonbox.set_layout(Gtk.ButtonBoxStyle.END)
		

		# buttons to commit and to cancel the list
		self.button_ok = Gtk.Button(stock=Gtk.STOCK_OK)
		self.button_cancel = Gtk.Button(stock=Gtk.STOCK_CANCEL)
		self.button_cancel.connect("clicked", self.on_button_cancel_clicked)
		#self.button_close = Gtk.Button(stock=Gtk.STOCK_CLOSE)#
		#self.button_close.connect("clicked", self.on_button_close_clicked)#
		self.button_ok.connect("clicked", self.on_button_ok_clicked)
		self.buttonbox.pack_start(self.button_ok, False, True, 0)
		self.buttonbox.pack_start(self.button_cancel, False, True, 0)
		#self.buttonbox.pack_start(self.button_close, False, True, 0)#

		self.mainbox.pack_start(self.listbox, True, True, 0)
		#self.mainbox.pack_start(self.frame, True, True, 0)
		self.mainbox.pack_start(self.buttonbox, False, True, 0)
		self.add(self.mainbox)

		self.selection_list = []
