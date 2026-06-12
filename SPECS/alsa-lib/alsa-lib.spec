# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond docs 1
%bcond lto 1

%if %{with lto}
# Needed for symbol versioning.
%global _lto_cflags -flto -ffat-lto-objects -flto-partition=none
%endif

Name:           alsa-lib
Version:        1.2.15.3
Release:        %autorelease
Summary:        The Advanced Linux Sound Architecture (ALSA) library
License:        LGPL-2.1-or-later
URL:            http://www.alsa-project.org/
#!RemoteAsset:  sha256:7b079d614d582cade7ab8db2364e65271d0877a37df8757ac4ac0c8970be861e
Source0:        https://www.alsa-project.org/files/pub/lib/%{name}-%{version}.tar.bz2
Source1:        asound.conf
Source2:        modprobe-dist-alsa.conf
Source3:        modprobe-dist-oss.conf
BuildSystem:    autotools

# configure options
BuildOption(conf):  --disable-aload
BuildOption(conf):  --with-plugindir=%{_libdir}/alsa-lib
BuildOption(conf):  --disable-alisp
BuildOption(build):  V=1
BuildOption(install):  DESTDIR=%{buildroot}

%if %{with docs}
BuildRequires:  doxygen
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc

%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes the ALSA runtime libraries to simplify application
programming and provide higher level functionality as well as support for
the older OSS API, providing binary compatibility for most OSS programs.

%package        devel
Summary:        Development files from the ALSA library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes the ALSA development libraries for developing
against the ALSA libraries and interfaces.

%prep
%autosetup -p1

%conf -p
autoreconf -vif

%build -p
# fix libtool rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool || :
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool || :

%build -a
%if %{with docs}
%make_build doc
%endif

%install -a
# Install global configuration files
mkdir -p -m 755 %{buildroot}/etc
install -p -m 644 %{SOURCE1} %{buildroot}/etc

# Install the modprobe files for ALSA
mkdir -p -m 755 %{buildroot}%{_prefix}/lib/modprobe.d
install -p -m 644 %{SOURCE2} %{buildroot}%{_prefix}/lib/modprobe.d/dist-alsa.conf
# bug#926973, place this file to the doc directory
install -p -m 644 %{SOURCE3} .

# Remove /usr/include/asoundlib.h
rm -f %{buildroot}%{_includedir}/asoundlib.h

%files
%license COPYING
%doc doc/asoundrc.txt modprobe-dist-oss.conf
%config %{_sysconfdir}/asound.conf
%{_libdir}/libasound.so.*
%{_libdir}/libatopology.so.*
%{_bindir}/aserver
#{_libdir}/alsa-lib/
%{_datadir}/alsa/
%exclude %{_datadir}/alsa/ucm
%exclude %{_datadir}/alsa/ucm2
%exclude %{_datadir}/alsa/topology
%{_prefix}/lib/modprobe.d/dist-*

%files devel
%doc TODO
%if %{with docs}
%doc doc/doxygen/
%endif
%{_includedir}/alsa/
%{_includedir}/sys/asoundlib.h
%{_libdir}/libasound.so
%{_libdir}/libatopology.so
%{_libdir}/pkgconfig/alsa.pc
%{_libdir}/pkgconfig/alsa-topology.pc
%{_datadir}/aclocal/alsa.m4

%changelog
%autochangelog
