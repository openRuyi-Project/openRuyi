# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ufoprocessor

Name:           python-%{srcname}
Version:        1.14.1
Release:        %autorelease
Summary:        Read, write and generate UFOs with designspace data
License:        MIT
URL:            https://github.com/LettError/ufoProcessor
#!RemoteAsset:  sha256:fd38d3cc359b94171ba8d3fdc1e4defde2206acef4f97d75b48503bb8ac03b01
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l ufoProcessor

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python package based on the designSpaceDocument from fontTools.designspaceLib) specifically to _process_ and _generate_ instances for UFO files, glyphs and other data.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
