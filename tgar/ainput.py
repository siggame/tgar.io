import platform
import asyncio

loop = asyncio.get_event_loop()

if platform.system() == "Windows":
    import msvcrt

    async def agetch() -> bytes:
        return await loop.run_in_executor(None, msvcrt.getch)

    def start(mainfn):
        # Intentionally a noop. Included for linux compat
        return mainfn

elif platform.system() == "Linux":
    import tty
    import termios
    import contextlib
    
    async def agetch() -> bytes:
        pass
        
    @contextlib.contextmanager
    def ainput(mainf):
        try:
            # TODO start terminal environment
            yield mainf
        finally:
            # TODO restore terminal environment
            pass


else:
    raise Exception("Unsupported platform")


if __name__ == "__main__":
    async def main():
        while True:
            print(await agetch())

    loop.create_task(main())
    loop.run_forever()