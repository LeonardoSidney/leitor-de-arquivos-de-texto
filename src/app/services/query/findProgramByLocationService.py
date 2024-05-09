from infra.repositories.programs.programsRepository import ProgramsRepository


def findProgramByLocationService(location, hour):
    program = ProgramsRepository()
    query = _formatQuery(location, hour)
    return program.find(query)

def _formatQuery(location, hour):
    return {
        "location": location,
        "hour": hour,
    }
