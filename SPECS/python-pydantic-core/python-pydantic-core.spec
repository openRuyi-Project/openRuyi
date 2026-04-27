# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pydantic-core
%global pypi_name pydantic_core

Name:           python-%{srcname}
Version:        2.41.5
Release:        %autorelease
Summary:        Core functionality for Pydantic validation and serialization
License:        MIT
URL:            https://github.com/pydantic/pydantic-core
#!RemoteAsset:  sha256:08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
# TODO: use system crates in the future
#!RemoteAsset:  sha256:7f7a8e00fb56c4677c589b2fc652aadcbd3e8d9967b121f14f50bd10f70977b7
Source1:        https://github.com/software-vendor/python-pydantic-core-vendor/releases/download/vendor-%{version}/pydantic-core-%{version}-vendor.tar.bz2
BuildSystem:    pyproject

BuildOption(prep):  -a1
BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  rust
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(puccinialin)
BuildRequires:  python3dist(maturin)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides the core functionality for
pydantic validation and serialization. Pydantic-core is
currently around 17x faster than pydantic V1.

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
%doc README.md
%license LICENSE

%changelog
%autochangelog
