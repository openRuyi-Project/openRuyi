# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Suyun114 <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libsigsegv
Version:        2.15
Release:        %autorelease
Summary:        Library for Handling Page Faults in User Mode
License:        GPL-2.0-or-later
URL:            https://www.gnu.org/software/libsigsegv/
VCS:            git:https://git.savannah.gnu.org/git/libsigsegv.git
#!RemoteAsset:  sha256:036855660225cb3817a190fc00e6764ce7836051bacb48d35e26444b8c1729d9
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:72a772fbea15850a1dac43bf4a05822367fb29725d8e0d69ae4759953874f3fe
Source1:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
BuildSystem:    autotools

BuildOption(conf):  --enable-shared

%description
This is a library for handling page faults in user mode. A page fault occurs
when a program tries to access to a region of memory that is currently not
available.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This is a library for handling page faults in user mode. A page fault occurs
when a program tries to access to a region of memory that is currently not
available.

%files
%license COPYING
%doc AUTHORS ChangeLog* NEWS PORTING README
%{_libdir}/libsigsegv.so.*

%files devel
%{_includedir}/sigsegv.h
%{_libdir}/libsigsegv.so
%{_libdir}/libsigsegv.a

%changelog
%autochangelog
