# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname zopfli

Name:           python-%{srcname}
Version:        0.4.3
Release:        %autorelease
Summary:        Zopfli module for python
License:        Apache-2.0
URL:            https://github.com/fonttools/py-zopfli
#!RemoteAsset:  sha256:d3a50f91a13cea9bafe025de8fd87a005eb26de02a4f0c193127ddbf23ac8ebe
Source0:        https://files.pythonhosted.org/packages/source/z/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  python3dist(pytest)
BuildRequires:  zopfli-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python bindings for the Zopfli compression library.

%build -p
export USE_SYSTEM_ZOPFLI=1

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Exercise the installed extension and entry points with the upstream test suite.
PATH=%{buildroot}%{_bindir}:$PATH PYTHONPATH=%{buildroot}%{python3_sitearch} %{python3} -m pytest -q tests/

%files -f %{pyproject_files}
%doc README.rst
%license COPYING

%changelog
%autochangelog
