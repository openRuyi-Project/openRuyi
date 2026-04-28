# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fribidi
Version:        1.0.16
Release:        %autorelease
Summary:        Library implementing the Unicode Bidirectional Algorithm
License:        LGPL-2.1-or-later
URL:            https://github.com/fribidi/fribidi
#!RemoteAsset
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Ddocs=false

BuildRequires:  meson

%description
A library to handle bidirectional scripts (for example Hebrew, Arabic),
so that the display is done in the proper way; while the text data itself
is always written in logical order.

%package        devel
Summary:        Libraries and include files for FriBidi
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Include files and libraries needed for developing applications which use
FriBidi.

%files
%doc README AUTHORS ChangeLog THANKS NEWS TODO
%license COPYING
%{_bindir}/fribidi
%{_libdir}/libfribidi.so.0*

%files devel
%{_includedir}/fribidi
%{_libdir}/libfribidi.so
%{_libdir}/pkgconfig/fribidi.pc

%changelog
%{?autochangelog}
