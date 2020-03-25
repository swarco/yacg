"""Reads JSON schema files and build the model types from it"""

from yacg.builder.impl.dictionaryBuilder import extractTypes, getParsedSchemaFromJson


def getModelFromJson(modelFile):
    """reads a JSON schema file and build a model from it, 
    returns a list of yacg.model.model.Type objects
    
    
    Keyword arguments:
    modelFile -- file name and path to the model to load
    """

    parsedSchema = getParsedSchemaFromJson(modelFile)
    return extractTypes (parsedSchema,modelFile)
