<div align="center">

# 🧰 rkit

**Your personal toolbox, compiled into a single Rust binary.**

Drop a `.rs` file in a folder. Recompile. Run it with `rkit <folder> <file>`.
No registration, no boilerplate, no glue code.

[![CI](https://github.com/YOUR_USERNAME/rkit/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/rkit/actions)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Rust](https://img.shields.io/badge/rust-stable-orange.svg)](https://www.rust-lang.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

```console
$ rkit docker stop
Stopping all running containers...

$ rkit docker
clean            Remove stopped containers and dangling images
stop             Stop all running containers

$ rkit
docker/
git/
```

---

## Why rkit?

Everyone ends up with a messy folder of personal scripts: `stop.sh`, `clean.py`, `sync`, `deploy_final_v2.sh`... Hard to remember, hard to share, hard to maintain.

**rkit** turns that folder into a real CLI:

- 🗂️ **Your folder structure *is* your command structure.** `commands/docker/stop.rs` becomes `rkit docker stop`.
- ⚡ **Zero registration.** A `build.rs` script scans `commands/` at compile time and generates the whole dispatch table for you.
- 📦 **One static binary.** Copy it to a server, a colleague's laptop, or a Docker image. Done.
- 🦀 **Everything is Rust.** Share code between commands, use any crate from crates.io, get type checking and speed for free.
- 🔍 **Self-documenting.** Every command exposes a one-line description, shown automatically when you list a folder.

---

## Installation

### From source

```bash
git clone https://github.com/YOUR_USERNAME/rkit.git
cd rkit
cargo install --path .
```

Make sure `~/.cargo/bin` is in your `PATH`:

```bash
export PATH="$HOME/.cargo/bin:$PATH"
```

### Quick check

```bash
rkit
```

You should see the list of top-level command folders.

---

## Usage

```text
rkit                      # list top-level folders and commands
rkit <folder>             # list the contents of a folder
rkit <folder> <command>   # run a command
rkit <folder> <command> [args...]   # run a command with arguments
```

Examples:

```bash
rkit docker stop
rkit docker clean --all
rkit git sync origin main
```

Any arguments after the command name are passed to the command as-is. The exit code of the command becomes the exit code of `rkit`, so it composes well in shell scripts and CI.

---

## How it works

```text
commands/                         rkit
├── docker/                       ├── docker
│   ├── stop.rs        ───────►   │   ├── stop
│   └── clean.rs                  │   └── clean
└── git/                          └── git
    └── sync.rs                       └── sync
```

1. At compile time, `build.rs` walks the `commands/` directory.
2. It generates a nested module tree (`docker::stop`, `git::sync`, ...) and a static table mapping names to functions.
3. At runtime, `main.rs` walks that table using your CLI arguments until it reaches a command, then calls its `run` function.

There is no reflection and no runtime file lookup: dispatch is a plain static lookup, so startup is instant.

---

## Writing a command

A command is a single `.rs` file exposing **two items**:

```rust
pub const DESC: &str = "One-line description shown in listings";

pub fn run(args: &[String]) -> i32 {
    // your logic here
    0 // exit code
}
```

### Example: `commands/docker/stop.rs`

```rust
use std::process::Command;

pub const DESC: &str = "Stop all running containers";

pub fn run(_args: &[String]) -> i32 {
    let status = Command::new("sh")
        .args(["-c", "docker stop $(docker ps -q)"])
        .status();

    match status {
        Ok(s) => s.code().unwrap_or(1),
        Err(e) => {
            eprintln!("error: {e}");
            1
        }
    }
}
```

### Example: `commands/git/sync.rs`

```rust
use std::process::Command;

pub const DESC: &str = "Pull with rebase, then push";

pub fn run(args: &[String]) -> i32 {
    let remote = args.first().map(String::as_str).unwrap_or("origin");
    let branch = args.get(1).map(String::as_str).unwrap_or("main");

    for cmd in [["pull", "--rebase", remote, branch], ["push", remote, branch]] {
        match Command::new("git").args(cmd).status() {
            Ok(s) if s.success() => {}
            Ok(s) => return s.code().unwrap_or(1),
            Err(e) => {
                eprintln!("error: {e}");
                return 1;
            }
        }
    }
    0
}
```

Then just rebuild:

```bash
cargo install --path .
rkit git sync
```

### Naming rules

- File and folder names become command names (`my-tool.rs` is run with `rkit my-tool`).
- Dashes are converted to underscores for the Rust module name automatically.
- Avoid Rust reserved keywords as names (`match.rs`, `type.rs`, `loop.rs`...).

### Sharing code between commands

All commands are compiled in the same crate, so shared helpers are one `mod` away. Create `src/util.rs`:

```rust
pub fn sh(cmd: &str) -> i32 {
    std::process::Command::new("sh")
        .args(["-c", cmd])
        .status()
        .ok()
        .and_then(|s| s.code())
        .unwrap_or(1)
}
```

Declare it in `src/main.rs` with `mod util;` and use it from any command:

```rust
pub const DESC: &str = "Prune unused Docker data";

pub fn run(_args: &[String]) -> i32 {
    crate::util::sh("docker system prune -f")
}
```

Need an external crate? Add it to `Cargo.toml` like in any Rust project (`clap`, `serde`, `anyhow`, `reqwest`...).

---

## Project structure

```text
rkit/
├── Cargo.toml
├── build.rs            # scans commands/ and generates the dispatch table
├── src/
│   ├── main.rs         # runtime navigation of the command tree
│   └── util.rs         # (optional) shared helpers
└── commands/
    ├── docker/
    │   ├── stop.rs
    │   └── clean.rs
    └── git/
        └── sync.rs
```

---

## Full source

<details>
<summary><b>Cargo.toml</b></summary>

```toml
[package]
name = "rkit"
version = "0.1.0"
edition = "2021"
description = "A personal toolbox compiled into a single Rust binary"
license = "MIT"

[dependencies]
# add whatever your commands need
```

</details>

<details>
<summary><b>build.rs</b></summary>

```rust
use std::{env, fs, path::Path};

fn ident(s: &str) -> String {
    s.replace('-', "_")
}

fn walk(dir: &Path, path: &mut Vec<String>, mods: &mut String, tree: &mut String) {
    let mut entries: Vec<_> = fs::read_dir(dir).unwrap().flatten().collect();
    entries.sort_by_key(|e| e.file_name());

    for e in entries {
        let p = e.path();
        let name = p.file_stem().unwrap().to_string_lossy().to_string();
        let id = ident(&name);

        if p.is_dir() {
            mods.push_str(&format!("pub mod {id} {{\n"));
            tree.push_str(&format!("(\"{name}\", Node::Dir(&[\n"));
            path.push(id);
            walk(&p, path, mods, tree);
            path.pop();
            mods.push_str("}\n");
            tree.push_str("])),\n");
        } else if p.extension().map_or(false, |x| x == "rs") {
            mods.push_str(&format!(
                "#[path = {:?}] pub mod {id};\n",
                p.canonicalize().unwrap().display().to_string()
            ));
            let full = path
                .iter()
                .cloned()
                .chain([id])
                .collect::<Vec<_>>()
                .join("::");
            tree.push_str(&format!(
                "(\"{name}\", Node::Cmd {{ desc: {full}::DESC, run: {full}::run }}),\n"
            ));
        }
    }
}

fn main() {
    println!("cargo:rerun-if-changed=commands");

    let (mut mods, mut tree) = (String::new(), String::new());
    walk(Path::new("commands"), &mut vec![], &mut mods, &mut tree);

    let out = format!("{mods}\npub static ROOT: Node = Node::Dir(&[\n{tree}]);\n");
    fs::write(
        Path::new(&env::var("OUT_DIR").unwrap()).join("commands.rs"),
        out,
    )
    .unwrap();
}
```

</details>

<details>
<summary><b>src/main.rs</b></summary>

```rust
use std::process::exit;

pub enum Node {
    Dir(&'static [(&'static str, Node)]),
    Cmd {
        desc: &'static str,
        run: fn(&[String]) -> i32,
    },
}

mod generated {
    use crate::Node;
    include!(concat!(env!("OUT_DIR"), "/commands.rs"));
}

fn list(entries: &[(&str, Node)]) {
    for (name, node) in entries {
        match node {
            Node::Dir(_) => println!("{name}/"),
            Node::Cmd { desc, .. } => println!("{name:<16} {desc}"),
        }
    }
}

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    let mut cur = &generated::ROOT;
    let mut i = 0;

    loop {
        match cur {
            Node::Cmd { run, .. } => exit(run(&args[i..])),
            Node::Dir(entries) => {
                let Some(arg) = args.get(i) else {
                    list(entries);
                    return;
                };
                match entries.iter().find(|(n, _)| *n == arg.as_str()) {
                    Some((_, node)) => {
                        cur = node;
                        i += 1;
                    }
                    None => {
                        eprintln!("rkit: '{arg}' not found, available:");
                        list(entries);
                        exit(1);
                    }
                }
            }
        }
    }
}
```

</details>

---

## Continuous integration

Add `.github/workflows/ci.yml` to keep the project healthy:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest]
    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@stable
        with:
          components: clippy, rustfmt
      - uses: Swatinem/rust-cache@v2
      - run: cargo fmt --all -- --check
      - run: cargo clippy --all-targets -- -D warnings
      - run: cargo build --release
```

---

## Roadmap

- [ ] Shell completion (bash, zsh, fish) generated from the command tree
- [ ] `rkit --help` and per-command `--help` from doc comments
- [ ] Argument parsing helpers (optional `clap` integration)
- [ ] Windows support
- [ ] Workspace mode: one crate per folder for faster incremental builds
- [ ] `rkit new <folder> <name>` to scaffold a command
- [ ] Prebuilt binaries on GitHub Releases

Have an idea? [Open an issue](https://github.com/YOUR_USERNAME/rkit/issues).

---

## Contributing

Contributions are welcome, whether it's a bug fix, a new feature, or a better example command.

1. Fork the repository
2. Create a branch: `git checkout -b feat/my-feature`
3. Make your changes and run `cargo fmt && cargo clippy`
4. Commit: `git commit -m "feat: add my feature"`
5. Push and open a Pull Request

If you share a useful command, put it under `examples/` so others can copy it into their own `commands/` folder.

---

## FAQ

**Do I have to recompile every time I add a command?**
Yes, that's the trade-off for getting a single, fast, dependency-free binary. Incremental builds keep it quick, and a workspace mode is on the roadmap for larger toolboxes.

**Can I still use shell scripts?**
Absolutely. A command can call anything via `std::process::Command`, or embed a script with `include_str!` and pipe it to `sh`.

**Does it work on Windows?**
The core (`build.rs` and dispatch) is portable Rust. Commands that shell out to `sh` are not. Official Windows support is planned.

---

## License

Released under the [MIT License](LICENSE).

---

<div align="center">

If rkit saves you time, consider leaving a ⭐ on the repo. It helps other people find it.

</div>
