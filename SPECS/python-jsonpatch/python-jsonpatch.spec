# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jsonpatch

Name:           python-%{srcname}
Version:        1.47
Release:        %autorelease
Summary:        JSON Patch implementation in Python
License:        BSD-3-Clause
URL:            https://github.com/stefankoegl/python-json-patch
#!RemoteAsset:  sha256:5ed650b7517789e0f43428aa7b09442c0b90de0a0fd17a53fd0ebf55205c601e
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname} %{srcname}_cli %{srcname}-stubs

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
JSON Patch is a Library to apply JSON Patches according to RFC 6902.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/jsondiff
%{_bindir}/jsonpatch

%changelog
%autochangelog
