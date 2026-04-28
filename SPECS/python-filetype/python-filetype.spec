# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname filetype

Name:           python-%{srcname}
Version:        1.2.0
Release:        %autorelease
Summary:        Infer file type and MIME type of any file/buffer
License:        MIT
URL:            https://github.com/h2non/filetype.py
#!RemoteAsset:  sha256:66b56cd6474bf41d8c54660347d37afcc3f7d1970648de365c102ef77548aadb
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  filetype

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Small and dependency-free Python package to infer file type and MIME type
checking the magic bytes signature of a file or buffer.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/filetype

%changelog
%autochangelog
