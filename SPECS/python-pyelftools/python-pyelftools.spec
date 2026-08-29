# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyelftools

Name:           python-%{srcname}
Version:        0.32
Release:        %autorelease
Summary:        Analyze binary and library file information
License:        LicenseRef-openRuyi-Public-Domain
URL:            https://github.com/eliben/pyelftools
#!RemoteAsset:  sha256:6de90ee7b8263e740c8715a925382d4099b354f29ac48ea40d840cf7aa14ace5
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l elftools +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This Python library provides interfaces for parsing and analyzing two
binary and library file formats ; the Executable and Linking Format (ELF), and
debugging information in the Debugging With Attributed Record
Format (DWARF).

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
