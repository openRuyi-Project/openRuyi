# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           pigz
Version:        2.8
Release:        %autorelease
License:        Zlib
Summary:        Parallel implementation of gzip
URL:            https://zlib.net/pigz/
VCS:            git:https://github.com/madler/pigz.git
#!RemoteAsset
Source0:        https://www.zlib.net/%{name}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  which
BuildRequires:  pkgconfig(zlib)

%description
pigz, which stands for parallel implementation of gzip,
is a fully functional replacement for gzip that exploits
multiple processors and multiple cores to the hilt when
compressing data.

# no configure script
%conf
:

%install
install -p -D pigz $RPM_BUILD_ROOT%{_bindir}/pigz
pushd $RPM_BUILD_ROOT%{_bindir}; ln pigz unpigz; popd
install -p -D pigz.1 -m 0644 $RPM_BUILD_ROOT%{_datadir}/man/man1/pigz.1

%files
%doc pigz.pdf README
%{_bindir}/pigz
%{_bindir}/unpigz
%{_datadir}/man/man1/pigz.*

%changelog
%autochangelog
