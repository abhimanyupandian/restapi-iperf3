class Cache(object):
    """Cache stores the registered Server/Client objects and allows
    switching between them using user given aliases.
    """

    def __init__(self):
        self._aliases = dict()

    def register(self, connection, alias):
        """Registers an alias with the given connection/object.
        """
        if type(alias) is str:
            self._aliases[alias] = connection
        return alias

    def get_aliases(self):
        """Returns all the aliases available.
        """
        return self._aliases.keys()

    def get_connection(self, alias):
        """Get the connection specified by the given alias or index.
        """
        try:
            return self._aliases[str(alias)]
        except ValueError:
            raise RuntimeError("Non-existing alias/component '%s'."
                               % alias)

    __getitem__ = get_connection

    def close_all(self, closer_method='close'):
        """Closes connections using given closer method and empties cache.
        """
        self.empty_cache()

    def empty_cache(self):
        """Empties the connection cache.
        """
        self._aliases = dict()

class UnmatchingConnectionType(Exception):
 
    def __init__(self, alias):
        self.message = "The connection is incompatible with the alias '" + alias + "'" 
 
    def __str__(self):
        return(repr(self.message))

