# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tokenizers

Name:           python-%{srcname}
Version:        0.22.2
Release:        %autorelease
Summary:        Fast, state-of-the-art tokenizers optimized for research and production
License:        Apache-2.0
URL:            https://pypi.org/project/tokenizers/
VCS:            git:https://github.com/huggingface/tokenizers
#!RemoteAsset:  sha256:473b83b915e547aa366d1eee11806deaf419e17be16310ac0a14077f1e28f917
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
# TODO(vendor): if OBS cannot access GitHub release directly, switch to _service(download_url) as fallback.
#!RemoteAsset:  sha256:16fe7eb5199169724cfbdac10f33d33fd40a18eacc29ca55218d2f44a26df002
Source1:        https://github.com/software-vendor/python-tokenizers/releases/download/vendor-%{version}/tokenizers-%{version}-vendor.tar.zst
BuildSystem:    pyproject

BuildOption(prep):  -a1
BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(maturin)
BuildRequires:  rust
BuildRequires:  cargo

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Tokenizers provides fast and production-ready tokenization implementations for
modern natural language processing workloads.

%prep -a
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF2'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF2

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc tokenizers/README.md
%license tokenizers/LICENSE

%changelog
%autochangelog
