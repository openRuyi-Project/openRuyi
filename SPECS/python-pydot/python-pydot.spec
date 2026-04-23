# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pydot

Name:           python-%{srcname}
Version:        4.0.1
Release:        %autorelease
Summary:        Python interface to Graphviz's Dot language
License:        MIT
URL:            https://github.com/pydot/pydot
#!RemoteAsset:  sha256:c2148f681c4a33e08bf0e26a9e5f8e4099a82e0e2a068098f32ce86577364ad5
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyparsing)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
An interface for creating both directed and non directed graphs from Python.
Currently all attributes implemented in the Dot language are supported.

Output can be inlined in Postscript into interactive scientific environments
like TeXmacs, or output in any of the format's supported by the Graphviz
tools dot, neato, twopi.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc ChangeLog README.md

%changelog
%autochangelog
