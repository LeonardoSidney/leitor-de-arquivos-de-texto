from infra.repositories.programs.programsRepository import ProgramsRepository


def insertNewEntryService(program):
    Program = ProgramsRepository()
    return Program.set_program(program)
