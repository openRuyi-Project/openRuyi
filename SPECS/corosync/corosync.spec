# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           corosync
Version:        3.1.10
Release:        %autorelease
Summary:        The Corosync Cluster Engine and Application Programming Interfaces
License:        BSD-3-Clause
URL:            https://corosync.github.io/corosync/
VCS:            git:https://github.com/corosync/corosync.git
#!RemoteAsset:  sha256:03c55b984380bdb68ecd8d0f9cb1f9f0c2a7e6e7b7f437becc33e9a804018340
Source:         https://github.com/corosync/corosync/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-secure-build
BuildOption(conf):  --enable-systemd
BuildOption(conf):  --enable-xmlconf
BuildOption(conf):  --with-initddir=%{_initrddir}
BuildOption(conf):  --with-systemddir=%{_unitdir}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  groff
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig(libknet)
BuildRequires:  pkgconfig(libqb)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(zlib)

Requires:       kronosnet%{?_isa} >= 1.18

%description
The Corosync Cluster Engine implements virtual synchrony, a model of
distributed coordination used to keep state machines in lock-step
across a cluster. This package contains the executive, the default
APIs and libraries, the default configuration files, and a set of
command-line tools.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the header files, shared library symlinks and
pkg-config files needed to develop applications that link against the
Corosync libraries.

%conf -p
autoreconf -fiv

%install -a
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -m 644 init/corosync.sysconfig.example \
    %{buildroot}%{_sysconfdir}/sysconfig/corosync
install -m 644 tools/corosync-notifyd.sysconfig.example \
    %{buildroot}%{_sysconfdir}/sysconfig/corosync-notifyd
# remove duped documents
rm -rf %{buildroot}%{_docdir}/%{name}

%check
# Upstream tests need a privileged runtime environment with networking
# and shared memory that are not available in the build chroot.

%post
%systemd_post corosync.service corosync-notifyd.service

%preun
%systemd_preun corosync.service corosync-notifyd.service

%postun
%systemd_postun_with_restart corosync.service corosync-notifyd.service

%files
%license LICENSE
%{_sbindir}/corosync
%{_sbindir}/corosync-keygen
%{_sbindir}/corosync-cmapctl
%{_sbindir}/corosync-cfgtool
%{_sbindir}/corosync-cpgtool
%{_sbindir}/corosync-quorumtool
%{_sbindir}/corosync-notifyd
%{_bindir}/corosync-blackbox
%{_bindir}/corosync-xmlproc
%dir %{_sysconfdir}/corosync
%dir %{_sysconfdir}/corosync/uidgid.d
%config(noreplace) %{_sysconfdir}/corosync/corosync.conf.example
%config(noreplace) %{_sysconfdir}/sysconfig/corosync
%config(noreplace) %{_sysconfdir}/sysconfig/corosync-notifyd
%config(noreplace) %{_sysconfdir}/logrotate.d/corosync
%dir %{_datadir}/corosync
%{_datadir}/corosync/xml2conf.xsl
# corosync runtime libraries, kept in the main package per openRuyi
# splitpackage policy (no separate -libs subpackage).
%{_libdir}/libcfg.so.*
%{_libdir}/libcmap.so.*
%{_libdir}/libcorosync_common.so.*
%{_libdir}/libcpg.so.*
%{_libdir}/libquorum.so.*
%{_libdir}/libsam.so.*
%{_libdir}/libvotequorum.so.*
%{_unitdir}/corosync.service
%{_unitdir}/corosync-notifyd.service
%{_mandir}/man5/corosync.conf.5*
%{_mandir}/man5/corosync.xml.5*
%{_mandir}/man5/votequorum.5*
%{_mandir}/man7/cmap_keys.7*
%{_mandir}/man7/corosync_overview.7*
%{_mandir}/man8/corosync.8*
%{_mandir}/man8/corosync-blackbox.8*
%{_mandir}/man8/corosync-cfgtool.8*
%{_mandir}/man8/corosync-cmapctl.8*
%{_mandir}/man8/corosync-cpgtool.8*
%{_mandir}/man8/corosync-keygen.8*
%{_mandir}/man8/corosync-notifyd.8*
%{_mandir}/man8/corosync-quorumtool.8*
%{_mandir}/man8/corosync-xmlproc.8*

%files devel
%dir %{_includedir}/corosync
%{_includedir}/corosync/cfg.h
%{_includedir}/corosync/cmap.h
%{_includedir}/corosync/corodefs.h
%{_includedir}/corosync/corotypes.h
%{_includedir}/corosync/cpg.h
%{_includedir}/corosync/hdb.h
%{_includedir}/corosync/quorum.h
%{_includedir}/corosync/sam.h
%{_includedir}/corosync/votequorum.h
%{_libdir}/libcfg.so
%{_libdir}/libcmap.so
%{_libdir}/libcorosync_common.so
%{_libdir}/libcpg.so
%{_libdir}/libquorum.so
%{_libdir}/libsam.so
%{_libdir}/libvotequorum.so
%{_libdir}/pkgconfig/corosync.pc
%{_libdir}/pkgconfig/libcfg.pc
%{_libdir}/pkgconfig/libcmap.pc
%{_libdir}/pkgconfig/libcorosync_common.pc
%{_libdir}/pkgconfig/libcpg.pc
%{_libdir}/pkgconfig/libquorum.pc
%{_libdir}/pkgconfig/libsam.pc
%{_libdir}/pkgconfig/libvotequorum.pc
%{_mandir}/man3/cmap_*.3*
%{_mandir}/man3/cpg_*.3*
%{_mandir}/man3/quorum_*.3*
%{_mandir}/man3/sam_*.3*
%{_mandir}/man3/votequorum_*.3*

%changelog
%autochangelog
