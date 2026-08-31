import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ProjectConsumer(AsyncWebsocketConsumer):
    """
    Handles real-time communication for a project.

    Users connected to the same project room
    can receive real-time updates.
    """

    async def connect(self):

        # URL बाट project_id प्राप्त हुन्छ।
        self.project_id = self.scope[
            "url_route"
        ][
            "kwargs"
        ][
            "project_id"
        ]

        self.room_group_name = (
            f"project_{self.project_id}"
        )

        # Add this WebSocket connection
        # to the project group.
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Send connection confirmation.
        await self.send(
            text_data=json.dumps({
                "type": "connection",
                "message": "Connected to project room.",
            })
        )

    async def disconnect(self, close_code):

        # Remove user from project group.
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(
        self,
        text_data
    ):

        try:

            data = json.loads(
                text_data
            )

            message = data.get(
                "message",
                ""
            )

            # Broadcast message to everyone
            # connected to the same project.
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "project_message",
                    "message": message,
                }
            )

        except json.JSONDecodeError:

            await self.send(
                text_data=json.dumps({
                    "type": "error",
                    "message": "Invalid JSON.",
                })
            )

    async def project_message(
        self,
        event
    ):

        await self.send(
            text_data=json.dumps({
                "type": "project_message",
                "message": event["message"],
            })
        )