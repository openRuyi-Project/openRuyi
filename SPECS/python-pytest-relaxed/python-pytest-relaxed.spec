# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-relaxed

Name:           python-%{srcname}
Version:        2.0.2
Release:        %autorelease
License:        BSD-2-clause
URL:            https://github.com/bitprophet/pytest-relaxed
Summary:        Relaxed test discovery for pytest
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildSystem:    pyproject
BuildOption(install): pytest_relaxed +auto
%description
This package provides relaxed test discovery for pytest.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README*

%changelog
%autochangelog
