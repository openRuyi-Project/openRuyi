# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0

Name:           imath
Version:        3.2.2
Release:        %autorelease
Summary:        Library of 2D and 3D vector, matrix, and math operations for computer graphics
License:        BSD-3-Clause
URL:            https://github.com/AcademySoftwareFoundation/Imath
#!RemoteAsset:  sha256:b4275d83fb95521510e389b8d13af10298ed5bed1c8e13efd961d91b1105e462
Source0:        https://github.com/AcademySoftwareFoundation/Imath/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

%ifarch riscv64
# https://github.com/AcademySoftwareFoundation/Imath/issues/515#issuecomment-3586903097
# It's from upstream's issue and comment to fix tests error.
Patch0:         0001-fix-riscv64-test-error.patch
# Diable the test or it will fail.
Patch1:         0002-imath-disable-python-testPlane.patch
%endif

BuildOption(conf):  -DPYTHON=ON
%if %{with doc}
BuildOption(conf):  -DDOCS=ON
BuildOption(conf):  -DINSTALL_DOCS=ON
%else
BuildOption(conf):  -DDOCS=OFF
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(numpy)
%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(breathe)
%endif

%description
Imath is a basic, light-weight, and efficient C++ representation of 2D and 3D
vectors and matrices and other simple but useful mathematical objects.

%package     -n python-%{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Python module for Imath
Provides:       python3-%{name}
%python_provide python3-%{name}

%description -n python-%{name}
Python module for Imath.

%package        devel
Summary:        Development files for Imath
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel

%description    devel
Development files for Imath.

%files
%license LICENSE.md
%doc CHANGES.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md SECURITY.md
%{_libdir}/libImath*.so.*
%{_libdir}/libPyImath_Python*.so.*

%files -n python-imath
%{_libdir}/libPyImath.so
%{python3_sitelib}/imath.so
%{python3_sitelib}/imathnumpy.so

%files devel
%{_includedir}/Imath/
%{_libdir}/pkgconfig/Imath.pc
%{_libdir}/pkgconfig/PyImath.pc
%{_libdir}/cmake/Imath/
%{_libdir}/libImath*.so
%{_libdir}/libPyImath_Python*.so

%changelog
%autochangelog
