# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname scikit-build
%global pypi_name scikit_build

Name:           python-%{srcname}
Version:        0.19.0
Release:        %autorelease
Summary:        Improved build system generator for Python C/C++ projects
License:        MIT
URL:            https://github.com/scikit-build/scikit-build
VCS:            git:https://github.com/scikit-build/scikit-build
#!RemoteAsset:  sha256:46e1b2d71343d14e4c07d7e60902e673c78defb9a2c282b70ad80fb8502ade2e
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l skbuild +auto

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(distro)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel) >= 0.32

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
scikit-build is an improved build system generator for Python extensions.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*
%license LICENSE*

%changelog
%autochangelog
