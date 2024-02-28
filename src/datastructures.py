"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        if member.get('id'):
           self._members.append(member)
        else: 
            member["id"] = self._generateId()  # Assign a unique ID to the member
            self._members.append(member)
        

    def delete_member(self, id):
        index_to_delete = None
        for i, member in enumerate(self._members):
            if member["id"] == id:
                index_to_delete = i
                break
        # If the member is found, remove it
        if index_to_delete is not None:
            del self._members[index_to_delete]

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None  # Return None if member not found
        
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
