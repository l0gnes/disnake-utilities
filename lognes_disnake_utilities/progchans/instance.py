#from .container import ProgrammableChannelContainer
from typing import Union, List
from disnake import TextChannel, VoiceChannel
from .disposal_behavior import DisposalBehaviour

class ProgrammableChannelInstance(object):

    container           : "ProgrammableChannelContainer"
    channel             : Union[TextChannel, VoiceChannel]
    dispose_behavior    : DisposalBehaviour

    async def dispose(self):
        if self.dispose_behavior == DisposalBehaviour.NONE:
            return

        elif self.dispose_behavior == DisposalBehaviour.DEPERMIT:
            all_overwrites = self.channel.overwrites

            for user_or_role, _ in all_overwrites.items():
                await self.channel.set_permissions(
                    target      = user_or_role,
                    overwrite   = None
                )

        elif self.dispose_behavior == DisposalBehaviour.DESTROY:
            await self.channel.delete()

    @classmethod
    async def build(cls, container : "ProgrammableChannelContainer", channel : Union[TextChannel, VoiceChannel]) -> "ProgrammableChannelInstance":
        newInstance = cls()
        
        newInstance.container = container
        newInstance.channel = channel

        return newInstance