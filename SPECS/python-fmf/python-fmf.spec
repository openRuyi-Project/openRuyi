# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fmf

Name:           python-%{srcname}
Version:        1.7.0
Release:        %autorelease
Summary:        Flexible Metadata Format
License:        GPL-2.0-or-later
URL:            https://github.com/teemtee/fmf
#!RemoteAsset:  sha256:131b557786b912f99d49d8dcc84196e3c2f39c5ce5ffe8b78e48150afd380dc3
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(ruamel-yaml)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Flexible Metadata Format is a framework and command line tool for storing
metadata in a filesystem tree and querying it efficiently.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc examples
%doc README.rst
%license LICENSE
%{_bindir}/fmf

%changelog
%autochangelog
