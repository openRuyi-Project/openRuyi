# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname psutil

Name:           python-%{srcname}
Version:        7.2.2
Release:        %autorelease
Summary:        Library for retrieving information on running processes
License:        BSD-3-Clause
URL:            https://github.com/giampaolo/psutil
#!RemoteAsset:  sha256:0746f5f8d406af344fd547f1c8daa5f5c33dbc293bb8d6a16d80b4bb88f59372
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  sed
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip) >= 19
BuildRequires:  python3dist(setuptools) >= 43

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Psutil (Python system and process utilities) is a library for
retrieving information on running processes and system utilization (CPU,
memory, disks, network) in Python.  It is useful mainly for system monitoring,
profiling and limiting process resources and management of running processes.
It implements many functionalities offered by command line tools such as: ps,
top, lsof, netstat, ifconfig, who, df, kill, free, nice, ionice, iostat,
iotop, uptime, pidof, tty, taskset, pmap.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
