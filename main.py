import asyncio
import websockets


REGISTERS = ["0", "0", "0", "0", "0", "0", "0", "0"]

async def stuff(websocket):
	global REGISTERS

	async for request in websocket:

		if request == 'read':

			await websocket.send(''.join(REGISTERS))
			print(f'READ!: {' - '.join(REGISTERS)}')

		else:

			REGISTERS = list(request)[0:8]
			await websocket.send('ok')
			print(f'WRITTEN!: {' - '.join(REGISTERS)}')


async def main():
	async with websockets.serve(stuff, "0.0.0.0", 8765):
		await asyncio.Future()  # run forever

if __name__ == "__main__":
	asyncio.run(main())