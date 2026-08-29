# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libftdi
Version:        1.6rc1
Release:        %autorelease
Summary:        A library to talk to FTDI chips
License:        GPL-2.0-only AND LGPL-2.1-only
URL:            https://www.intra2net.com/en/developer/libftdi/
VCS:            git://developer.intra2net.com/libftdi
#!RemoteAsset:  sha256:6a065fc6d2c39c25e724c8da62d0dfb602548c7fb583a24a91c094d15d5dfee5
Source:         https://www.intra2net.com/en/developer/libftdi/download/libftdi1-%{version}.tar.bz2
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTS=ON
BuildOption(conf):  -DPYTHON_BINDINGS=ON
BuildOption(conf):  -DDOCUMENTATION=ON
BuildOption(conf):  -DFTDIPP=ON
BuildOption(conf):  -DSTATICLIBS=OFF

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  swig
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  boost-devel

Requires:       libconfuse
Requires:       libusb

%description
libFTDI is an open source library to talk to FTDI chips.

%package        devel
Summary:        Development files for libFTDI
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and static libraries for libFTDI.

%package     -n python-%{name}
Summary:        Python bindings for libFTDI
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-%{name} = %{version}-%{release}
Provides:       python3-%{name}%{?_isa} = %{version}-%{release}
%python_provide python3-%{name}

%description -n python-%{name}
Python bindings for libFTDI.

%files
%{_libdir}/libftdi1.so.2.6.0
%{_libdir}/libftdi1.so.2
%{_libdir}/libftdipp1.so.2.6.0
%{_libdir}/libftdipp1.so.3

%files devel
%{_bindir}/ftdi_eeprom
%{_bindir}/libftdi1-config
%doc %{_docdir}/libftdi1/example.conf
%{_includedir}/libftdi1/ftdi.h
%{_includedir}/libftdi1/ftdi.hpp
%{_libdir}/libftdi1.so
%{_libdir}/libftdipp1.so
%{_libdir}/pkgconfig/libftdi1.pc
%{_libdir}/pkgconfig/libftdipp1.pc
%{_libdir}/cmake/libftdi1/LibFTDI1Config.cmake
%{_libdir}/cmake/libftdi1/LibFTDI1ConfigVersion.cmake
%{_libdir}/cmake/libftdi1/UseLibFTDI1.cmake

%files -n python-%{name}
%{python3_sitearch}/ftdi1.py
%{python3_sitearch}/_pyftdi1.so
%{_datadir}/libftdi/examples/simple.py
%{_datadir}/libftdi/examples/complete.py
%{_datadir}/libftdi/examples/cbus.py

%changelog
%autochangelog
