from src.twitter import domain, infra
from src.shared import databaseConnection


class GetSpacesByQueryApp:

    def getSpacesByQuery(query: str) -> list:
        spaceCollection = databaseConnection['space']
        spaces = infra.GetSpacesByQuery().getSpacesByQuery(query=query)

        spacesDict = list()
        for space in spaces:
            spaceDict = space.slotted_to_dict()
            spaceDict.update(query=query)
            spacesDict.append(spaceDict)

        return spaceCollection.insert_many(spacesDict).inserted_ids
