# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rpds-py

Name:           python-%{srcname}
Version:        0.30.0
Release:        %autorelease
Summary:        Python bindings to Rust's persistent data structures (rpds)
License:        MIT
URL:            https://github.com/crate-py/rpds
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/rpds_py-%{version}.tar.gz
# TODO: use system crates in the future
#!RemoteAsset
Source1:        https://github.com/MahnoKropotkinvich/python-rpds-py-vendor/releases/download/vendor-%{version}/%{srcname}-%{version}-vendor.tar.bz2
BuildSystem:    pyproject

BuildOption(prep):  -a1
BuildOption(install):  rpds

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  python3dist(maturin)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%prep -a
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%description
Python bindings to the Rust rpds crate, which provides persistent (immutable)
data structures including hash tries, red-black trees, and lists.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%{?autochangelog}
