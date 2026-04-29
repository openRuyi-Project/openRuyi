# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname plac

Name:           python-%{srcname}
Version:        1.4.5
Release:        %autorelease
Summary:        Command line argument parser for Python
License:        BSD-2-Clause
URL:            https://github.com/ialbert/plac
#!RemoteAsset:  sha256:5f05bf85235c017fcd76c73c8101d4ff8e96beb3dc58b9a37de49cac7de82d14
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# plac_tk still imports the Python 2 Tkinter module and is not usable on Python 3.
BuildOption(install):  -l plac plac_core plac_ext plac_tk
BuildOption(check):  -e plac_tk plac plac_core plac_ext

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
plac provides a command line argument parser and command dispatcher for Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGES.md
%license LICENSE.txt
%{_bindir}/plac_runner.py

%changelog
%autochangelog
