from disnake import (
    CategoryChannel,
    PermissionOverwrite, 
    TextChannel, 
    VoiceChannel, 
    User, 
    Member,
    Role
)
from typing import List, Union
from asyncio import Queue
from .disposal_behavior import DisposalBehaviour
from .instance import ProgrammableChannelInstance
from time import time
from .templates import TemplatesHandler

class ProgrammableChannelContainer(object):

    category                    : CategoryChannel
    channel_list                : List[ProgrammableChannelInstance]         = []
    disposal                    : Queue                                     = Queue()
    default_disposal_behavior   : DisposalBehaviour                         = DisposalBehaviour.NONE
    channel_template            : str                                       = "room-%(shorthextime)s"
    templates_handler           : TemplatesHandler                          = TemplatesHandler

    use_batch_disposal          : bool                                      = False


    def __construct(
        self, 
        category        : CategoryChannel,
        *,
        use_batching    : bool              = False
    ) -> "ProgrammableChannelContainer":

        self.category               = category
        self.use_batch_disposal     = use_batching
        return self



    @classmethod
    def using_category(cls, category : CategoryChannel) -> "ProgrammableChannelContainer":
        return cls().__construct(category)



    async def __construct_new_empty_instance(self) -> "ProgrammableChannelInstance":

        newChannel = await self.category.create_text_channel(
            name = self.channel_template % TemplatesHandler.fetch_formatting()
        )

        return ProgrammableChannelInstance.build(
            channel     = newChannel,
            container   = self
        )



    async def create_new_instance_for(
        self,
        users   : List[Union[User, Member, Role]]
    ) -> "ProgrammableChannelInstance":
        newInstance = await self.__construct_new_empty_instance()

        for user in users:

            newInstance.channel.set_permissions(
                target = user,
                overwrite = PermissionOverwrite(read_messages=True)
            )

        return newInstance

