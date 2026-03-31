# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname schedutils

Name:           python-%{srcname}
Version:        0.6
Release:        %autorelease
Summary:        Linux scheduler python bindings
License:        GPL-2.0-only
URL:            https://git.kernel.org/cgit/libs/python/python-schedutils/python-schedutils.git
#!RemoteAsset:  sha256:90a24f8d46574513b3d334b473e128c456e7eddaec6e3dd198d7e5ad69ddc12f
Source0:        https://cdn.kernel.org/pub/software/libs/python/%{name}/%{name}-%{version}.tar.xz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Python interface for the Linux scheduler sched_{get,set}{affinity,scheduler}\
functions and friends.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license COPYING
%{_bindir}/pchrt
%{_bindir}/ptaskset
%{_mandir}/man1/pchrt.1*
%{_mandir}/man1/ptaskset.1*

%changelog
%autochangelog
