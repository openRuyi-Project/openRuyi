# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tomlkit

Name:           python-%{srcname}
Version:        0.13.2
Release:        %autorelease
License:        MIT
URL:            https://github.com/sdispater/tomlkit
Summary:        Style-preserving TOML library
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

BuildRequires:  pytest
BuildRequires:  python3dist(pyyaml)

BuildSystem:    pyproject
BuildOption(install): %{srcname} +auto
%description
TOML Kit is a 1.0.0rc1-compliant TOML library.  It includes a parser that
preserves all comments, indentations, whitespace and internal element ordering,
and makes them accessible and editable via an intuitive API.  It can also
create new TOML documents from scratch using the provided helpers.  Part of the
implementation has been adapted, improved, and fixed from Molten.

%generate_buildrequires
%pyproject_buildrequires -r

%check
%pytest

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
