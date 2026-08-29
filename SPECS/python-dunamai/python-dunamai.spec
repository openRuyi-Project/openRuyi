# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname dunamai

Name:           python-%{srcname}
Version:        1.26.1
Release:        %autorelease
Summary:        Dynamic versioning library and CLI
License:        MIT
URL:            https://github.com/mtkennerly/dunamai
#!RemoteAsset:  sha256:3b46007bd65b00b4824ead0a1aee365fd22d0ec2b9c219497d4fd48f52860c8b
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Dunamai is a library and command line tool for producing dynamic, standards-
compliant version strings, derived from tags in version control.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/dunamai

%changelog
%autochangelog
