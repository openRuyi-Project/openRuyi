# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pycdlib

Name:           python-%{srcname}
Version:        1.14.0
Release:        %autorelease
Summary:        A pure python ISO9660 read and write library
License:        LGPL-2.0-only
URL:            https://github.com/clalancette/pycdlib
#!RemoteAsset:  sha256:8ec306b31d9c850f28c5fda52438d904edd1e8fcf862c5ffd756272efac9f422
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Pycdlib is a pure python library for reading, writing, and otherwise
manipulating ISO9660 files.  It is focused on speed, correctness, and
conformance to the various standards around ISO9660, including ISO9660
itself, the Joliet extensions, the Rock Ridge extensions, the El Torito
boot extensions, and UDF.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md examples/
%license COPYING
# These are tools shipped with pycdlib for working with ISO files
%{_bindir}/pycdlib-explorer
%{_bindir}/pycdlib-extract-files
%{_bindir}/pycdlib-genisoimage
%{_mandir}/man1/*

%changelog
%autochangelog
