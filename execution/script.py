import module as module

print('This is the script calling a module')

print('Execution mode for script - value of __name__:',repr(__name__))

#Running whole workflow from module:
print('Running whole workflow:')
module.main()

#Running selected functions() from module
inputdata = 'Input custom data'
print('Running parts of the workflow for data',inputdata)

modified_data=module.process_data(inputdata)
module.write_data_to_database(modified_data)
