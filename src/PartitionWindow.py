from gi.repository import Gtk
from FileList import *

class PartitionWindow(Gtk.Window):

	def get_selection_list(self):
		return self.selection_list

	def set_dataset_list(self, dataset_list):
		self.dataset_listbox.store.clear()
		for row in dataset_list:
			self.dataset_listbox.store.append(row[:])

	def get_dataset_partition_dic(self):
		return self.dataset_partition_dic

	# def get_dataset_partition_dic(self):

	def set_dataset_partition_dic(self, dataset_list):
		self.temp_dataset_partition_dic = self.dataset_partition_dic
		self.dataset_partition_dic = {}
		for row in dataset_list:
			self.dataset_partition_dic[row[0]] = []
			if self.temp_dataset_partition_dic.has_key(row[0]):
				self.dataset_partition_dic[row[0]] = self.temp_dataset_partition_dic[row[0]]
		# if len(dataset_list) > 0:
		# 	self.dataset_listbox.select_first_dataset(self.dataset_listbox.store.get_iter(0))
		# self.is_open = True
		# for a, b in self.dataset_partition_dic.items():
		# 	print a, '->', b

	def update_selected_dataset(self, selected_dataset):
		self.dataset_on_focus = selected_dataset
		self.partition_listbox.store.clear()
		for i in self.dataset_partition_dic[self.dataset_on_focus]:
			self.partition_listbox.store.append([i])

	def update_dataset_partition_dic(self):
		self.temp_dic_list = []
		for row in self.partition_listbox.store:
			self.temp_dic_list.append(row[0])
		self.dataset_partition_dic[self.dataset_on_focus] = self.temp_dic_list
		for a, b in self.dataset_partition_dic.items():
			print a, '->', b
		print "\n"

	def on_button_ok_clicked(self, widget):
		self.selection_list = []
		self.partition_listbox.temp_store.clear()
		for row in self.partition_listbox.store:
			self.selection_list.append(row)
			self.partition_listbox.temp_store.append(row[:])
		self.hide()
		# self.is_open = False

	def on_button_cancel_clicked(self, widget):
		self.partition_listbox.store.clear()
		for row in self.partition_listbox.temp_store:
			self.partition_listbox.store.append(row[:])
		self.hide()
		# self.is_open = False

	def clean_settings(self):
		self.dataset_partition_dic = {}
		self.partition_listbox.store.clear()
		self.partition_listbox.temp_store.clear()

	def set_loaded_settings(self, partition_dic):
		self.dataset_partition_dic = partition_dic
		for dataset, partition in self.dataset_partition_dic.items():
			for i in partition:
				self.partition_listbox.store.append([i])
				self.partition_listbox.temp_store.append([i])

	
	# def on_button_close_clicked(self, widget):#
	# 	self.hide()
	
	def hide_window(self, window, event):
		self.hide()
		# self.is_open = False
		return True

	def __init__(self, title):
		Gtk.Window.__init__(self, title=title)
		self.set_default_size(800, 400)
		self.connect('delete-event', self.hide_window)

		# containers
		self.mainbox = Gtk.VBox()
		self.listbox = Gtk.HBox()
		self.dataset_listbox = FileList("DataSet", False)
		self.dataset_listbox.set_partition_window_instance(self)
		self.separator = Gtk.VSeparator()
		self.partition_listbox = FileList("Partition", True)
		self.partition_listbox.set_partition_window_instance(self)

		self.dataset_partition_dic = {}
		# self.is_open = False

		# self.test_print()

		self.buttonbox = Gtk.HButtonBox(False, 6)
		self.buttonbox.set_layout(Gtk.ButtonBoxStyle.END)

		# buttons to commit and to cancel the list
		self.button_ok = Gtk.Button(stock=Gtk.STOCK_OK)
		self.button_cancel = Gtk.Button(stock=Gtk.STOCK_CANCEL)
		self.button_cancel.connect("clicked", self.on_button_cancel_clicked)
		# self.button_close = Gtk.Button(stock=Gtk.STOCK_CLOSE)
		# self.button_close.connect("clicked", self.on_button_close_clicked)
		self.button_ok.connect("clicked", self.on_button_ok_clicked)
		self.buttonbox.pack_start(self.button_ok, False, True, 0)
		self.buttonbox.pack_start(self.button_cancel, False, True, 0)
		# self.buttonbox.pack_start(self.button_close, False, True, 0)

		self.listbox.pack_start(self.dataset_listbox, True, True, 0)
		self.listbox.pack_start(self.separator, False, True, 5)
		self.listbox.pack_start(self.partition_listbox, True, True, 0)
		self.mainbox.pack_start(self.listbox, True, True, 0)
		self.mainbox.pack_start(self.buttonbox, False, True, 0)
		self.add(self.mainbox)
