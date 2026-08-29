# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname av

Name:           python-%{srcname}
Version:        17.0.1
Release:        %autorelease
Summary:        Python bindings for FFmpeg libraries
License:        BSD-3-Clause
URL:            https://github.com/PyAV-Org/PyAV
#!RemoteAsset:  sha256:fbcbd4aa43bca6a8691816283112d1659a27f407bbeb66d1397023691339f5d4
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libswresample)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PyAV provides Python bindings for the FFmpeg libraries. It allows
access to the FFmpeg multimedia framework's powerful features
directly from Python.

%generate_buildrequires
%pyproject_buildrequires -p

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{python3_sitearch}/av-17.0.1.dist-info/*
%{_bindir}/pyav

%changelog
%autochangelog
