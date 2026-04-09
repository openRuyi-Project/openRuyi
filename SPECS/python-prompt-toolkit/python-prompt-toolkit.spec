# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname prompt_toolkit

Name:           python-prompt-toolkit
Version:        3.0.52
Release:        %autorelease
Summary:        Library for building powerful interactive command lines in Python
License:        BSD-3-Clause
URL:            https://github.com/prompt-toolkit/python-prompt-toolkit
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(asyncssh)
BuildRequires:  python3dist(pyperclip)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
`prompt_toolkit` is a library for building powerful interactive command line applications in Python.

%generate_buildrequires
%pyproject_buildrequires

%prep -a
# Remove Win32 support to pass checks.
cd %{_builddir}/%{name}-%{version}
rm ./src/prompt_toolkit/eventloop/win32.py
rm ./src/prompt_toolkit/input/win32_pipe.py
rm ./src/prompt_toolkit/input/win32.py
rm ./src/prompt_toolkit/output/conemu.py
rm ./src/prompt_toolkit/output/win32.py
rm ./src/prompt_toolkit/output/windows10.py

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
