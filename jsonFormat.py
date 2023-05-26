class jsonFormat():
    
    def __init__(self, j: dict or list = dict(), showComment: bool = True) -> None:
        self.change(j, showComment)

    @classmethod
    def getVersion(cls) -> str:
        return "1.0.1"

    def change(self, j: dict or list = dict(), showComment: bool = True) -> None:
        self.__jsonStr = j
        self.__showComment = showComment
    
    def get(self) -> str:
        jsonType = type(self.__jsonStr)
        if (jsonType is set or jsonType is tuple): self.__jsonStr = list(self.__jsonStr)
        s = ""
        if (type(self.__jsonStr) is dict):
            for item in self.__dictToJsonFormat(self.__jsonStr, self.__showComment):
                s += item
            # return self.__dictToJsonFormat(self.__jsonStr, self.__showComment)
        elif (type(self.__jsonStr) is list):
            for item in self.__listToJsonFormat(self.__jsonStr, self.__showComment):
                s += item
            # return self.__listToJsonFormat(self.__jsonStr, self.__showComment)
        return s

    def __dictPrintJson(self, jsonObject: dict, showComment: bool = False, tabFormat: int = 1) -> None: # not used
        if ( (not isinstance(jsonObject, dict)) 
            or (not isinstance(showComment, bool)) 
            or (not isinstance(tabFormat, int))): return
        print( ("{\n") if (tabFormat == 1) else "", end = "")
        count = len(jsonObject.keys())
        for index, key in enumerate(jsonObject.keys()):
            if ( (key[0:2] == "//" or key[0:3] == "//_") and 
                (not showComment) ):
                continue
            jsonType = type(jsonObject[key])

            if (jsonType is int or jsonType is float or jsonType is bool or jsonType is None):
                print("\t" * tabFormat + f"\"{key}\" : {jsonObject[key]}" + ("," if (count - 1 != index) else ""))

            elif (jsonType is str):
                print("\t" * tabFormat + f"\"{key}\" : \"{jsonObject[key]}\"" + ("," if (count - 1 != index) else ""))
                
            elif (jsonType is dict):
                print("\t" * tabFormat + f"\"{key}\" : {{")
                self.dictPrintJson(jsonObject[key], showComment, (tabFormat + 1))
                print("\t" * tabFormat + "}" + ("," if (count - 1 != index) else ""))
                
            elif (jsonType is list):
                print("\t" * tabFormat + f"\"{key}\" : [")
                self.listPrintJson(jsonObject[key], showComment, (tabFormat + 1))
                print("\t" * tabFormat + "]" + ("," if (count - 1 != index) else ""))

        print( ("}\n") if (tabFormat == 1) else "", end = "")

    def __listPrintJson(self, jsonArray: list, showComment: bool = False, tabFormat: int = 1) -> None: # not used
        if ( (not isinstance(jsonArray, list)) 
            or (not isinstance(showComment, bool)) 
            or (not isinstance(tabFormat, int))): return
        print( ("[\n") if (tabFormat == 1) else "", end = "")
        count = len(jsonArray)
        for index, value in enumerate(jsonArray):
            jsonType = type(value)

            if (jsonType is int or jsonType is float or jsonType is bool or jsonType is None):
                print("\t" * tabFormat + f"{value}" + "," if (count - 1 != index) else "")
                pass
            elif (jsonType is str):
                if ( (value[0:2] == "//" or value[0:3] == "//_") and 
                    (not showComment) ):
                    continue
                print("\t" * tabFormat + f"\"{value}\"" + ("," if (count - 1 != index) else ""))
                
            elif (jsonType is dict):
                print("\t" * tabFormat + "{")
                self.dictPrintJson(value, showComment, (tabFormat + 1))
                print("\t" * tabFormat + "}" + ("," if (count - 1 != index) else ""))
                
            elif (jsonType is list):
                print("\t" * tabFormat + "[")
                self.listPrintJson(value, showComment, (tabFormat + 1))
                print("\t" * tabFormat + "]" + ("," if (count - 1 != index) else ""))

        print( ("]\n") if (tabFormat == 1) else "", end = "")

    def __dictToJsonFormat(self, jsonObject: dict, showComment: bool = False, tabFormat: int = 1) -> str:
        if ( (not isinstance(jsonObject, dict)) 
            or (not isinstance(showComment, bool)) 
            or (not isinstance(tabFormat, int))): return
        yield ("{\n") if (tabFormat == 1) else ""
        count = len(jsonObject.keys())
        for index, key in enumerate(jsonObject.keys()):
            if ( (key[0:2] == "//" or key[0:3] == "//_") and 
                (not showComment) ):
                continue
            jsonType = type(jsonObject[key])

            if (jsonType is int or jsonType is float or jsonType is None):
                yield "\t" * tabFormat + f"\"{key}\" : {jsonObject[key]}" + (",\n" if (count - 1 != index) else "\n")

            elif (jsonType is bool):
                yield "\t" * tabFormat + f"\"{key}\" : {str(jsonObject[key]).lower()}" + (",\n" if (count - 1 != index) else "\n")

            elif (jsonType is str):
                yield "\t" * tabFormat + f"\"{key}\" : \"{jsonObject[key]}\"" + (",\n" if (count - 1 != index) else "\n")
                
            elif (jsonType is dict):
                yield "\t" * tabFormat + f"\"{key}\" : {{\n"
                for item in self.__dictToJsonFormat(jsonObject[key], showComment, (tabFormat + 1)):
                    yield item
                yield "\t" * tabFormat + "}" + (",\n" if (count - 1 != index) else "\n")
                
            elif (jsonType is list):
                yield "\t" * tabFormat + f"\"{key}\" : [\n"
                for item in self.__listToJsonFormat(jsonObject[key], showComment, (tabFormat + 1)):
                    yield item
                yield "\t" * tabFormat + "]" + (",\n" if (count - 1 != index) else "\n")

        yield ("}") if (tabFormat == 1) else ""

    def __listToJsonFormat(self, jsonArray: list, showComment: bool = False, tabFormat: int = 1) -> str:
        if ( (not isinstance(jsonArray, list)) 
            or (not isinstance(showComment, bool)) 
            or (not isinstance(tabFormat, int))): return
        yield ("[\n") if (tabFormat == 1) else ""
        count = len(jsonArray)
        for index, value in enumerate(jsonArray):
            jsonType = type(value)

            if (jsonType is int or jsonType is float or jsonType is None):
                # print("\t" * tabFormat + f"{value}" + "," if (count - 1 != index) else "")
                yield "\t" * tabFormat + f"{value}" + ",\n" if (count - 1 != index) else "\n"

            elif (jsonType is bool):
                yield "\t" * tabFormat + f"{str(value).lower()}" + ",\n" if (count - 1 != index) else "\n"

            elif (jsonType is str):
                if ( (value[0:2] == "//" or value[0:3] == "//_") and 
                    (not showComment) ):
                    continue
                # print("\t" * tabFormat + f"\"{value}\"" + ("," if (count - 1 != index) else ""))
                yield "\t" * tabFormat + f"\"{value}\"" + (",\n" if (count - 1 != index) else "\n")
                
            elif (jsonType is dict):
                # print("\t" * tabFormat + "{")
                yield "\t" * tabFormat + "{\n"
                # self.dictPrintJson(value, showComment, (tabFormat + 1))
                for item in self.__dictToJsonFormat(value, showComment, (tabFormat + 1)):
                    yield item
                # print("\t" * tabFormat + "}" + ("," if (count - 1 != index) else ""))
                yield "\t" * tabFormat + "}" + (",\n" if (count - 1 != index) else "\n")
                
            elif (jsonType is list):
                # print("\t" * tabFormat + "[")
                yield "\t" * tabFormat + "[\n"
                # self.listPrintJson(value, showComment, (tabFormat + 1))
                for item in self.__listToJsonFormat(value, showComment, (tabFormat + 1)):
                    yield item
                # print("\t" * tabFormat + "]" + ("," if (count - 1 != index) else ""))
                yield "\t" * tabFormat + "]" + (",\n" if (count - 1 != index) else "\n")

        # print( ("]\n") if (tabFormat == 1) else "", end = "")
        yield ("]") if (tabFormat == 1) else ""
