# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libtasn1
Version:        4.20.0
Release:        %autorelease
Summary:        ASN.1 parsing library
License:        GFDL-1.3-or-later AND GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://www.gnu.org/software/libtasn1/
#!RemoteAsset
Source0:        http://ftpmirror.gnu.org/gnu/libtasn1/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        http://ftpmirror.gnu.org/gnu/libtasn1/%{name}-%{version}.tar.gz.sig

BuildRequires:  perl
BuildRequires:  autoconf
BuildRequires:  automake
BuildSystem:    autotools
BuildOption(conf):   --disable-static
%description
This is the ASN.1 library used by GNUTLS. Abstract Syntax Notation One (ASN.1)
is a standardized data description and serialization language.

%package devel
Summary:        Development files for the ASN.1 parsing library
License:        GFDL-1.3-or-later AND LGPL-2.1-or-later
Requires:       %{name} = %{version}

%description devel
This is the ASN.1 library used by GNUTLS. Abstract Syntax Notation One (ASN.1)
is a standardized data description and serialization language.

%files
%license COPYING
%{_bindir}/*
%{_libdir}/*.so*
%{_infodir}/*
%{_mandir}/man?/*


%files devel
%license COPYING.LESSERv2
%doc NEWS README THANKS
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libtasn1.pc
%{_mandir}/man3/*

%changelog
%{?autochangelog}
