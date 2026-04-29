# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jiter

Name:           python-jiter
Version:        0.13.0
Release:        %autorelease
Summary:        Fast iterable JSON parser
License:        MIT
URL:            https://github.com/pydantic/jiter
#!RemoteAsset:  sha256:f2839f9c2c7e2dffc1bc5929a510e14ce0a946be9365fd1219e7ef342dae14f4
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
# TODO: use system crates in the future
#!RemoteAsset:  sha256:58772dc2004e8b16123f7adc85962ad9c89d601660c21e120a40329373a696f2
Source1:        https://github.com/MahnoKropotkinvich/python-jiter-vendor/releases/download/vendor-%{version}/%{srcname}-%{version}-vendor.tar.bz2
BuildSystem:    pyproject

BuildOption(prep):  -a1
BuildOption(check):  jiter
BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  rust

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%prep -a
# Regenerate lockfile against vendored crates to avoid lock/vendor mismatch.
rm -f Cargo.lock
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%description
jiter is a high-performance iterable JSON parser used by pydantic ecosystem
components.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
