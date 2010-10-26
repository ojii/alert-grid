class AlertGridBaseException(Exception): pass
class AlertGridURLError(AlertGridBaseException): pass
class UnknownError(AlertGridBaseException): pass
class ReceiverNameMissing(AlertGridBaseException): pass
class ApiIdMissing(AlertGridBaseException): pass
class ReceiverDoesNotExist(AlertGridBaseException): pass
class ReceiverNotEnabled(AlertGridBaseException): pass
class InvalidApiId(AlertGridBaseException): pass

ERRORS = {
    '0': UnknownError,
    '11': ReceiverNameMissing,
    '12': ApiIdMissing,
    '21': ReceiverDoesNotExist,
    '22': ReceiverNotEnabled,
    '31': InvalidApiId
}