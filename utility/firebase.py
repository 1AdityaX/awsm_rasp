import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class Firebase:
    def __init__(self, collection_name):
        cred = credentials.Certificate("D:\\test\\firebase\\creds.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client().collection(collection_name)

    
    def get_documents(self):
        return [i.to_dict() for i in self.db.get()]

    def get_document(self, document_name):
        return self.db.document(str(document_name)).get().to_dict()

    def set_document(self, document_name, data):
        ids = [data["id"] for data in self.get_documents()]
        if int(document_name) in ids:
            raise Exception("Document already exists")
        else:
            return self.db.document(document_name).set(data)
    
    def delete_document(self, document_name):
        return self.db.document(document_name).delete()
    
    def update_document(self, document_name, data):
        return self.db.document(document_name).update(data)

    def get_document_by_var(self, key, value):
        return [i.to_dict() for i in self.db.where(key, "==", value).get()]

    def get_document_by_name(self, name):
        return self.get_document_by_var("name", name)
        
    def get_document_by_class(self, doc_class):
        return self.get_document_by_var("class", doc_class)
    
    

