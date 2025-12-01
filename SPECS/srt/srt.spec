# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           srt
Version:        1.5.4
Release:        %autorelease
Summary:        Secure Reliable Transport protocol tools
License:        MPL-2.0
URL:            https://www.srtalliance.org
#!RemoteAsset
Source:         https://github.com/Haivision/srt/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          0001-build-Update-for-compatibility-with-CMake-4.x-3167.patch
BuildSystem:    cmake

BuildOption(conf): -DENABLE_STATIC=OFF
BuildOption(conf): -DENABLE_UNITTESTS=ON
BuildOption(conf): -DENABLE_GETNAMEINFO=ON
BuildOption(conf): -DENABLE_BONDING=ON
BuildOption(conf): -DENABLE_PKTINFO=ON
BuildOption(conf): -DUSE_ENCLIB=gnutls

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  gnutls-devel
BuildRequires:  nettle-devel
BuildRequires:  pkgconfig(gmock)
BuildRequires:  gtest-devel

%description
Secure Reliable Transport (SRT) is an open source transport technology that
optimizes streaming performance across unpredictable networks.
This package contains the command-line tools.

%package devel
Summary:        Development libraries and headers for SRT
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the libraries and header files needed for developing
applications that use the Secure Reliable Transport protocol.

%install -a
rm -f %{buildroot}/%{_libdir}/pkgconfig/haisrt.pc

%check
%ctest --parallel 1 -E TestIPv6

%files
%license LICENSE
%doc README.md docs
%{_bindir}/srt-ffplay
%{_bindir}/srt-file-transmit
%{_bindir}/srt-live-transmit
%{_bindir}/srt-tunnel
%{_libdir}/libsrt.so.1.5*

%files devel
%doc examples
%{_includedir}/srt/
%{_libdir}/libsrt.so
%{_libdir}/pkgconfig/srt.pc

%changelog
%{?autochangelog}
