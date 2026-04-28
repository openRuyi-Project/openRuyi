# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname asyncssh

Name:           python-%{srcname}
Version:        2.22.0
Release:        %autorelease
Summary:        Asynchronous SSHv2 client and server library
License:        EPL-2.0 OR GPL-2.0-or-later
URL:            https://asyncssh.timeheart.net/
#!RemoteAsset:  sha256:c3ce72b01be4f97b40e62844dd384227e5ff5a401a3793007c42f86a5c8eb537
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(gssapi)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyopenssl)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
AsyncSSH is a Python package which provides an asynchronous client and server implementation of the SSHv2 protocol on top of the Python 3.10+ asyncio framework.

%generate_buildrequires
%pyproject_buildrequires

%prep -a
cd %{_builddir}/%{name}-%{version}

# Remove Windows support to pass checks.
rm ./asyncssh/gss_win32.py
rm ./tests/sspi_stub.py

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
