# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname python-pam
%global pypi_name python_pam

Name:           python-%{srcname}
Version:        2.1.1
Release:        %autorelease
Summary:        Python PAM module using ctypes, py3
License:        MIT
URL:            https://github.com/FirefighterBlu3/python-pam
#!RemoteAsset:  sha256:d5bf50bd619a7d93514149a34aa4e4f9f174c90b38ec9657054f6a2017f65bb5
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l pam
# No module named '__internals'
BuildOption(check):  -e pam.pam

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This module provides an authenticate function that allows the caller to
authenticate a given username / password against the PAM system on Linux.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
