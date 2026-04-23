# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname orjson

Name:           python-%{srcname}
Version:        3.11.7
Release:        %autorelease
Summary:        Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy
License:        MPL-2.0 AND (Apache-2.0 OR MIT)
URL:            https://github.com/ijl/orjson
#!RemoteAsset:  sha256:9b1a67243945819ce55d24a30b59d6a168e86220452d2c96f4d1f093e71c0c49
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(parso)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  cargo
BuildRequires:  rust

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
orjson is a fast, correct JSON library for Python. It benchmarks as
the fastest Python library for JSON and is more correct than the standard
json library or other third-party libraries. It serializes dataclass,
datetime, numpy, and UUID instances natively.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE-APACHE LICENSE-MIT LICENSE-MPL-2.0

%changelog
%autochangelog
