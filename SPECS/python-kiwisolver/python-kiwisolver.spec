# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname kiwisolver

Name:           python-%{srcname}
Version:        1.4.9
Release:        %autorelease
Summary:        A fast implementation of the Cassowary constraint solver
License:        BSD-3-Clause AND HPND-sell-variant
URL:            https://github.com/nucleic/kiwi
#!RemoteAsset:  sha256:c3b22c26c6fd6811b0ae8363b95ca8ce4ea3c202d3d0975b2914310ceb1bcc4d
Source0:        https://files.pythonhosted.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Kiwi is an efficient C++ implementation of the Cassowary constraint solving
algorithm. Kiwi is an implementation of the algorithm based on the seminal
Cassowary paper. It is *not* a refactoring of the original C++ solver. Kiwi has
been designed from the ground up to be lightweight and fast.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
