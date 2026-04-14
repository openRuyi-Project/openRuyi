# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname greenlet

Name:           python-%{srcname}
Version:        3.4.0
Release:        %autorelease
Summary:        Lightweight in-process concurrent programming
License:        MIT AND PSF-2.0
URL:            https://github.com/python-greenlet/greenlet
VCS:            git:https://github.com/python-greenlet/greenlet.git
#!RemoteAsset:  sha256:f50a96b64dafd6169e595a5c56c9146ef80333e67d4476a65a9c55f400fc22ff
Source:         https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e "%{srcname}.tests*"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The greenlet package is a spin-off of Stackless, a version of CPython that
supports micro-threads called "tasklets". Tasklets run pseudo-concurrently
and are synchronized with data exchanges on "channels". A "greenlet" is a
still more primitive notion of micro-thread with no implicit scheduling.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE LICENSE.PSF
%doc README.rst
%{_includedir}/python%{python3_version}/%{srcname}/%{srcname}.h

%changelog
%autochangelog
