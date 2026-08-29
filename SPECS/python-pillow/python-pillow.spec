# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pillow

Name:           python-%{srcname}
Version:        12.0.0
Release:        %autorelease
Summary:        Python image processing library
License:        MIT
URL:            http://python-pillow.github.io/
#!RemoteAsset:  sha256:87d4f8125c9988bfbed67af47dd7a953e2fc7b0cc1e7800ec6d2080d490bb353
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l PIL

BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}
Provides:       python3-imaging = %{version}-%{release}
Provides:       python3-imaging%{?_isa} = %{version}-%{release}

%description
Python image processing library, fork of the Python Imaging Library (PIL).

%generate_buildrequires
%pyproject_buildrequires

%install -a
install -d %{buildroot}/%{_includedir}/python%{python3_version}/Imaging
install -m 644 src/libImaging/*.h %{buildroot}/%{_includedir}/python%{python3_version}/Imaging

# Maybe add AVIF, LIBIMAGEQUANT, OPENJPEG, RAQM, TKINTER & XCB later for testing
%check

%files -f %{pyproject_files}
%doc README.md CHANGES.rst
%license docs/COPYING
%{_includedir}/python%{python3_version}/Imaging/

%changelog
%autochangelog
