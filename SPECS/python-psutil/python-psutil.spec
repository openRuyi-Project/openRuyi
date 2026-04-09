# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname psutil

Name:           python-%{srcname}
Version:        7.2.2
Release:        %autorelease
License:        BSD-3-Clause
URL:            https://github.com/giampaolo/psutil
Summary:        Library for retrieving information on running processes
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  sed
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip) >= 19
BuildRequires:  python3dist(setuptools) >= 43
BuildSystem:    pyproject
BuildOption(install):  -l %{srcname} +auto
%description
@code{psutil} (Python system and process utilities) is a library for
retrieving information on running processes and system utilization (CPU,
memory, disks, network) in Python.  It is useful mainly for system monitoring,
profiling and limiting process resources and management of running processes.
It implements many functionalities offered by command line tools such as: ps,
top, lsof, netstat, ifconfig, who, df, kill, free, nice, ionice, iostat,
iotop, uptime, pidof, tty, taskset, pmap.

%generate_buildrequires
%pyproject_buildrequires

# TODO: Our OBS has some limits and some tests are flaky.
%check

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
