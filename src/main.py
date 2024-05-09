from infra.repositories.programs.programsRepository import ProgramsRepository
from interface.batchFiles.files.fileController import FileController
from interface.stdin.console.consoleController import ConsoleController

def main():
    ProgramsRepository("memory")
    FileController().execute()
    # ConsoleController().execute()

if __name__ == "__main__":
    main()
