# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname safetensors

Name:           python-%{srcname}
Version:        0.7.0
Release:        %autorelease
Summary:        Simple, safe way to store and distribute tensors
License:        Apache-2.0
URL:            https://github.com/huggingface/safetensors
#!RemoteAsset:  sha256:07663963b67e8bd9f0b8ad15bb9163606cd27cc5a1b96235a50d8369803b96b0
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
# TODO: use system crates in the future
#!RemoteAsset:  sha256:710d5402bab8653296ad7bd1fe1c4fdb9cb69f85c2449ceb5209981c999276cb
Source1:        https://github.com/software-vendor/python-%{srcname}-vendor/releases/download/vendor-%{version}/safetensors-%{version}-vendor.tar.bz2
BuildSystem:    pyproject

BuildOption(prep):  -a1
BuildOption(install):  -l %{srcname}
# Needs additional dependencies
BuildOption(check):  -e "safetensors.torch" -e "safetensors.tensorflow" -e "safetensors.paddle" -e "safetensors.flax" -e "safetensors.mlx"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(maturin)
BuildRequires:  python3dist(numpy)
BuildRequires:  rust

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This repository implements a new simple format for storing
tensors safely (as opposed to pickle) and that is still fast (zero-copy).

%prep -a
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc safetensors/README.md
%license safetensors/LICENSE

%changelog
%autochangelog
