# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cfitsio
Version:        4.6.4
Release:        %autorelease
Summary:        Library for reading and writing FITS data files
License:        CFITSIO
URL:            https://heasarc.gsfc.nasa.gov/fitsio/
VCS:            git:https://github.com/HEASARC/cfitsio.git
#!RemoteAsset:  sha256:fb09b18638b0a71fa3c2612aac4fafd29cae8642266ba690803eb95f037a5268
Source0:        https://github.com/HEASARC/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
BuildSystem:    cmake

# Use the system cfortran header, following Debian's 4.6.4 packaging.
# https://salsa.debian.org/debian-astro-team/cfitsio/-/blob/debian/4.6.4-1/debian/patches/02-system-cfortran.patch
Patch2000:      2000-use-system-cfortran.patch

BuildOption(conf):  -DUSE_BZIP2=ON
BuildOption(conf):  -DUSE_PTHREADS=ON

BuildRequires:  cfortran
BuildRequires:  cmake
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(zlib)

%description
CFITSIO is a library of C and Fortran routines for reading and writing FITS
data files.

%package        devel
Summary:        Development files for CFITSIO
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and pkg-config metadata for developing applications with CFITSIO.

%prep -a
rm cfortran.h

%files
%license licenses/License.txt
%{_bindir}/cookbook
%{_bindir}/fitscopy
%{_bindir}/fitsverify
%{_bindir}/fpack
%{_bindir}/funpack
%{_bindir}/imcopy
%{_bindir}/smem
%{_bindir}/speed
%{_libdir}/libcfitsio.so.*

%files devel
%{_includedir}/cfitsio_export.h
%{_includedir}/fitsio.h
%{_includedir}/fitsio2.h
%{_includedir}/longnam.h
%{_libdir}/libcfitsio.so
%{_libdir}/cmake/cfitsio/
%{_libdir}/pkgconfig/cfitsio.pc

%changelog
%autochangelog
