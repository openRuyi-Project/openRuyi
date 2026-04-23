# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname py-cpuinfo

Name:           python-%{srcname}
Version:        9.0.0
Release:        %autorelease
Summary:        Get CPU information with pure Python
License:        MIT
URL:            https://github.com/workhorsy/py-cpuinfo
VCS:            git:https://github.com/workhorsy/py-cpuinfo.git
#!RemoteAsset:  sha256:3cdbbf3fac90dc6f118bfd64384f309edeadd902d7c8fb17f02ffa1fc3f49690
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l cpuinfo

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
py-cpuinfo gets CPU information with pure Python. It supports many operating
systems and reports vendor, architecture, cache, and feature data.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/cpuinfo

%changelog
%autochangelog
