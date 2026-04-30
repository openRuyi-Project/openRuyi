# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname imagesize

Name:           python-%{srcname}
Version:        2.0.0
Release:        %autorelease
Summary:        Get image size from PNG, JPEG, JPEG2000, WebP and GIF files
License:        MIT
URL:            https://github.com/shibukawa/imagesize_py
VCS:            git:https://github.com/shibukawa/imagesize_py.git
#!RemoteAsset:  sha256:8e8358c4a05c304f1fccf7ff96f036e7243a189e9e42e90851993c558cfe9ee3
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This module analyzes images and returns image size, without actually
decoding the image data.  It supports PNG, JPEG, JPEG2000, WebP, and GIF
formats.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.rst

%changelog
%autochangelog
