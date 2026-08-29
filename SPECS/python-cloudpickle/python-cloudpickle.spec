# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cloudpickle

Name:           python-%{srcname}
Version:        3.1.2
Release:        %autorelease
Summary:        Extended pickling support for Python objects
License:        BSD-3-Clause
URL:            https://github.com/cloudpipe/cloudpickle
#!RemoteAsset:  sha256:7fda9eb655c9c230dab534f1983763de5835249750e85fbcef43aaa30a9a2414
Source:         https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(flit-core)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
cloudpickle makes it possible to serialize Python constructs not supported
by the default pickle module from the Python standard library. It is
especially useful for cluster computing where Python expressions are shipped
over the network.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
