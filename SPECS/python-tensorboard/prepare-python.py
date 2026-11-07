# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

"""Stage the upstream Python release layout from source and web release assets."""

import ast
import re
from pathlib import Path
import shutil
import sys
import zipfile

if sys.argv[1] == "--generated-requirements":
    module = next(Path("tensorboard").rglob("*_pb2.py"))
    tree = ast.parse(module.read_text())
    validator = next(
        node for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "ValidateProtobufRuntimeVersion"
    )
    version = ".".join(str(ast.literal_eval(arg)) for arg in validator.args[1:4])
    requirements = Path("requirements.txt")
    requirements.write_text(re.sub(
        r"^protobuf[^\n]*", f"protobuf >= {version}, < 8.0.0",
        requirements.read_text(), flags=re.MULTILINE,
    ))
    grpc_tree = ast.parse(Path("tensorboard/data/proto/data_provider_pb2_grpc.py").read_text())
    for node in ast.walk(grpc_tree):
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "GRPC_GENERATED_VERSION"
            for target in node.targets
        ):
            grpc_version = ast.literal_eval(node.value)
            requirements.write_text(re.sub(
                r"^grpcio[^\n]*", f"grpcio >= {grpc_version}, < 2.0",
                requirements.read_text(), flags=re.MULTILINE,
            ))
            break
    sys.exit(0)

source = Path("tensorboard-upstream")
Path("tensorboard").rename(source)
assets = {
    "tensorboard/webfiles.zip",
    "tensorboard/plugins/projector/tf_projector_plugin/index.js",
    "tensorboard/plugins/projector/tf_projector_plugin/projector_binary.html",
    "tensorboard/plugins/projector/tf_projector_plugin/projector_binary.js",
}
with zipfile.ZipFile(sys.argv[1]) as wheel:
    for name in wheel.namelist():
        target = Path(name)
        if name in assets:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(wheel.read(name))
        elif name.startswith("tensorboard/") and "/_vendor/" not in name and name.endswith(".py"):
            target.parent.mkdir(parents=True, exist_ok=True)
            original = source.joinpath(*target.parts[1:])
            if original.is_file():
                shutil.copy2(original, target)
            elif name.endswith("__init__.py"):
                target.touch()
            elif not name.endswith(("_pb2.py", "_pb2_grpc.py")):
                raise RuntimeError(f"Release module missing from source: {name}")
    assert assets.issubset(wheel.namelist())
for proto in source.rglob("*.proto"):
    if proto.name.endswith("_test.proto") or "defs" in proto.parts:
        continue
    target = Path("tensorboard") / proto.relative_to(source)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(proto, target)
