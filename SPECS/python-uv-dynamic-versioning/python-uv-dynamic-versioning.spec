# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname uv-dynamic-versioning
%global pypi_name uv_dynamic_versioning

Name:           python-%{srcname}
Version:        0.14.0
Release:        %autorelease
Summary:        Dynamic versioning plugin for hatchling using uv
License:        MIT
URL:            https://github.com/ninoseki/uv-dynamic-versioning
#!RemoteAsset:  sha256:574fbc07e87ace45c01d55967ad3b864871257b98ff5b8ac87c261227ac8db5b
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{pypi_name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(dunamai)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(tomlkit)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A hatchling plugin for dynamic versioning powered by dunamai, designed to
work with uv-based Python projects.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/uv-dynamic-versioning

%changelog
%autochangelog
