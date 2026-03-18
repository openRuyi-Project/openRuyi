# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jiter

Name:           python-%{srcname}
Version:        0.13.0
Release:        %autorelease
Summary:        Fast iterable JSON parser
License:        MIT
URL:            https://github.com/pydantic/jiter
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
# TODO: use system crates in the future
#!RemoteAsset
Source1:        https://github.com/MahnoKropotkinvich/python-jiter-vendor/releases/download/vendor-%{version}/%{srcname}-%{version}-vendor.tar.bz2
BuildSystem:    pyproject

BuildOption(prep):  -a1
BuildOption(install):  jiter

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  python3dist(maturin)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%prep -a
# Drop the upstream Cargo.lock so cargo regenerates it from the vendor directory,
# avoiding version mismatches between the lock file and vendored crates.
rm -f Cargo.lock
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%description
A fast iterable JSON parser written in Rust, used as the JSON parsing backend
for pydantic.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%{?autochangelog}
