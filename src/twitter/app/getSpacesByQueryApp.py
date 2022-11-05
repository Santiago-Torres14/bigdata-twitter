from src.twitter import domain, infra
from src.shared import databaseConnection


class GetSpacesByQueryApp:

    def getSpacesByQuery(query: str) -> list:
        spaceCollection = databaseConnection['space']
        spaces = infra.GetSpacesByQuery().getSpacesByQuery(query=query)

        spacesDict = list()
        for space in spaces:
            spaceDict = domain.model.Spaces.slotted_to_dict(space)
            spaceDict.update(query=query)
            spacesDict.append(spaceDict)

        return spaceCollection.insert_many(spacesDict).inserted_ids
