# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname PySocks

Name:           python-pysocks
Version:        1.7.1
Release:        %autorelease
Summary:        A Python SOCKS client module
License:        BSD-3-Clause
URL:            https://github.com/Anorov/PySocks
#!RemoteAsset:  sha256:3f8804571ebe159c380ac6de37643bb4685970655d3bba243530d6558b799aa0
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l socks sockshandler

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-pysocks = %{version}-%{release}
%python_provide python3-pysocks

%description
A fork of SocksiPy with bug fixes and extra features. Acts as a
drop-in replacement to the socket module.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
