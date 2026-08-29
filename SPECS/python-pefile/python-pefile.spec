# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pefile

Name:           python-%{srcname}
Version:        2024.8.26
Release:        %autorelease
Summary:        Python module to read and work with PE (Portable Executable) files
License:        MIT
URL:            https://github.com/erocarrera/pefile
#!RemoteAsset:  sha256:3ff6c5d8b43e8c37bb6e6dd5085658d658a7a0bdcd20b6a07b1fcfc1c4e9d632
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname} ordlookup peutils +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pefile is a multi-platform Python module to parse and work with Portable
Executable (PE) files. Most of the information contained in the PE file
headers is accessible, as well as all the sections' details and data.

The structures defined in the Windows header files will be accessible
as attributes in the PE instance. The naming of fields/attributes will
try to adhere to the naming scheme in those headers. Only shortcuts
added for convenience will depart from that convention.

pefile requires some basic understanding of the layout of a PE file —
with it, it's possible to explore nearly every single feature of the PE
file format.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
