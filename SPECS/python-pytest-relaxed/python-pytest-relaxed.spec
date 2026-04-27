# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-relaxed

Name:           python-%{srcname}
Version:        2.0.2
Release:        %autorelease
Summary:        Relaxed test discovery for pytest
License:        BSD-2-clause
URL:            https://github.com/bitprophet/pytest-relaxed
#!RemoteAsset:  sha256:956ea028ec30dbbfb680dd8e7b4a7fb8f80a239595e88bace018bf2c0d718248
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  pytest_relaxed +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides relaxed test discovery for pytest.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*
%license LICENSE

%changelog
%autochangelog
