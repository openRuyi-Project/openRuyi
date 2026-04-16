# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname libnacl

Name:           python-%{srcname}
Version:        2.1.0
Release:        %autorelease
Summary:        Python ctypes wrapper for libsodium
License:        Apache-2.0
URL:            https://libnacl.readthedocs.io/en/latest/
VCS:            git:https://github.com/saltstack/libnacl.git
#!RemoteAsset:  sha256:f3418da7df29e6d9b11fd7d990289d16397dc1020e4e35192e11aee826922860
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
This library is used to gain direct access
to the functions exposed by Daniel J. Bernstein’s nacl library via libsodium.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
