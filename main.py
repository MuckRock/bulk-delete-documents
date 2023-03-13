from documentcloud.addon import AddOn, SoftTimeOutAddOn
class BulkDelete(SoftTimeOutAddOn):
    def main(self):
        for document in self.get_documents():
            document.delete()

if __name__ == "__main__":
    BulkDelete().main()
