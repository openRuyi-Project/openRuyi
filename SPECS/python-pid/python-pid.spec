# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pid

Name:           python-%{srcname}
Version:        3.0.4
Release:        %autorelease
Summary:        Pidfile featuring stale detection and file-locking, can also be used as context-manager or decorator
License:        Apache-2.0
URL:            https://github.com/trbs/pid
#!RemoteAsset:  sha256:0e33670e83f6a33ebb0822e43a609c3247178d4a375ff50a4689e266d853eb66
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}
# Exclude win32 stuff
BuildOption(check):  -e pid.win32

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pid provides a PidFile class that manages PID files. PidFile features:
  - stale detection
  - locking using fcntl
  - chmod (default is 0o644)
  - chown
  - custom exceptions

PidFile can also be used as a context manager or a decorator.

%prep -a
rm -rf %{srcname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest

%files -f %{pyproject_files}
%doc AUTHORS CHANGELOG README.rst
%license LICENSE

%changelog
%autochangelog
