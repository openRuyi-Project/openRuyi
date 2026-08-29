# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global pypi_name msgspec

Name:           python-%{pypi_name}
Version:        0.19.0
Release:        %autorelease
Summary:        Fast serialization and validation library
License:        BSD-3-Clause
URL:            https://jcristharif.com/msgspec/
#!RemoteAsset:  sha256:33961077a37830c54fa3108bd226a9d7a09b91ff82ef7b976a371039b54b6bc7
Source0:        https://github.com/jcrist/%{pypi_name}/archive/refs/tags/%{version}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{pypi_name} = %{version}-%{release}
Provides:       python3-%{pypi_name}%{?_isa} = %{version}-%{release}
%python_provide python3-%{pypi_name}

%description
A fast serialization and validation library, with builtin support for
JSON, MessagePack, YAML, and TOML.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
