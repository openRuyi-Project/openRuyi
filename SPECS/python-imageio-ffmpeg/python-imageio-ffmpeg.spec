# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname imageio-ffmpeg
%global pypi_name imageio_ffmpeg

Name:           python-%{srcname}
Version:        0.6.0
Release:        %autorelease
Summary:        FFMPEG wrapper for Python ImageIO
License:        BSD-2-Clause
URL:            https://github.com/imageio/imageio-ffmpeg
#!RemoteAsset:  sha256:e2556bed8e005564a9f925bb7afa4002d82770d6b08825078b7697ab88ba1755
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l imageio_ffmpeg

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python bindings for FFMPEG using ImageIO.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
