from infra.database.memory.models.programsModel import ProgramsModel


class ProgramsRepository:
    _instance = None
    _memory = None

    def __new__(cls, db=None):
        if cls._instance is None:
            cls._instance = super(ProgramsRepository, cls).__new__(cls)
        if db is not None:
                cls._instance._initialize(db)
        return cls._instance

    def _initialize(self, db):
        if not hasattr(self, 'db') or self.db is None:
            self.db = db
            if db == "memory":
                self._memory = ProgramsModel()

    def get_programs(self):
        if self.db == "memory":
            self._memory.get_programs()
        pass

    def find(self, query):
        if self.db == "memory":
            return self._memory.findByLocation(query)

    def get_program(self, program):
        pass

    def set_program(self, program):
        if self.db == "memory":
            program_mapped = self._map_object(program)
            self._memory.set_program(program_mapped)
        return True

    def delete_program(self, program):
        pass

    def update_program(self, program):
        pass

    def _map_object(self, program):
        formatted_object = {
            "location": program[1],
            "name": program[2],
            "start_at": program[3],
            "end_at": program[4],
        }
        return formatted_object
