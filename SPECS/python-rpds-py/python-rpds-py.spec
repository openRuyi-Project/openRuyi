# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rpds-py
%global pypi_name rpds_py

Name:           python-%{srcname}
Version:        0.21.0
Release:        %autorelease
Summary:        Python bindings to Rust's persistent data structures
License:        MIT
URL:            https://github.com/crate-py/rpds
#!RemoteAsset:  sha256:ed6378c9d66d0de903763e7706383d60c33829581f0adff47b6535f1802fa6db
Source0:        https://files.pythonhosted.org/packages/23/80/afdf96daf9b27d61483ef05b38f282121db0e38f5fd4e89f40f5c86c2a4f/%{pypi_name}-0.21.0.tar.gz
Source1:        %{pypi_name}-%{version}-vendor.tar.zst
BuildSystem:    pyproject

BuildOption(prep):  -a1
BuildOption(install):  -l rpds -L
BuildOption(check):  rpds

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(maturin)
BuildRequires:  python3dist(pip)
BuildRequires:  rust
BuildRequires:  cargo

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
rpds-py provides Python bindings to Rust's persistent data structures.

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
%license LICENSE
%doc README.rst

%changelog
%autochangelog
