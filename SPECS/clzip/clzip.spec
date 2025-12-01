# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           clzip
Version:        1.15
Release:        %autorelease
Summary:        Small, stand-alone lzip compressor and decompressor
License:        GPLv2+ AND BSD-2-Clause
URL:            https://www.nongnu.org/lzip/clzip.html
#!RemoteAsset
Source0:         https://download.savannah.nongnu.org/releases/lzip/clzip/clzip-%{version}.tar.gz
#!RemoteAsset
Source1:         https://download.savannah.nongnu.org/releases/lzip/clzip/clzip-%{version}.tar.gz.sig
BuildSystem:    autotools
BuildRequires:  gcc
BuildRequires:  texinfo

%description
Clzip is a compressor and decompressor for files in the lzip compression
format (.lz), written as a single small C tool with no dependencies.  This makes
it well-suited to embedded and other systems without a C++ compiler, or for use
in other applications like package managers.
Clzip is intended to be fully compatible with the regular lzip package.

%install -a
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%doc README
%license COPYING
%{_bindir}/clzip
%{_mandir}/man1/*
%{_infodir}/*

%changelog
%{?autochangelog}
