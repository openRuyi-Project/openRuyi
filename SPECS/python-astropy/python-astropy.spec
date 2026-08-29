# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname astropy

Name:           python-%{srcname}
Version:        8.0.1
Release:        %autorelease
Summary:        Astronomy and astrophysics core library
License:        BSD-3-Clause
URL:            https://www.astropy.org/
VCS:            git:https://github.com/astropy/astropy.git
#!RemoteAsset:  sha256:45ca31d5b91fa294cd590a4791a32db94de7f9c8a343155f4d5877baa82351da
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l astropy
# Build helper modules require the source tree as their working directory
BuildOption(check):  -e 'astropy.io.ascii.setup_package'
BuildOption(check):  -e 'astropy.table.setup_package'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(astropy-iers-data)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(dask)
BuildRequires:  python3dist(extension-helpers)
BuildRequires:  python3dist(fitsio)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyarrow)
BuildRequires:  python3dist(pyerfa)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-remotedata)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Astropy is a core Python package for astronomy and astrophysics.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.rst licenses/
%{_bindir}/fits2bitmap
%{_bindir}/fitscheck
%{_bindir}/fitsdiff
%{_bindir}/fitsheader
%{_bindir}/fitsinfo
%{_bindir}/samp_hub
%{_bindir}/showtable
%{_bindir}/showtable-astropy
%{_bindir}/volint
%{_bindir}/wcslint

%changelog
%autochangelog
