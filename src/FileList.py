from gi.repository import Gtk

class FileList(Gtk.HBox):
	def __init__(self, string, showListControl):
		Gtk.HBox.__init__(self)

		self.frame = Gtk.Frame()
		self.listcontrolbox = Gtk.VButtonBox(False, 4)
		self.listcontrolbox.set_layout(Gtk.ButtonBoxStyle.START)

		# models for the lists of files
		self.store = Gtk.ListStore(str)
		self.temp_store = Gtk.ListStore(str)
		self.status = False

		# view for the list of files
		self.treeview = Gtk.TreeView(self.store)
		self.renderer = Gtk.CellRendererText()
		self.column = Gtk.TreeViewColumn(string + " file name", self.renderer, text=0)
		self.treeview.append_column(self.column)

		
		self.selection = self.treeview.get_selection()
		if showListControl == True:
			self.selection.set_mode(Gtk.SelectionMode.MULTIPLE)
		else:
			self.selection.set_mode(Gtk.SelectionMode.SINGLE)
		self.selection.connect("changed", self.on_tree_selection_changed, showListControl)

		if showListControl == True:
		    # buttons to control the list
		    self.button_add = Gtk.Button(stock=Gtk.STOCK_ADD)
		    self.button_rm = Gtk.Button(stock=Gtk.STOCK_REMOVE)
		    self.button_clear = Gtk.Button(stock=Gtk.STOCK_CLEAR)
            
		    self.button_add.connect("clicked", self.on_button_add_clicked, string)
		    self.button_rm.connect("clicked", self.on_button_rm_clicked, string)
		    self.button_clear.connect("clicked", self.on_button_clear_clicked, string)
            
		    self.listcontrolbox.pack_start(self.button_add, True, False, 0)
		    self.listcontrolbox.pack_start(self.button_rm, True, False, 0)
		    self.listcontrolbox.pack_start(self.button_clear, True, False, 0)
		    
		self.frame.add(self.treeview)
		#self.pack_start(self.treeview, True, True, 0)
		self.pack_start(self.frame, True, True, 0)
		self.pack_start(self.listcontrolbox, False, False, 0)
		

	def on_tree_selection_changed(self, selection, control):
		if control == True:
			self.treemodel, self.selected = selection.get_selected_rows()
		else:
			self.treemodel, self.selected = selection.get_selected()
			# if self.partition_window.is_open == True:
			self.partition_window.update_selected_dataset(self.treemodel.get_value(self.selected, 0))

	def on_button_add_clicked(self, widget, string):
		self.filechooser = Gtk.FileChooserDialog("Please select files", None, Gtk.FileChooserAction.OPEN, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
		self.filechooser.set_select_multiple(self);
		if self.filechooser.run() == Gtk.ResponseType.OK:
		    for i in self.filechooser.get_uris():
			    self.store.append([i])
		self.filechooser.destroy()
		if string == "Partition":
			self.partition_window.update_dataset_partition_dic()

	def on_button_rm_clicked(self, widget, string):
		self.model, self.pathlist = self.selection.get_selected_rows()
		if self.pathlist == []:
			self.message_warning = Gtk.MessageDialog(None, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, "Empty List!")
			self.message_warning.format_secondary_text("There is no selected items or no items at all to delete!")
			self.message_warning.run()
			self.message_warning.destroy()
		else:
			self.message_remove = Gtk.MessageDialog(None, 0, Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, "Are you sure?")
			self.message_remove.format_secondary_text("This action will delete the selected items from list!")
			iters = [self.treemodel.get_iter(path) for path in self.selected]
			if self.message_remove.run() == Gtk.ResponseType.YES:
				for iter in iters:
					value = self.treemodel.get_value(iter, 0)
					print value
					self.treemodel.remove(iter)
			self.message_remove.destroy()
			if string == "Partition":
				self.partition_window.update_dataset_partition_dic()


	def on_button_clear_clicked(self, widget, string):
		if len(self.store) == 0:
			self.message_warning = Gtk.MessageDialog(None, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, "Empty List!")
			self.message_warning.format_secondary_text("There is nothing to delete!")
			self.message_warning.run()
			self.message_warning.destroy()
		else:
			self.message_clear = Gtk.MessageDialog(None, 0, Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, "Are you sure?")
			self.message_clear.format_secondary_text("This action will delete all items from list!")
			if self.message_clear.run() == Gtk.ResponseType.YES:
					self.store.clear()
			self.message_clear.destroy()
			if string == "Partition":
				self.partition_window.update_dataset_partition_dic()

	# def select_first_dataset(self, dataset):
	# 	self.selection.select_iter(dataset)


	def set_partition_window_instance(self, part_win):
		self.partition_window = part_win
