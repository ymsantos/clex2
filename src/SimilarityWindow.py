from gi.repository import Gtk

class SimilarityWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Select Similarity Measures")
		self.connect('delete-event', self.hide_window)
		# self.selection_list = []
		self.similarity_param_list = []
		# self.temp_similarity_param_list = []

		# Containers
		self.set_default_size(300, 200)
		self.box = Gtk.VBox()
		self.bbox = Gtk.HButtonBox(spacing=6)
		self.bbox.set_layout(Gtk.ButtonBoxStyle.END)

		# List model
		# self.store = Gtk.ListStore(str)
		# self.store.append(["Euclidean Distance"])
		# self.store.append(["Pearson Correlation"])
		self.check_similarity1 = Gtk.CheckButton(label="Euclidean Distance")
		self.check_similarity2 = Gtk.CheckButton(label="Pearson Correlation")
		self.check_similarity1.set_active(True)
		self.similarity_param_list.append("7")


		# List view
		# self.treeview = Gtk.TreeView(self.store)
		# self.renderer = Gtk.CellRendererText()
		# self.column = Gtk.TreeViewColumn("Similarity Index", self.renderer, text=0)
		# self.treeview.append_column(self.column)
		# self.box.pack_start(self.treeview, True, True, 0)

		# List control
		# self.selection = self.treeview.get_selection()
		# self.selection.set_mode(Gtk.SelectionMode.MULTIPLE)
		# self.selection.connect("changed", self.on_tree_selection_changed)
		self.check_similarity1.connect("toggled", self.on_check_similarity1_clicked, "Euclidean Distance")
		self.check_similarity2.connect("toggled", self.on_check_similarity2_clicked, "Pearson Correlation")

		# Control buttons
		self.button_ok = Gtk.Button(stock=Gtk.STOCK_OK)
		self.button_cancel = Gtk.Button(stock=Gtk.STOCK_CANCEL)
		self.button_ok.connect("clicked", self.on_button_ok_clicked)
		self.button_cancel.connect("clicked", self.on_button_cancel_clicked)

		# Packing buttons
		self.box.pack_start(self.check_similarity1, False, False, 4)
		self.box.pack_start(self.check_similarity2, False, False, 4)
		self.bbox.pack_start(self.button_ok, True, True, 0)
		self.bbox.pack_start(self.button_cancel, True, True, 0)
		self.box.pack_start(self.bbox, True, True, 0)
		self.add(self.box)

	def hide_window(self, window, event):
		self.hide()
		return True
	
	# def on_tree_selection_changed(self, widget):
	# 	self.model, self.treeiter = self.selection.get_selected_rows()

	# Add Euclidean Distance in Similarity List
	def on_check_similarity1_clicked(self, widget, data=None):#########
		if widget.get_active():
			self.similarity_param_list.append("7")
		else:
			self.similarity_param_list.remove("7")
	
	# Add Pearson Correlation in Similarity List
	def on_check_similarity2_clicked(self, widget, data=None):#########
		if widget.get_active():
			self.similarity_param_list.append("2")
		else:
			self.similarity_param_list.remove("2")

	def on_button_ok_clicked(self, widget):
		# self.similarity_param_list = self.temp_similarity_param_list
		# self.temp_similarity_param_list = []
		self.hide()

	def on_button_cancel_clicked(self, widget):
		self.hide()

	def get_selection_list(self):
		return self.selection_list

	def get_similarity_param_list(self):
		return self.similarity_param_list

	def clean_settings(self):
		self.similarity_param_list = []
		self.check_similarity1.set_active(False)
		self.check_similarity2.set_active(False)

	def set_loaded_settings(self, similarity_list):
		self.clean_settings()
		for i in similarity_list:
			self.similarity_param_list.append(i)
		for i in self.similarity_param_list:
			if i == "7":
				self.check_similarity1.set_active(True)
			elif i == "2":
				self.check_similarity2.set_active(True)
