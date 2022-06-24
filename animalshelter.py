# create method to create

def create(self, data):
	if data is not None:
		#self.database.animals.insert(data)
		insert_result = self.database.animals.insert(data)

		if insert_result is not None:
			status = True
		else:
			status = False
		return status
	else:
		raise Exception("Parameter is empty")

# create method for read

def read(self, data):
	if data is not None:
		animalsCollection = self.database.animals.find(data)
		#return animalsCollection
		#print animalsCollection cursor
		for aniumals in animalsCollection:
			print(animals)
		else:
			raise Exception("Search criteria not provided")

# create method for update

def update(self, query, record):
	if record is not None:
		update_result = self.database.animals.update_many(query, record)
		result= "Documents updated: " + json.dumps(update_result.modified_count)
		return result
	else:
		raise Exception("No record found")

# create method to delete

def delete(self, data):
	if data is not None:
		delete_result = self.database.animals.delete_many(data)
		result = "documents deleted: " + json.dumps(delete_result.deleted_count)
		return result
	else:
		raise Exception("Record not provided")