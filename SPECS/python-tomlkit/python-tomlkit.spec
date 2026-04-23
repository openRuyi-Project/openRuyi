# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tomlkit

Name:           python-%{srcname}
Version:        0.13.2
Release:        %autorelease
Summary:        Style-preserving TOML library
License:        MIT
URL:            https://github.com/sdispater/tomlkit
#!RemoteAsset:  sha256:fff5fe59a87295b278abd31bec92c15d9bc4a06885ab12bcea52c71119392e79
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
TOML Kit is a 1.0.0rc1-compliant TOML library.  It includes a parser that
preserves all comments, indentations, whitespace and internal element ordering,
and makes them accessible and editable via an intuitive API.  It can also
create new TOML documents from scratch using the provided helpers.  Part of the
implementation has been adapted, improved, and fixed from Molten.

%generate_buildrequires
%pyproject_buildrequires -r

%check -a
%pytest

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
