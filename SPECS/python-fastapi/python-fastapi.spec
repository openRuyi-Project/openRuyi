# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fastapi

Name:           python-%{srcname}
Version:        0.135.1
Release:        %autorelease
Summary:        FastAPI web framework for APIs
License:        MIT
URL:            https://github.com/fastapi/fastapi
#!RemoteAsset:  sha256:d04115b508d936d254cea545b7312ecaa58a7b3a0f84952535b4c9afae7668cd
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Switch from pdm-backend to setuptools for the openRuyi buildroot.
Patch0:         2000-python-fastapi-switch-to-setuptools-build-backend.patch

BuildOption(install):  -l %{srcname}
# OBS first blocked this package on optional runtime/test dependencies such as
# annotated-doc and starlette. Once those were added, importing
# fastapi.testclient still failed because starlette.testclient requires httpx,
# which is not packaged in openRuyi yet. Keep a smoke import for the main
# package and skip only the optional test client module for now.
BuildOption(check):    -e fastapi.testclient fastapi

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
FastAPI is a modern, fast web framework for building APIs with Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/fastapi

%changelog
%autochangelog
