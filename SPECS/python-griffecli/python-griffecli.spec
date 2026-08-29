# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname griffecli

Name:           python-%{srcname}
Version:        2.0.2
Release:        %autorelease
Summary:        Griffe command-line interface
License:        ISC
URL:            https://github.com/mkdocstrings/griffe
#!RemoteAsset:  sha256:40a1ad4181fc39685d025e119ae2c5b669acdc1f19b705fb9bf971f4e6f6dffb
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(griffelib)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pdm-backend)
BuildRequires:  python3dist(uv-dynamic-versioning)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Command-line interface for Griffe, providing tools to dump API data as JSON
and check for API breaking changes.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/griffecli

%changelog
%autochangelog
