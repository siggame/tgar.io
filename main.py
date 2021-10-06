if __name__ == "__main__":
  async def main():
    while True:
      print(await agetch())

      loop.create_task(main())
      loop.run_forever