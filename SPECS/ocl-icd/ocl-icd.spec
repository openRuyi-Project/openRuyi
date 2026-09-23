# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ocl-icd
Version:        2.3.5
Release:        %autorelease
Summary:        OpenCL Library (Installable Client Library) Bindings
License:        BSD-2-Clause
URL:            https://github.com/OCL-dev/ocl-icd
VCS:            git:https://github.com/OCL-dev/ocl-icd.git
#!RemoteAsset:  sha256:cdd7984425fa92d37273eee4180b5f57b047eda6dd8fd623e58498f844b09b75
Source0:        https://github.com/OCL-dev/ocl-icd/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  ruby
BuildRequires:  opencl-headers

%description
This package contains the development files for the OpenCL ICD bindings.

%package        devel
Summary:        Development files for ocl-icd
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the development files for the OpenCL ICD bindings.

%conf -p
autoreconf -fiv

%install -a
rm -vrf %{buildroot}%{_defaultdocdir}

%files
%doc NEWS README
%license COPYING
%{_libdir}/libOpenCL.so.1
%{_libdir}/libOpenCL.so.1.0.0

%files devel
%doc ocl_icd_loader_gen.map ocl_icd_bindings.c
%{_includedir}/ocl_icd.h
%{_bindir}/cllayerinfo
%{_libdir}/libOpenCL.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/OpenCL.pc

%changelog
%autochangelog
