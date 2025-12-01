# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           soxr
Version:        0.1.3
Release:        %autorelease
Summary:        The SoX Resampler library
License:        LGPL-2.1-or-later
URL:            https://github.com/chirlu/soxr
#!RemoteAsset
Source:         https://github.com/chirlu/soxr/archive/refs/tags/%{version}.tar.gz
Patch:          0001-soxr-cmake.patch
BuildSystem:    cmake

BuildOption(conf): -DWITH_CR32S=FALSE
BuildOption(conf): -DCMAKE_POLICY_VERSION_MINIMUM:STRING=3.5

BuildRequires:  cmake
BuildRequires:  gcc

%description
The SoX Resampler library `libsoxr' performs one-dimensional sample-rate
conversion -- it may be used, for example, to resample PCM-encoded audio.
This package contains the shared library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%install -a
# Remove docs and use the rpmbuild macro instead
rm -rf %{buildroot}%{_docdir}/*

%files
%doc NEWS README
%license LICENCE
%{_libdir}/*.so.*

%files devel
%doc examples/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/soxr-lsr.pc
%{_libdir}/pkgconfig/soxr.pc

%changelog
%{?autochangelog}
