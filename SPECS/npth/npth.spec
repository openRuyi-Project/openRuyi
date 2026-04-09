# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Suyun114 <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           npth
Version:        1.8
Release:        %autorelease
Summary:        GNU Portable Threads library
License:        LGPL-2.1-or-later
URL:            https://gnupg.org/software/npth/
VCS:            git:https://git.gnupg.org/npth.git
#!RemoteAsset
Source:         https://gnupg.org/ftp/gcrypt/%{name}/%{name}-%{version}.tar.bz2
#!RemoteAsset
Source2:        https://gnupg.org/ftp/gcrypt/%{name}/%{name}-%{version}.tar.bz2.sig
BuildSystem:    autotools

BuildOption(conf):  --disable-static

%description
nPth is a non-preemptive threads implementation using an API very similar
to the one known from GNU Pth. It has been designed as a replacement of
GNU Pth for non-ancient operating systems. In contrast to GNU Pth is is
based on the system's standard threads implementation. Thus nPth allows
the use of libraries which are not compatible to GNU Pth.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%files
%license COPYING.LIB
%{_libdir}/lib%{name}.so.*

%files devel
%license COPYING.LIB
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_datadir}/aclocal/%{name}.m4

%changelog
%autochangelog
