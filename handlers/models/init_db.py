from setting import db
from handlers.models.user import UserModel
from handlers.models.message import MessageModel
from handlers.models.ranklog import RanklogModel
from handlers.models.system import SystemModel
from handlers.models.chanllage import ChanllageModel
from handlers.models.hintmodel import HintModel
from handlers.models.type import TypeModel

if __name__ == '__main__':
    db.create_tables([UserModel, MessageModel, SystemModel, TypeModel,
                      ChanllageModel, RanklogModel, HintModel, RanklogModel])
