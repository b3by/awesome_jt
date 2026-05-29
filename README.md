# awesome_jt
Collection of juturna plugins.

## Install the plugins
When working on a project that uses Juturna, you can install the plugins
included in this repository using `pip`:

```console
$ pip install https://github.com/b3by/awesome_jt
```

As an example, an optional group was created in the project, called
`proc`. Dependency groups can be used to prevent the repository from pulling
all the dependencies of the included nodes. To install selective groups, run:

```console
$ pip install "awesome-jt[proc] @ https://github.com/b3by/awesome_jt/archive/main.zip"
```

Alternatively, clone the repository locally and install it:

```console
$ git clone https://github.com/b3by/awesome_jt
$ pip install ./awesome_jt
$ pip install "./awesome_jt[proc]"
```

## Import the plugins

Once installed, plugins are available straight into your interpreter.

```python
from juturna.contrib.anto.nodes import proc as anto_proc


generator = anto_proc.MatrixGenerator(...)
```

Installed plugins are also listed in the pipeline creator tool.
