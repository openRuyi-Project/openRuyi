# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname trio

Name:           python-%{srcname}
Version:        0.31.0
Release:        %autorelease
Summary:        A friendly Python library for async concurrency and I/O
License:        MIT
URL:            https://github.com/python-trio/trio
#!RemoteAsset:  sha256:f71d551ccaa79d0cb73017a33ef3264fde8335728eb4c6391451fe5d253a9d5b
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The Trio project produces an async/await-native I/O library for
Python. Like all async libraries, its main purpose is to help write
programs that do multiple things at the same time with parallelized
I/O, such as a web spider that wants to fetch lots of pages in
parallel, a web server that needs to juggle lots of downloads and
websocket connections at the same time, a process supervisor
monitoring multiple subprocesses. Compared to other libraries, Trio
has an obsessive focus on usability and correctness.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
