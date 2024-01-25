""" Requires SoftTimeOutAddOn and APIError from python-documentcloud """
from documentcloud.addon import SoftTimeOutAddOn
from documentcloud.exceptions import APIError


class BulkDelete(SoftTimeOutAddOn):
    """ DocumentCloud Add-On to bulk delete documents"""
    def main(self):
        """ Checks that the user confirmed 
        and then deletes the documents that they are authorized to delete."""
        confirm = self.data.get("confirm")
        if confirm is not None and confirm is True:
            for document in self.get_documents():
                try:
                    document.delete()
                except APIError: # If user does not have permissions to delete the document, skip.
                    pass
        else:
            self.set_message("You did not confirm, this Add-On did nothing.")


if __name__ == "__main__":
    BulkDelete().main()
