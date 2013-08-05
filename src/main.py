#!/usr/bin/env python
# main loop of the program

from gi.repository import Gtk
from DataSetWindow import *
from PartitionWindow import *
from SimilarityWindow import *
from ExternalValidationWindow import *
from InternalValidationWindow import *
from AlgorithmWindow import *
from Clex_module import *
from subprocess import call
from os import path
from urlparse import urlparse 
import json
from datetime import datetime
import os, errno

class RealPartitionWindow(PartitionWindow):
	def __init__(self):
		PartitionWindow.__init__(self, title="Select Real Partitions")

class GeneratedPartitionWindow(PartitionWindow):
	def __init__(self):
		PartitionWindow.__init__(self, title="Select Generated Partitions")

class MainWindow(Gtk.Window):

	# Mount view elements
	def __init__(self):

		# Create a new window
		Gtk.Window.__init__(self, title="Clustering Experimenter")
		
		
		# Containers
		self.vbox = Gtk.VBox(spacing=6)
		self.vbox.set_border_width(10)
		self.vbox_general = Gtk.VBox(spacing=6)
		self.vbox_windows = Gtk.VBox(spacing=6)
		self.hbox = Gtk.HBox(spacing=6)

		# General Configuration Frame
		self.frame_general = Gtk.Frame(label="General Settings")
		self.hbox_expname = Gtk.HBox(spacing=6)
		self.hbox_expdir = Gtk.HBox(spacing=6)

		# Button Boxes
		self.bbox1 = Gtk.VButtonBox(spacing=6)
		self.bbox2 = Gtk.VButtonBox(spacing=6)
		self.bbox3 = Gtk.HButtonBox(spacing=6)
		self.bbox1.set_layout(Gtk.ButtonBoxStyle.START)
		self.bbox2.set_layout(Gtk.ButtonBoxStyle.START)
		self.bbox3.set_layout(Gtk.ButtonBoxStyle.START)
		
		# Algorithms Frame
		self.frame_algorithms = Gtk.Frame(label="Algorithms Preferences")
		self.bbox2a = Gtk.VBox(False, 0)##
		self.bbox2b = Gtk.HBox(False, 0)##
		self.separator = Gtk.HSeparator()
		self.hbox_minK = Gtk.HBox(spacing=6)
		self.hbox_maxK = Gtk.HBox(spacing=6)

		# Packing containers
		self.hbox.pack_start(self.bbox1, True, True, 0)
		self.hbox.pack_start(self.bbox2, True, True, 0)
		self.vbox_general.pack_start(self.hbox_expname, True, True, 0)
		self.vbox_general.pack_start(self.hbox_expdir, True, True, 0)
		self.vbox_windows.pack_start(self.hbox, True, True, 0)
		self.frame_algorithms.add(self.bbox2a)
		self.vbox_windows.pack_start(self.frame_algorithms, True, True, 0)##
		self.vbox_windows.pack_start(self.bbox3, True, True, 10)
		self.frame_general.add(self.vbox_general)
		self.vbox.pack_start(self.frame_general, True, True, 0)
		self.vbox.pack_start(self.vbox_windows, True, True, 0)
		self.add(self.vbox)

		# General configuration labels and inputs boxes
		self.label_name = Gtk.Label("Experiment name: ")
		self.entry_name = Gtk.Entry()
		self.label_dir = Gtk.Label("Directory: ")
		self.entry_dir = Gtk.Entry()

		self.hbox_expname.pack_start(self.label_name, True, True, 0)
		self.hbox_expname.pack_start(self.entry_name, True, True, 0)
		self.hbox_expdir.pack_start(self.label_dir, True, True, 0)
		self.hbox_expdir.pack_start(self.entry_dir, True, True, 0)

		# Buttons to open other windows
		self.button_dataset = Gtk.Button(label="DataSets")
		self.button_real_partition = Gtk.Button(label="Real Partitions")
		self.button_generated_partition = Gtk.Button(label="Generated Partitions")
		self.button_similarity = Gtk.Button(label="Set Similarity Measure")
		self.button_external_validation = Gtk.Button(label="Set External Validation Indexes")
		self.button_internal_validation = Gtk.Button(label="Set Internal Validation Indexes")
		self.button_algorithm = Gtk.Button(label="Set Algorithms")
		self.button_execute = Gtk.Button(stock=Gtk.STOCK_EXECUTE)
		self.button_save = Gtk.Button(stock=Gtk.STOCK_SAVE)
		self.button_open = Gtk.Button(stock=Gtk.STOCK_OPEN)
		self.button_close = Gtk.Button(stock=Gtk.STOCK_CLOSE)
		
		
		# Algorithms Parameters
		self.label_min_cluster = Gtk.Label("Min. Cluster number: ")
		self.spin_min_cluster = Gtk.SpinButton()
		self.spin_min_cluster.set_adjustment(Gtk.Adjustment(2, 2, 100, 1, 10, 0))
		self.spin_min_cluster.set_numeric(True)

		self.label_max_cluster = Gtk.Label("Max. Cluster number: ")
		self.spin_max_cluster = Gtk.SpinButton()
		self.spin_max_cluster.set_adjustment(Gtk.Adjustment(2, 2, 100, 1, 10, 0))
		self.spin_max_cluster.set_numeric(True)
		
		self.label_times = Gtk.Label("Times to execute\nnon-deterministic\nalgorithms: ")
		self.spin_times = Gtk.SpinButton()
		self.spin_times.set_adjustment(Gtk.Adjustment(30, 1, 100, 1, 10, 0))
		self.spin_times.set_numeric(True)
		
		self.hbox_minK.pack_start(self.label_min_cluster, True, False, 0)
		self.hbox_minK.pack_start(self.spin_min_cluster, True, False, 0)
		self.hbox_maxK.pack_start(self.label_max_cluster, True, False, 0)
		self.hbox_maxK.pack_start(self.spin_max_cluster, True, False, 0)

		# Connect the callback functions to the click event
		self.button_dataset.connect("clicked", self.on_button_dataset_clicked)
		self.button_real_partition.connect("clicked", self.on_button_real_partition_clicked, "Real")
		self.button_generated_partition.connect("clicked", self.on_button_generated_partition_clicked, "Generated")
		self.button_similarity.connect("clicked", self.on_button_similarity_clicked)
		self.button_external_validation.connect("clicked", self.on_button_external_validation_clicked)
		self.button_internal_validation.connect("clicked", self.on_button_internal_validation_clicked)
		self.button_algorithm.connect("clicked", self.on_button_algorithm_clicked)
		self.button_execute.connect("clicked", self.on_button_execute_clicked)
		self.button_save.connect("clicked", self.on_button_save_clicked)
		self.button_open.connect("clicked", self.on_button_open_clicked)
		self.button_close.connect("clicked", self.on_button_close_clicked)

		# put the buttons into the containers
		self.bbox1.pack_start(self.button_dataset, True, True, 6)
		self.bbox1.pack_start(self.button_real_partition, True, True, 0)
		self.bbox1.pack_start(self.button_generated_partition, True, True, 0)
		self.bbox2.pack_start(self.button_similarity, True, True, 0)
		self.bbox2.pack_start(self.button_external_validation, True, True, 0)
		self.bbox2.pack_start(self.button_internal_validation, True, True, 0)
		self.bbox2.pack_start(self.button_algorithm, True, True, 0)
		
		self.bbox2a.pack_start(self.hbox_minK, True, True, 4)##
		self.bbox2a.pack_start(self.hbox_maxK, True, True, 4)##
		self.bbox2a.pack_start(self.separator, True, True, 2)
		self.bbox2a.pack_start(self.bbox2b, True, True, 4)##
		self.bbox2b.pack_start(self.label_times, True, False, 0)
		self.bbox2b.pack_start(self.spin_times, True, False, 0)

		self.bbox3.pack_start(self.button_execute, True, True, 0)
		self.bbox3.pack_start(self.button_save, True, True, 0)
		self.bbox3.pack_start(self.button_open, True, True, 0)
		self.bbox3.pack_start(self.button_close, True, True, 0)

		# Create the other windows
		self.win_dataset = DataSetWindow()
		self.win_real_partition = RealPartitionWindow()
		self.win_generated_partition = GeneratedPartitionWindow()
		self.win_external_validation = ExternalValidationWindow()
		self.win_internal_validation = InternalValidationWindow()
		self.win_algorithm = AlgorithmWindow()
		self.win_similarity = SimilarityWindow()

	
	# Open window for selecting Datasets
	def on_button_dataset_clicked(self, widget):
		self.win_dataset.show_all()

	# Open window for selecting Real Partitions
	def on_button_real_partition_clicked(self, widget, data):
		self.dataset_list = self.win_dataset.get_selection_list()
		self.win_real_partition.set_dataset_list(self.dataset_list)
		self.win_real_partition.set_dataset_partition_dic(self.dataset_list)
		self.win_real_partition.show_all()

	# Open window for selecting Generated Partitions
	def on_button_generated_partition_clicked(self, widget, data):
		self.dataset_list = self.win_dataset.get_selection_list()
		self.win_generated_partition.set_dataset_list(self.dataset_list)
		self.win_generated_partition.set_dataset_partition_dic(self.dataset_list)
		self.win_generated_partition.show_all()

	# Open window for selecting External Validation Indexes to be used
	def on_button_external_validation_clicked(self, widget):
		self.win_external_validation.show_all()
		
	# Open window for selecting Internal Validation Indexes to be used
	def on_button_internal_validation_clicked(self, widget):
		self.win_internal_validation.show_all()
		
	# Open window for selecting Clustering Algorithms to be used
	def on_button_algorithm_clicked(self, widget):
		self.win_algorithm.show_all()

	# Open window for selecting Similarity Indexes to be used
	def on_button_similarity_clicked(self, widget):
		self.win_similarity.show_all()
	

	
	def get_minK(self):
		return self.spin_min_cluster.get_value_as_int()

	def get_maxK(self):
		return self.spin_max_cluster.get_value_as_int()

	def get_execution_times(self):
		return self.spin_times.get_value_as_int()
	
	# Return the time elapsed since the Experiment execution started
	def get_time(self):
		now = datetime.now()
		return ((now - self.begin_time).total_seconds())

	# Run the Experiment
	def on_button_execute_clicked(self, widget):

		print "......................................"
		print "\n[%.2fs] Starting Experiment..." % .0
		self.begin_time = datetime.now()

		# create directory tree for the experiment
		self.expname = self.entry_name.get_text()
		self.expdir = self.entry_dir.get_text()
		if(self.expname == ""):
			print "\n[%.2fs] Error: Experiment name not set" % self.get_time()
			return
		if(self.expdir == ""):
			print "\n[%.2fs] Error: Experiment directory not set" % self.get_time()
			return

		self.exppath = os.path.join(self.expdir, self.expname)
		try:
			os.makedirs(self.exppath)
		except OSError as exc:
			if exc.errno == errno.EEXIST and os.path.isdir(self.exppath):
				pass
			else: raise

		# instanciate Clex
		print "\n[%.2fs] Creating Clex instance..." % self.get_time()
		self.clex = Clex()
		print "[%.2fs] Clex instance created." % self.get_time()
		
		# instanciate Similarity Measures
		print "[%.2fs] Setting Similarity measure..." % self.get_time()
		self.win_similarity_list = self.win_similarity.get_similarity_param_list()

		if(self.win_similarity_list == []):
			print "[%.2fs] Error: No Similarities selected." % self.get_time()
			return

		self.similarity_list = StrVector(len(self.win_similarity_list))
		for i in range(0, len(self.similarity_list)):
			self.similarity_list[i] = self.similarity_list[i]
		self.clex.setSimilarity(self.similarity_list)
		print "[%.2fs] Similarity measures setted." % self.get_time()

		# instanciate DataSets
		print "\n[%.2fs] Loading DataSets..." % self.get_time()
		self.win_dataset_list = self.win_dataset.get_selection_list()
		if(self.win_dataset_list == []):
			print "[%.2fs] Error: No DataSets selected." % self.get_time()
			return

		self.dataset_list = StrPairVector(len(self.win_dataset_list))
		for i in range(0, len(self.dataset_list)):
			# split directory name from the filename
			self.head, self.tail = path.split(self.win_dataset_list[i][0])
			# cut 'file://' off, convert unicode to bytecode, and create a pair of strings
			self.dataset_list[i] = StrPair(urlparse(self.head).path.encode() + '/', self.tail.encode())
	
		self.clex.setDataSet(self.dataset_list)
		print "[%.2fs] DataSets loaded." % self.get_time()

		# instanciate External Validation Indexes
		print "\n[%.2fs] Setting External Validation Indexes..." % self.get_time()
		self.win_external_validation_list = self.win_external_validation.get_validation_list()
		if(self.win_external_validation_list == []):
			print "[%.2fs] No External Validation Indexes selected." % self.get_time()
		else:
			self.external_validation_list = StrVector(len(self.win_external_validation_list))
			for i in range(0, len(self.external_validation_list)):
				self.external_validation_list[i] = self.external_validation_list[i]
			self.clex.setExternalIndex(self.external_validation_list)
			print "[%.2fs] External Validation Indexes setted." % self.get_time()

		# instanciate Internal Validation Indexes
		print "\n[%.2fs] Setting Internal Validation Indexes..." % self.get_time()
		self.win_internal_validation_list = self.win_internal_validation.get_validation_list()

		if(self.win_internal_validation_list == []):
			print "[%.2fs] No Internal Validation Indexes selected." % self.get_time()
		else:
			self.internal_validation_list = StrVector(len(self.win_internal_validation_list))
			for i in range(0, len(self.internal_validation_list)):
				self.internal_validation_list[i] = self.internal_validation_list[i]
			self.clex.setInternalIndex(self.internal_validation_list)
		print "[%.2fs] Internal Validation Indexes setted." % self.get_time()

		# Clustering program
		print "\n[%.2fs] Running Clustering Algorithms..." % self.get_time()
		self.cluster_program = self.win_algorithm.get_clustering_program_path()

		# Prepare the calling strings
		self.call_list = []
		self.alg_param_list = self.win_algorithm.get_algorithm_param_list()

		if(self.alg_param_list== []):
			print "[%.2fs] No Clustering Algorithms selected." % self.get_time()
		else:
			self.minK = self.get_minK()
			self.maxK = self.get_maxK()
			self.times_to_run = self.get_execution_times()
			self.sim_list = self.win_similarity.get_similarity_param_list()
			for dataset in self.dataset_list:
				for alg_param in self.alg_param_list:

					# create directory for each dataset
					self.jobdir = os.path.join(self.exppath, dataset[1], "generatedPartition")
					try:
						os.makedirs(self.jobdir)
					except OSError as exc:
						if exc.errno == errno.EEXIST and os.path.isdir(self.jobdir):
							pass
						else: raise

					# K-means
					if (alg_param == "k"):
						for similarity in self.sim_list:
							for k in range(self.minK, self.maxK + 1):
								for r in range(1, self.times_to_run + 1):
									self.jobname = os.path.join(self.jobdir, "KM-" + similarity + "-k" + str(k) + "-r" + str(r))
									self.call_list.append([self.cluster_program, "-f", dataset[0] + dataset[1], "-g", similarity, "-k", str(k), "-r", str(r), "-u", self.jobname])

					# Hierarchical algorithm
					else:
						for similarity in self.sim_list:
							self.jobname = os.path.join(self.jobdir, alg_param + "-" + similarity)
							self.call_list.append([self.cluster_program, "-f", dataset[0] + dataset[1], "-m", alg_param, "-u", self.jobname])
						

			# Run the calling strings
			for call_string in self.call_list:
				print "[%.2fs] " % self.get_time() + ' '.join(call_string)
				call(call_string)
			print "[%.2fs] Clustering Algorithms completed running." % self.get_time()

		print "\n[%.2fs] Finished running Experiment." % self.get_time()
	
	
	# Save the Experiment Configuration to a file
	def on_button_save_clicked(self, widget):
		# Open output file
		self.savefilechooser = Gtk.FileChooserDialog("Please select saving path", self, Gtk.FileChooserAction.SAVE, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.OK))

		self.response = self.savefilechooser.run()
		if self.response != Gtk.ResponseType.OK:
			self.savefilechooser.destroy()
			return

		self.outuri = self.savefilechooser.get_uri()
		self.savefilechooser.destroy()

		if self.outuri == None:
			return

		outfile = open(urlparse(self.outuri).path, 'w')
		if ( outfile == None ):
			print 'Error while opening file ' + self.outuri
			return

		# Construct JSON structure
		# self.savedata = { 'ExperimentName': None, 'Directory': None, 'MinCluster': None, 'MaxCluster': None, 'ExecutionTimes': None, 'ShowTime': None, 'DataSet': [], 'RealPartition': [], 'GeneratedPartition': []}
		self.savedata =	{ 'ExperimentName': None, 'Directory': None, 'MinCluster': None, 'MaxCluster': None,
		'ExecutionTimes': None, 'SimilarityMeasure': [], 'ExternalValidationIndexes': [],
		'InternalValidationIndexes': [], 'Algorithms': [], 'DataSet': []}
		self.savedata["ExperimentName"] = self.entry_name.get_text()
		self.savedata["Directory"] = self.entry_dir.get_text()
		self.savedata["MinCluster"] = self.spin_min_cluster.get_value()
		self.savedata["MaxCluster"] = self.spin_max_cluster.get_value()
		self.savedata["ExecutionTimes"] = self.spin_times.get_value()
		self.savedata["SimilarityMeasure"] = self.win_similarity.get_similarity_param_list()
		self.savedata["ExternalValidationIndexes"] = self.win_external_validation.get_validation_list()
		self.savedata["InternalValidationIndexes"] = self.win_internal_validation.get_validation_list()
		self.savedata["Algorithms"] = self.win_algorithm.get_algorithm_param_list()
		self.savedata["DataSet"] = self.win_dataset.get_dataset_list()
		if len(self.win_real_partition.dataset_partition_dic) > 0:
			self.savedata["DataSet_RealPartition"] = self.win_real_partition.get_dataset_partition_dic()
		if len(self.win_generated_partition.dataset_partition_dic) > 0:
			self.savedata["DataSet_GeneratedPartition"] = self.win_generated_partition.get_dataset_partition_dic()
		# self.savedata["ShowTime"] = self.check_time.get_active()

		# Write to the file
		print "Saving Configuration..."
		print json.dumps(self.savedata)
		json.dump(self.savedata, outfile)
		outfile.close()
		print "Configuration Saved Successfully."

	# Load configuration from a previously saved file
	def on_button_open_clicked(self, widget):
		# Open input file
		self.openfilechooser = Gtk.FileChooserDialog("Please select saving path", self, Gtk.FileChooserAction.OPEN, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

		self.response = self.openfilechooser.run()
		if self.response != Gtk.ResponseType.OK:
			self.openfilechooser.destroy()
			return

		self.inuri = self.openfilechooser.get_uri()
		self.openfilechooser.destroy()

		if self.inuri == None:
			return

		infile = open(urlparse(self.inuri).path, 'r')
		if ( infile == None ):
			print "Error while opening file " + self.inuri
			return

		# Construct JSON structure from the read file
		print "Loading Configuration..."
		self.readdata = json.load(infile)

		# Set the attributes recovered from the file
		print json.dumps(self.readdata)
		self.entry_name.set_text(self.readdata["ExperimentName"])
		self.entry_dir.set_text(self.readdata["Directory"])
		self.spin_min_cluster.set_value(self.readdata["MinCluster"])
		self.spin_max_cluster.set_value(self.readdata["MaxCluster"])
		self.spin_times.set_value(self.readdata["ExecutionTimes"])
		self.win_similarity.set_loaded_settings(self.readdata["SimilarityMeasure"])
		self.win_external_validation.set_loaded_settings(self.readdata["ExternalValidationIndexes"], "External")
		self.win_internal_validation.set_loaded_settings(self.readdata["InternalValidationIndexes"], "Internal")
		self.win_algorithm.set_loaded_settings(self.readdata["Algorithms"])
		self.win_dataset.set_loaded_settings(self.readdata["DataSet"])
		self.win_real_partition.set_dataset_list(self.win_dataset.get_selection_list())
		self.win_generated_partition.set_dataset_list(self.win_dataset.get_selection_list())
		self.win_real_partition.clean_settings()
		self.win_generated_partition.clean_settings()
		if self.readdata.has_key("DataSet_RealPartition"):
			self.win_real_partition.set_loaded_settings(self.readdata["DataSet_RealPartition"])
		if self.readdata.has_key("DataSet_GeneratedPartition"):
			self.win_generated_partition.set_loaded_settings(self.readdata["DataSet_GeneratedPartition"])
		# self.check_time.set_active(self.readdata["ShowTime"])

		infile.close()
		print "Configuration Loaded Successfully."

	# Quit the program
	def on_button_close_clicked(self, widget):
		Gtk.main_quit()

# Main execution
win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
