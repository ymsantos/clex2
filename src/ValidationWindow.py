from gi.repository import Gtk

class ValidationWindow(Gtk.Window):
	def __init__(self, string):
		Gtk.Window.__init__(self, title="Select " + string + " Validation Indexes")
		self.connect('delete-event', self.hide_window)
		self.selection_list = []
		self.validation_list = []

		if string == "External":
			self.check_ext_validation1 = Gtk.CheckButton(label="CR")
			self.check_ext_validation2 = Gtk.CheckButton(label="NMI")
			self.check_ext_validation3 = Gtk.CheckButton(label="VI")
			self.check_ext_validation1.set_active(True)
			self.validation_list.append("CRIndex")
		elif string == "Internal":
			self.check_int_validation1 = Gtk.CheckButton(label="Connectivity")
			self.check_int_validation2 = Gtk.CheckButton(label="Deviation")
			self.check_int_validation3 = Gtk.CheckButton(label="Silhouette")
			self.check_int_validation3.set_active(True)
			self.validation_list.append("Silhouette")


		# Containers
		self.set_default_size(300, 200)
		self.box = Gtk.VBox()
		self.bbox = Gtk.HButtonBox(spacing=6)
		self.bbox.set_layout(Gtk.ButtonBoxStyle.END)

		# List model
		# self.store = Gtk.ListStore(str)

		# List view
		# self.treeview = Gtk.TreeView(self.store)
		# self.renderer = Gtk.CellRendererText()
		# self.column = Gtk.TreeViewColumn(string + "Validation Index", self.renderer, text=0)
		# self.treeview.append_column(self.column)
		# self.box.pack_start(self.treeview, True, True, 0)

		# List control
		# self.selection = self.treeview.get_selection()
		# self.selection.set_mode(Gtk.SelectionMode.MULTIPLE)
		# self.selection.connect("changed", self.on_tree_selection_changed)
		if string == "External":
			self.check_ext_validation1.connect("toggled", self.on_check_ext_val1_clicked)
			self.check_ext_validation2.connect("toggled", self.on_check_ext_val2_clicked)
			self.check_ext_validation3.connect("toggled", self.on_check_ext_val3_clicked)
		elif string == "Internal":
			self.check_int_validation1.connect("toggled", self.on_check_int_val1_clicked)
			self.check_int_validation2.connect("toggled", self.on_check_int_val2_clicked)
			self.check_int_validation3.connect("toggled", self.on_check_int_val3_clicked)

		# Control buttons
		self.button_ok = Gtk.Button(stock=Gtk.STOCK_OK)
		self.button_cancel = Gtk.Button(stock=Gtk.STOCK_CANCEL)
		self.button_ok.connect("clicked", self.on_button_ok_clicked)
		self.button_cancel.connect("clicked", self.on_button_cancel_clicked)

		# Packing buttons
		if string == "External":
			self.box.pack_start(self.check_ext_validation1, False, False, 4)
			self.box.pack_start(self.check_ext_validation2, False, False, 4)
			self.box.pack_start(self.check_ext_validation3, False, False, 4)
		elif string == "Internal":
			self.box.pack_start(self.check_int_validation1, False, False, 4)
			self.box.pack_start(self.check_int_validation2, False, False, 4)
			self.box.pack_start(self.check_int_validation3, False, False, 4)
		self.bbox.pack_start(self.button_ok, True, True, 0)
		self.bbox.pack_start(self.button_cancel, True, True, 0)
		self.box.pack_start(self.bbox, True, True, 0)
		self.add(self.box)

	def hide_window(self, window, event):
		self.hide()
		return True

	# Add CRIndex in the List
	def on_check_ext_val1_clicked(self, widget):#########
		if widget.get_active():
			self.validation_list.append("CRIndex")
		else:
			self.validation_list.remove("CRIndex")
	
	# Add NMIIndex in the List
	def on_check_ext_val2_clicked(self, widget):#########
		if widget.get_active():
			self.validation_list.append("NMIIndex")
		else:
			self.validation_list.remove("NMIIndex")

	# Add VIIndex in the List
	def on_check_ext_val3_clicked(self, widget):#########
		if widget.get_active():
			self.validation_list.append("VIIndex")
		else:
			self.validation_list.remove("VIIndex")

	# Add Connectivity in the List
	def on_check_int_val1_clicked(self, widget):#########
		if widget.get_active():
			self.validation_list.append("Connectivity")
		else:
			self.validation_list.remove("Connectivity")
	
	# Add Deviation in the List
	def on_check_int_val2_clicked(self, widget):#########
		if widget.get_active():
			self.validation_list.append("Deviation")
		else:
			self.validation_list.remove("Deviation")

	# Add Silhouette in the List
	def on_check_int_val3_clicked(self, widget):#########
		if widget.get_active():
			self.validation_list.append("Silhouette")
		else:
			self.validation_list.remove("Silhouette")
	
	# def on_tree_selection_changed(self, widget):
	# 	self.model, self.treeiter = self.selection.get_selected_rows()

	def on_button_ok_clicked(self, widget):
		# self.model, self.treeiter = self.selection.get_selected_rows()
		# for row in self.treeiter:
		# 	self.selection_list.append(self.model[row][0])
		self.hide()

	def on_button_cancel_clicked(self, widget):
		self.hide()

	def get_selection_list(self):
		return self.selection_list

	def get_validation_list(self):
		return self.validation_list

	def clean_settings(self, val):
		self.validation_list = []
		if val == "External":
			self.check_ext_validation1.set_active(False)
			self.check_ext_validation2.set_active(False)
			self.check_ext_validation3.set_active(False)
		elif val == "Internal":
			self.check_int_validation1.set_active(False)
			self.check_int_validation2.set_active(False)
			self.check_int_validation3.set_active(False)

	def set_loaded_settings(self, val_list, string):
		self.clean_settings(string)
		if string == "External":
			for i in val_list:
				self.validation_list.append(i)
			for i in self.validation_list:
				if i == "CRIndex":
					self.check_ext_validation1.set_active(True)
				elif i == "NMIIndex":
					self.check_ext_validation2.set_active(True)
				elif i == "VIIndex":
					self.check_ext_validation3.set_active(True)
		elif string == "Internal":
			for i in val_list:
				self.validation_list.append(i)
			for i in self.validation_list:
				if i == "Connectivity":
					self.check_int_validation1.set_active(True)
				elif i == "Deviation":
					self.check_int_validation2.set_active(True)
				elif i == "Silhouette":
					self.check_int_validation3.set_active(True)
