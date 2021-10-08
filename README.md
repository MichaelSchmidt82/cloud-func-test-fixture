# cloud-func-test-fixture
An HTTP cloud function test fixture.

### Use:
1) Open VS Code.
2) Write your code in `entrypoint.py` under the `test_fixture` function.
3) Go to the debug tile on the left.
4) Set breakpoints in the gutter and press debug -> "Debug fixture" or press `F5`.

### Requirements:
1) Docker installed and running
2) VS Code with Docker and Python extensions
3) obtain a credentials.json by creating an API key for the service account in the console.
4) Fill payload.json with the JSON payload of the incoming request.

### Configure:

1) Add, modify, or delete any environmental variables in `Dockerfile` with the `ENV` directive.  These variables can also be set in the cloud function configuration.  Access these variable in python using `os`.  E.g `os.environ.get('FOO')`.
