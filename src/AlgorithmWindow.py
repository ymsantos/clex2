from gi.repository import Gtk

class AlgorithmWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Set Algorithms")
		self.connect('delete-event', self.hide_window)
		self.algorithm_param_list = []
		# self.temp_algorithm_param_list = []

		# clustering program path
		self.clustering_program_path = "clustering/cluster"

		# Containers
		self.set_default_size(300, 200)
		self.box = Gtk.VBox()
		self.bbox = Gtk.HButtonBox(spacing=6)
		self.bbox.set_layout(Gtk.ButtonBoxStyle.END)
		self.parambox = Gtk.VBox(spacing=6)
		self.hbox_minK = Gtk.HBox(spacing=6)
		self.hbox_maxK = Gtk.HBox(spacing=6)
		self.hbox_exec_times = Gtk.HBox(spacing=6)

		# Algorithm List
		# self.store = Gtk.ListStore(str)
		self.check_alg1 = Gtk.CheckButton(label="K-means")
		self.check_alg2 = Gtk.CheckButton(label="Pairwise complete-linkage")
		self.check_alg3 = Gtk.CheckButton(label="Pairwise single-linkage")
		self.check_alg4 = Gtk.CheckButton(label="Pairwise centroid-linkage")
		self.check_alg5 = Gtk.CheckButton(label="Pairwise average-linkage")
		self.check_alg1.set_active(True)
		self.algorithm_param_list.append("k")
		# self.store.append(["K-means"])
		# self.store.append(["Pairwise complete-linkage"])
		# self.store.append(["Pairwise single-linkage"])
		# self.store.append(["Pairwise centroid-linkage"])
		# self.store.append(["Pairwise average-linkage"])

		# List view
		# self.treeview = Gtk.TreeView(self.store)
		# self.renderer = Gtk.CellRendererText()
		# self.column = Gtk.TreeViewColumn("Algorithm", self.renderer, text=0)
		# self.treeview.append_column(self.column)

		# List control
		# self.selection = self.treeview.get_selection()
		# self.selection.set_mode(Gtk.SelectionMode.MULTIPLE)
		# self.selection.connect("changed", self.on_tree_selection_changed)

		# Connect the callback functions to the click event
		self.check_alg1.connect("toggled", self.on_check_alg1_clicked, "K-means")
		self.check_alg2.connect("toggled", self.on_check_alg2_clicked, "Pairwise complete-linkage")
		self.check_alg3.connect("toggled", self.on_check_alg3_clicked, "Pairwise single-linkage")
		self.check_alg4.connect("toggled", self.on_check_alg4_clicked, "Pairwise centroid-linkage")
		self.check_alg5.connect("toggled", self.on_check_alg5_clicked, "Pairwise average-linkage")

		# Control buttons
		self.button_ok = Gtk.Button(stock=Gtk.STOCK_OK)
		self.button_cancel = Gtk.Button(stock=Gtk.STOCK_CANCEL)
		self.button_ok.connect("clicked", self.on_button_ok_clicked)
		self.button_cancel.connect("clicked", self.on_button_cancel_clicked)

		# Packing buttons
		self.bbox.pack_start(self.button_ok, True, True, 0)
		self.bbox.pack_start(self.button_cancel, True, True, 0)

		# Algorithm parameters
		# self.label_min_cluster = Gtk.Label("Min. Cluster number: ")
		# self.spin_min_cluster = Gtk.SpinButton()
		# self.spin_min_cluster.set_adjustment(Gtk.Adjustment(2, 2, 100, 1, 10, 0))
		# self.spin_min_cluster.set_numeric(True)

		# self.label_max_cluster = Gtk.Label("Max. Cluster number: ")
		# self.spin_max_cluster = Gtk.SpinButton()
		# self.spin_max_cluster.set_adjustment(Gtk.Adjustment(2, 2, 100, 1, 10, 0))
		# self.spin_max_cluster.set_numeric(True)

		# self.label_times = Gtk.Label("Times to execute\n non-deterministic\n algorithms: ")
		# self.spin_times = Gtk.SpinButton()
		# self.spin_times.set_adjustment(Gtk.Adjustment(1, 1, 100, 1, 10, 0))
		# self.spin_times.set_numeric(True)
		# self.hbox_exec_times.pack_start(self.label_times, True, True, 0)
		# self.hbox_exec_times.pack_start(self.spin_times, True, True, 0)

		# self.hbox_minK.pack_start(self.label_min_cluster, True, True, 0)
		# self.hbox_minK.pack_start(self.spin_min_cluster, True, True, 0)
		# self.hbox_maxK.pack_start(self.label_max_cluster, True, True, 0)
		# self.hbox_maxK.pack_start(self.spin_max_cluster, True, True, 0)

		# self.parambox.pack_start(self.hbox_minK, True, True, 0)
		# self.parambox.pack_start(self.hbox_maxK, True, True, 0)
		# self.parambox.pack_start(self.hbox_exec_times, True, True, 0)

		# Packing into window
		# self.box.pack_start(self.treeview, True, True, 0)
		self.box.pack_start(self.check_alg1, True, True, 4)
		self.box.pack_start(self.check_alg2, True, True, 4)
		self.box.pack_start(self.check_alg3, True, True, 4)
		self.box.pack_start(self.check_alg4, True, True, 4)
		self.box.pack_start(self.check_alg5, True, True, 4)
		# self.box.pack_start(self.parambox, True, True, 0)
		self.box.pack_start(self.bbox, True, True, 0)
		self.add(self.box)
	
	def hide_window(self, window, event):
		self.hide()
		return True

	# def on_tree_selection_changed(self, widget):
	# 	self.model, self.treeiter = self.selection.get_selected_rows()

	def on_button_ok_clicked(self, widget):
		# self.algorithm_param_list = self.temp_algorithm_param_list
		# self.temp_algorithm_param_list = []
		self.hide()

	def on_button_cancel_clicked(self, widget):
		# for i in self.temp_algorithm_param_list:
		# 	if i == "k":
		# 		self.check_alg1.set_active(False)
		# 	elif i == "m":
		# 		self.check_alg2.set_active(False)
		# 	elif i == "s":
		# 		self.check_alg3.set_active(False)
		# 	elif i == "c":
		# 		self.check_alg4.set_active(False)
		# 	elif i == "a":
		# 		self.check_alg5.set_active(False)

		# self.temp_algorithm_param_list = []
		self.hide()

	def get_algorithm_param_list(self):
		return self.algorithm_param_list

	def get_clustering_program_path(self):
		return self.clustering_program_path
	
	# def get_minK(self):
	# 	return self.spin_min_cluster.get_value_as_int()

	# def get_maxK(self):
	# 	return self.spin_max_cluster.get_value_as_int()

	# def get_execution_times(self):
	# 	return self.spin_times.get_value_as_int()

	# Add K-means in algorithms list to be executed
	def on_check_alg1_clicked(self, widget, data=None):#########
		if widget.get_active():
			self.algorithm_param_list.append("k")
		else:
			self.algorithm_param_list.remove("k")
	
	# Add Pairwise complete-linkage in algorithms list to be executed
	def on_check_alg2_clicked(self, widget, data=None):#########
		if widget.get_active():
			self.algorithm_param_list.append("m")
		else:
			self.algorithm_param_list.remove("m")
	
	# Add Pairwise single-linkage in algorithms list to be executed
	def on_check_alg3_clicked(self, widget, data=None):#########
		if widget.get_active():
			self.algorithm_param_list.append("s")
		else:
			self.algorithm_param_list.remove("s")
	
	# Add Pairwise centroid-linkage in algorithms list to be executed
	def on_check_alg4_clicked(self, widget, data=None):#########
		if widget.get_active():
			self.algorithm_param_list.append("c")
		else:
			self.algorithm_param_list.remove("c")
	
	# Add Pairwise average-linkage in algorithms list to be executed
	def on_check_alg5_clicked(self, widget, data=None):#########
		if widget.get_active():
			self.algorithm_param_list.append("a")
		else:
			self.algorithm_param_list.remove("a")

	def clean_settings(self):
		self.algorithm_param_list = []
		self.check_alg1.set_active(False)
		self.check_alg2.set_active(False)
		self.check_alg3.set_active(False)
		self.check_alg4.set_active(False)
		self.check_alg5.set_active(False)

	def set_loaded_settings(self, algorithm_list):
		self.clean_settings()
		for i in algorithm_list:
			self.algorithm_param_list.append(i)
		for i in self.algorithm_param_list:
			if i == "k":
				self.check_alg1.set_active(True)
			elif i == "m":
				self.check_alg2.set_active(True)
			elif i == "s":
				self.check_alg3.set_active(True)
			elif i == "c":
				self.check_alg4.set_active(True)
			elif i == "a":
				self.check_alg5.set_active(True)
