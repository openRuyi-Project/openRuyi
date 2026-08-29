# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fakeredis

Name:           python-%{srcname}
Version:        2.35.1
Release:        %autorelease
Summary:        Python implementation of redis API
License:        BSD-3-Clause
URL:            https://github.com/cunla/fakeredis-py
#!RemoteAsset:  sha256:5bae5eba7b9d93cb968944ac40936373cf2397ff71667d4b595df65c3d2e413f
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(lupa)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
FakeRedis is a pure-Python implementation of the Redis Protocol API.
It provides enhanced versions of the redis-py/valkey-py Python bindings for Redis.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
