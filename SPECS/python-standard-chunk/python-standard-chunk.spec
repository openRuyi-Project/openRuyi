# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname standard-chunk
%global pypi_name standard_chunk

Name:           python-%{srcname}
Version:        3.13.0
Release:        %autorelease
Summary:        Module to read IFF chunks.
License:        PSF-2.0
URL:            https://github.com/youknowone/python-deadlib
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  chunk

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This module provides an interface for reading files that use EA IFF 85 chunks.
This format is used in at least the Audio Interchange File Format (AIFF/AIFF-C) and
the Real Media File Format (RMFF). The WAVE audio file format is closely related and
can also be read using this module.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
