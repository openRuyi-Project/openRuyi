# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyscard

Name:           python-%{srcname}
Version:        2.1.1
Release:        %autorelease
Summary:        Smartcard module for Python
License:        LGPL-2.1-or-later
URL:            https://github.com/LudovicRousseau/pyscard
VCS:            git:https://github.com/LudovicRousseau/pyscard.git
#!RemoteAsset:  sha256:f9b0dc3fad83ac72a9335af4d04b608edc9d01e2b90e0c38ed0ef1fd014c4414
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# Backport upstream commit 54ef7f2 to fix SWIG wrapper generation.
Patch0:         0001-fix-swig-exception-action.patch

BuildOption(install):  smartcard
# Skip optional GUI modules: No module named 'wx'.
BuildOption(check):  -e 'smartcard.wx*'
# Skip optional card-name database: No module named '_bsddb'.
BuildOption(check):  -e 'smartcard.CardNames'
# Skip optional Pyro reader: No module named 'Pyro'.
BuildOption(check):  -e 'smartcard.pyro.PyroReader'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  swig
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pyscard provides Python modules for smart card communication through PC/SC.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
