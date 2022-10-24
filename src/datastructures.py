
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
import json
from flask import Flask, request, jsonify, url_for

class FamilyStructure:

    def __init__(self, last_name):
        # Recibe un String, corresponde al apellido de la familia.
        self.last_name = last_name

        # Se guardan los miembros
        self._members = [{
            "id":self._generateId(),
            "first_name": "John",
             "last_name": last_name,
             "age": "33 years old",
             "lucky_numbers": [7, 13, 22]
        },{
            "id":self._generateId(),
            "first_name": "Jane",
             "last_name": last_name,
             "age":"35 years old",
             "lucky_numbers": [10, 14, 3]
        },{
            "id":self._generateId(),
            "first_name": "Jimmy",
             "last_name": last_name,
             "age": "5 years old",
             "lucky_numbers": [1]
        }]

    # Se genera el ID de forma random de los miembros
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Agregar un miembro de la familia


        return self._members.append({
            "id":self._generateId(),
            "first_name": member["first_name"],
             "last_name": self.last_name,
             "age": str(member["age"])+" years old",
             "lucky_numbers": member["lucky_numbers"]
        })

    def delete_member(self, id):
        # Borrar un miembro de la familia
        num = -1
            
            
        for content in self._members:
            num = num+1
            bool = False
               
            if content["id"]== id:
                self._members.pop(num)
                bool = True
                break
        
        return bool
               
                  
            

                    
                
            
     # Obtener un miembro de la familia            

    def get_member(self, id):
        num = -1
        obj = ""
        for content in self._members:
            num = num+1
            
            if content["id"]== id:
                obj = self._members[num]
                bool = True
                break
        return obj    

    # Lista con todos los miembros de la familia
    def get_all_members(self):
        return self._members

    
