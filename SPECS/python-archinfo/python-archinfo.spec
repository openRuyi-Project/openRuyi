# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname archinfo

Name:           python-%{srcname}
Version:        9.2.193
Release:        %autorelease
Summary:        Collection of classes that contain architecture-specific information
License:        BSD
URL:            https://github.com/angr/archinfo
#!RemoteAsset:  sha256:b46da3d0ee6cc7b46230c8e4f1dec9606b9acf814ea585ddaa794b82a7976628
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip) >= 19

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
archinfo is a collection of classes that contain architecture-specific
information. It is useful for cross-architecture tools.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
