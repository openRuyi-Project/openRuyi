# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>

%global srcname modelscope

Name:           python-modelscope
Version:        1.40.2
Release:        %autorelease
Summary:        Model-as-a-Service framework for machine learning
License:        Apache-2.0
URL:            https://pypi.org/project/modelscope/
VCS:            git:https://github.com/modelscope/modelscope
#!RemoteAsset:  sha256:7a642cef8c144c28c4ddcc37db5fd803f5481f0d78a7f26c2b9e0e2a225b528c
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# Model adapters require separately selected framework extras. Check the base API.
BuildOption(check):  -t

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(modelscope-hub) >= 0.4.6
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(requests) >= 2.25
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tqdm) >= 4.64.0
BuildRequires:  python3dist(urllib3) >= 1.26
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       python3dist(filelock)
Requires:       python3dist(modelscope-hub) >= 0.4.6
Requires:       python3dist(packaging)
Requires:       python3dist(requests) >= 2.25
Requires:       python3dist(tqdm) >= 4.64.0
Requires:       python3dist(urllib3) >= 1.26

%description
ModelScope provides unified interfaces for inference, training, and evaluation
of machine learning models across multiple domains.

%generate_buildrequires
%pyproject_buildrequires

%check -a
# The framework extras contain legacy model adapters which are not compatible
# with the packaged Transformers 5 API.  Keep the default check focused on the
# supported top-level API and exercise the hub cache path without network I/O.
PYTHONPATH="%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}" \
  %{__python3} - <<'PY'
import tempfile
from pathlib import Path

from modelscope.hub.snapshot_download import snapshot_download

with tempfile.TemporaryDirectory() as directory:
    cache = Path(directory)
    snapshot = cache / "models" / "owner--repo" / "snapshots" / "fixture"
    snapshot.mkdir(parents=True)
    (snapshot / "config.json").write_text("{}", encoding="utf-8")
    result = snapshot_download(
        "owner/repo",
        revision="fixture",
        cache_dir=cache,
        local_files_only=True,
    )
    assert Path(result) == snapshot
    assert (Path(result) / "config.json").read_text(encoding="utf-8") == "{}"
PY

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
